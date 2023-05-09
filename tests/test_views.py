from pathlib import Path
from application import create_app
from flask_testing import TestCase
import tempfile
import sqlite3
from application import database as db
from .testdata import TESTLOCOMOTIVE, TESTWAGON


class test_views(TestCase):
    def create_app(self):
        app = create_app()
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False

        _, self.db_file = tempfile.mkstemp()
        app.config["DATABASE"] = Path(self.db_file)

        self.db = db.DataBase(Path(self.db_file))
        conn = sqlite3.connect(self.db_file)
        conn.cursor().execute(
            f"""INSERT INTO LOCOMOTIVE (name, number, address,protocol, sound, ltype, vmax, power, year, modelproducer, producer, comment)
        VALUES {tuple(list(TESTLOCOMOTIVE.values())[1:])}"""
        )
        conn.cursor().execute(
            f"""INSERT INTO WAGON (name, number, producer, comment)
        VALUES {tuple(list(TESTWAGON.values())[1:])}"""
        )
        conn.commit()
        conn.close()

        return app

    def setUp(self):
        self.client = self.app.test_client()

    def test_index(self):
        self.assert200(self.client.get("/"))

    def test_add_get(self):
        self.assert200(self.client.get("/add/locomotive"))
        self.assert200(self.client.get("/add/wagon"))

    def test_add_post(self):
        response = self.client.post("/add/locomotive", data=TESTLOCOMOTIVE)
        assert response.status_code == 302
        assert response.headers["Location"] == "/"
        assert len(self.db.get_all_trains(db.TrainType.LOCOMOTIVE)) == 2

        response = self.client.post("/add/wagon", data=TESTWAGON)
        assert response.status_code == 302
        assert response.headers["Location"] == "/"
        assert len(self.db.get_all_trains(db.TrainType.WAGON)) == 2

    def test_edit_get(self):
        self.assert200(self.client.get("/edit/locomotive", query_string={"id": 1}))
        self.assert200(self.client.get("/edit/wagon", query_string={"id": 1}))

    def test_edit_post(self):
        temp_TESTLOCOMOTIVE = TESTLOCOMOTIVE.copy()
        temp_TESTWAGON = TESTWAGON.copy()
        temp_TESTLOCOMOTIVE["name"] = "edit_post"
        temp_TESTWAGON["name"] = "edit_post"

        response = self.client.post("/edit/locomotive", data=temp_TESTLOCOMOTIVE)
        assert response.status_code == 302
        assert response.headers["Location"] == "/"
        assert len(self.db.get_all_trains(db.TrainType.LOCOMOTIVE)) == 1
        assert (
            self.db.get_train_by_id(db.TrainType.LOCOMOTIVE, 1) == temp_TESTLOCOMOTIVE
        )

        response = self.client.post("/edit/wagon", data=temp_TESTWAGON)
        assert response.status_code == 302
        assert response.headers["Location"] == "/"
        assert len(self.db.get_all_trains(db.TrainType.WAGON)) == 1
        assert self.db.get_train_by_id(db.TrainType.WAGON, 1) == temp_TESTWAGON
