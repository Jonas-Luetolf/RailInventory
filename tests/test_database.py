from pathlib import Path
from unittest import TestCase
from application import database as db
import tempfile
import sqlite3

TESTENTRY = {
    "id": 1,
    "name": "test_entry",
    "number": 123,
    "address": 123,
    "sound": 1,
    "ltype": "test",
    "vmax": 123,
    "power": 123,
    "year": 1234,
    "modelproducer": "test",
    "producer": "test",
    "comment": "test",
}


class test_views(TestCase):
    def setUp(self):
        _, self.db_file = tempfile.mkstemp()
        print(self.db_file)
        self.db = db.DataBase(Path(self.db_file))

        conn = sqlite3.connect(self.db_file)
        conn.cursor().execute(
            f"""INSERT INTO LOCOMOTIVE (name, number, address, sound, ltype, vmax, power, year, modelproducer, producer, comment)
        VALUES {tuple(list(TESTENTRY.values())[1:])}"""
        )
        conn.commit()
        conn.close()

    def test_get_all(self):
        all_trains = self.db.get_all_trains(db.TrainType.LOCOMOTIVE)

        self.assertIsInstance(all_trains, list)
        self.assertIsInstance(all_trains[0], tuple)
        self.assertEqual(all_trains[0], tuple(TESTENTRY.values()))

    def test_get_by_name(self):
        train = self.db.get_train_by_name(db.TrainType.LOCOMOTIVE, "test_entry")

        self.assertIsInstance(train, dict)
        self.assertEqual(train, TESTENTRY)

    def test_get_by_id(self):
        train = self.db.get_train_by_id(db.TrainType.LOCOMOTIVE, 1)

        self.assertIsInstance(train, dict)
        self.assertEqual(train, TESTENTRY)

    def test_add(self):
        testdata = TESTENTRY.copy()
        del testdata["id"]
        testdata["name"] = "add_test"

        self.db.add_train(db.TrainType.LOCOMOTIVE, **testdata)

        testdata.update({"id": 2})
        getdata = self.db.get_train_by_name(db.TrainType.LOCOMOTIVE, "add_test")

        self.assertEqual(testdata, getdata)

    def test_update(self):
        testdata = TESTENTRY
        testdata["comment"] = "update_test"

        self.db.update_train(db.TrainType.LOCOMOTIVE, **testdata)
        getdata = self.db.get_train_by_id(db.TrainType.LOCOMOTIVE, 1)

        self.assertEqual(testdata, getdata)

    def tearDown(self):
        self.db.close()
