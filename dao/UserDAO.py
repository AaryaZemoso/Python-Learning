import sqlite3
from typing import List

from models.User import User

class UserDAO:
    
    CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY, name text, password text)"
    DROP_TABLE_QUERY = "DROP TABLE IF EXISTS users"

    CREATE_QUERY = "INSERT INTO users VALUES (?, ?, ?)"
    UPDATE_QUERY = "UPDATE users SET name = ?, password = ? WHERE id = ?"
    DELETE_QUERY = "DELETE FROM users WHERE id = ?"
    GET_BY_ID_QUERY = "SELECT * FROM users WHERE id = ?"
    GET_ALL_QUERY = "SELECT * FROM users"

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection
        self.cursor = connection.cursor()

    def create(self, user: User) -> None:
        self.cursor.execute(self.CREATE_QUERY, (user.id, user.name, user.password))

    def update(self, user: User):
        self.cursor.execute(self.UPDATE_QUERY, (user.name, user.password, user.id))

    def delete(self, _id: int): 
        self.cursor.execute(self.DELETE_QUERY, (_id, ))

    def get_all(self) -> List[User]:
        list_of_users = self.cursor.execute(self.GET_ALL_QUERY)
        return [User(*user) for user in list_of_users]

    def get_by_id(self, _id) -> User:
        try:
            user = next(self.cursor.execute(self.GET_BY_ID_QUERY, (_id, )))
            return User(*user)
        except StopIteration:
            return None

    def reset_table(self): 
        self.cursor.execute(self.DROP_TABLE_QUERY)
        self.cursor.execute(self.CREATE_TABLE_QUERY)