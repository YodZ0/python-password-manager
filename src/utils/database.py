import sqlite3

from typing import List, Dict, Union


class DBHandler:
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        try:
            return sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            print("[DB] - Connection error: ", e)
            raise

    def create_data_table(self) -> None:
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        source TEXT NOT NULL,
                        login TEXT NOT NULL,
                        password TEXT NOT NULL
                    )
                    """
                )
        except sqlite3.DatabaseError as e:
            print("[DB] - Tables creation error: ", e)

    def drop_data_table(self) -> None:
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("DROP TABLE IF EXISTS Data")
        except sqlite3.DatabaseError as e:
            print("[DB] - Drop table error: ", e)

    def insert_row(self, source: str, login: str, password: str) -> None:
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO Data (source, login, password) VALUES (?, ?, ?)",
                    (source, login, password),
                )
        except sqlite3.DatabaseError as e:
            print("[DB] - Insert row error: ", e)

    def select_all(self) -> List[Dict[str, Union[int, str]]]:
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Data")
                data = [
                    {
                        "id": row[0],
                        "source": row[1],
                        "login": row[2],
                        "password": row[3],
                    }
                    for row in cursor.fetchall()
                ]
                return data
        except sqlite3.DatabaseError as e:
            print("[DB] - Select all error: ", e)
            return []
