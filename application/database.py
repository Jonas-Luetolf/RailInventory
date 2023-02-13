import sqlite3

class DataBase:
    """
    used to write to and read from a local DataBase
    """
    def __init__(self, file:str) -> None:
        """
        connets to file and creates cursor
        
        :param file: filename of the sqlite database 
        :return: None
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

    def _create_table(self):
        """
        creates new tabel if one doesn't exists
        
        :return: None
        """
        
        query = f"""CREATE TABLE IF NOT EXISTS trains 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, number INTEGER, producer TEXT, comment TEXT)"""
        
        self.cursor.execute(query)
        self.conn.commit()

    def get_train_by_name(self, name:str):
        """
        gets the train by name
        
        :param name: name of the train to search for
        :return: the data of the searched train
        """
        
        raise NotImplemented

    def add_train(self, name:str, num:int, producer:str, comment:str) -> None:
        """
        add a new trains
        
        :param name: name of the train
        :param num: number of the train
        :param producer: producer of the train
        :param comment: comment to the train
        :return: None
        """
        
        query = f"""INSERT INTO trains (name, number, producer, comment)
        VALUES ({name}, {num}, {producer}, {comment})"""

        self.cursor.execute(query)
        self.conn.commit()
