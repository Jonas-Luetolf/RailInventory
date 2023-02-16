import sqlite3
from enum import Enum


class TrainType(Enum):
    LOCOMOTIVE = 1
    WAGON = 2


class DataBase:
    """
    used to write to and read from a local DataBase
    """

    def __init__(self, file: str) -> None:
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
        number INTEGER, producer TEXT, comment TEXT)"""

        self.cursor.execute(query)
        self.conn.commit()

        query = """CREATE TABLE IF NOT EXISTS WAGON 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,
        number INTEGER, producer TEXT, comment TEXT)"""

        self.cursor.execute(query)
        self.conn.commit()

    def get_train_by_name(self, train_type: TrainType, name: str) -> list:
        """
        gets the train by name

        :param train_type: type of the train (locomotive or wagon)
        :param name: name of the train to search for
        :return: the data of the searched train
        """

        query = f"""SELECT * FROM {train_type.name} WHERE name = ?"""

        result = self.cursor.execute(query, (name,)).fetchall()

        return result

    def get_all_trains(self, train_type: TrainType) -> list:
        """
        gets all trains from the database

        :param train_type: type of the train
        :return: list of all trains
        """

        query = f"""SELECT * FROM {train_type.name}"""

        result = self.cursor.execute(query).fetchall()

        return result

    def add_train(
        self, train_type: TrainType, name: str, num: int, producer: str, comment: str
    ) -> None:
        """
        add a new trains

        :param train_type: type of the train
        :param name: name of the train
        :param num: number of the train
        :param producer: producer of the train
        :param comment: comment to the train
        :return: None
        """

        query = f"""INSERT INTO {train_type.name} (name, number, producer, comment)
        VALUES (?, ?, ?, ?)"""

        self.cursor.execute(query, (name, num, producer, comment))
        self.conn.commit()
