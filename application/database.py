import sqlite3

class DataBase:
    """
    used to write to and read from a local DataBase
    """
    def __init__(self, file:str) -> None:
        """
        connets to file and creates cursor
        """
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()
        
        self._create_table()

    def close(self) -> None:
        """
        close the db connection
        """
        self.conn.close()

    def _create_table(self):
        """
        creates new tabel if one doesn't exists
        """
        query = f"""CREATE TABLE IF NOT EXISTS trains 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, number INTEGER, producer TEXT, comment TEXT)"""
        
        self.cursor.execute(query)
        self.conn.commit()

    def get_train_by_name(self, name:str):
        """
        gets the train by name
        """
        raise NotImplemented

    def add_train(self, name:str, num:int, producer:str, comment:str) -> None:
        """
        add a new trains
        """
        raise NotImplemented
