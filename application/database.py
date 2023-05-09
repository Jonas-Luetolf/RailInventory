import sqlite3
from pathlib import Path
from enum import Enum


class TrainType(Enum):
    LOCOMOTIVE = 1
    WAGON = 2


LOCOMOTIVE_DATA_STRUCTURE = {
    "id": None,
    "name": None,
    "number": None,
    "address": None,
    "protocol": None,
    "sound": None,
    "ltype": None,
    "vmax": None,
    "power": None,
    "year": None,
    "modelproducer": None,
    "producer": None,
    "comment": None,
}

WAGON_DATA_STRUCTURE = {
    "id": None,
    "name": None,
    "number": None,
    "producer": None,
    "comment": None,
}


def adjust_train_values(
    train_type: TrainType, values: dict, id_req: bool = True
) -> dict:
    if train_type == TrainType.LOCOMOTIVE:
        excepted_dict = LOCOMOTIVE_DATA_STRUCTURE.copy()

    else:
        excepted_dict = WAGON_DATA_STRUCTURE.copy()

    if id_req == False:
        del excepted_dict["id"]

    if set(values.keys()) != set(excepted_dict.keys()):
        raise ValueError(
            "Invalid data structure: expected keys are {}".format(excepted_dict.keys())
        )

    # order values
    for key in excepted_dict:
        excepted_dict[key] = values[key]

    return excepted_dict


class DataBase:
    """
    used to write to and read from a local DataBase
    """

    def __init__(self, file: Path) -> None:
        """
        connets to file and creates cursor

        :param file: filename of sqlite database
        """

        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

        self._create_table()

    def close(self) -> None:
        """
        close the db connection

        :return: None
        """

        self.conn.close()

    def _create_table(self) -> None:
        """
        creates new tabels if one doesn't exists

        :return: None
        """

        query = """CREATE TABLE IF NOT EXISTS LOCOMOTIVE 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,
        number INTEGER, address INTEGER, protocol TEXT,sound INTEGER, ltype TEXT, vmax INTEGER, power INTEGER, year INTEGER, modelproducer TEXT, producer TEXT, comment TEXT)"""

        self.cursor.execute(query)
        self.conn.commit()

        query = """CREATE TABLE IF NOT EXISTS WAGON 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,
        number INTEGER, producer TEXT, comment TEXT)"""

        self.cursor.execute(query)
        self.conn.commit()

    def get_train_by_name(self, train_type: TrainType, name: str) -> dict:
        """
        gets the train by name

        :param train_type: type of the train (locomotive or wagon)
        :param name: name of the train to search for
        :return: the data of the searched train
        """

        self.cursor.row_factory = sqlite3.Row
        query = f"""SELECT * FROM {train_type.name} WHERE name = ?"""

        result = self.cursor.execute(query, (name,)).fetchall()

        return dict(result[0])

    def get_train_by_id(self, train_type: TrainType, id: int) -> dict:
        """
        gets a train by its id

        :param train_type: type of the train
        :param id: id of the train
        :return: the data of the searched train
        """
        self.cursor.row_factory = sqlite3.Row
        query = f"""SELECT * FROM {train_type.name} WHERE id = ?"""

        result = self.cursor.execute(query, (id,)).fetchall()

        return dict(result[0])

    def get_all_trains(self, train_type: TrainType) -> list:
        """
        gets all trains from the database

        :param train_type: type of the train
        :return: list of all trains
        """
        self.cursor.row_factory = None
        query = f"""SELECT * FROM {train_type.name}"""

        result = self.cursor.execute(query).fetchall()

        return result

    def add_train(self, train_type: TrainType, **values) -> None:
        """
        add a new trains

        :param train_type: type of the train
        :param values: all values of the train
        :return: None
        """

        if train_type == TrainType.LOCOMOTIVE:
            params = adjust_train_values(TrainType.LOCOMOTIVE, values, id_req=False)
            query = """INSERT INTO LOCOMOTIVE (name, number, address,protocol, sound, ltype, vmax, power, year, modelproducer, producer, comment)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)"""

        else:
            params = adjust_train_values(TrainType.WAGON, values, id_req=False)
            query = """ INSERT INTO WAGON (name, number, producer,comment) VALUES (?, ?, ?, ?)"""

        self.cursor.execute(query, tuple(value for value in params.values()))
        self.conn.commit()

    def update_train(self, train_type: TrainType, **values):
        if train_type == TrainType.LOCOMOTIVE:
            params = adjust_train_values(TrainType.LOCOMOTIVE, values, id_req=True)
            query = """UPDATE LOCOMOTIVE SET name = ?, number = ?, address = ?,protocol=?, sound = ?, ltype = ?, vmax = ?, power = ?, year = ?, modelproducer = ?, producer = ?, comment = ? WHERE id = ?"""

        else:
            params = adjust_train_values(TrainType.WAGON, values, id_req=True)
            query = """UPDATE WAGON SET name = ?, number = ?, producer = ?, comment = ? WHERE id = ?"""

        self.cursor.execute(
            query,
            tuple(value for value in list(params.values())[1:])
            + (list(params.values())[0],),
        )
        self.conn.commit()
