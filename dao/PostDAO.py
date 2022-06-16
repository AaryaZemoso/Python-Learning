from sqlite3 import Connection
from typing import List

from models.Post import Post

class PostDAO:

    CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS posts (id int PRIMARY KEY, title text, content text)"
    DROP_TABLE_QUERY = "DROP TABLE IF EXISTS posts"

    CREATE_QUERY = "INSERT INTO posts VALUES (?, ?, ?)"
    UPDATE_QUERY = "UPDATE posts SET title = ?, content = ? WHERE id = ?"
    DELETE_QUERY = "DELETE FROM posts WHERE id = ?"
    GET_BY_ID_QUERY = "SELECT * FROM posts WHERE id = ?"
    GET_ALL_QUERY = "SELECT * FROM posts"

    def __init__(self, connection: Connection) -> None:
        
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.execute(self.CREATE_TABLE_QUERY)


    def create(self, post: Post):
        self.cursor.execute(self.CREATE_QUERY, (
            post.id,
            post.title,
            post.content
        ))

    def update(self, post: Post):
        self.cursor.execute(self.UPDATE_QUERY, (
            post.title,
            post.content, 
            post.id
        ))
    
    def delete(self, id: int):
        self.cursor.execute(self.DELETE_QUERY, (id, ))

    def get_by_id(self, id: int) -> Post:
        return Post(*next(self.cursor.execute(self.GET_BY_ID_QUERY, (id, ))))

    def get_all(self) -> List[Post]:
        list_of_posts = self.cursor.execute(self.GET_ALL_QUERY)
        return [Post(*post) for post in list_of_posts]

    def reset_table(self):
        self.cursor.execute(self.DROP_TABLE_QUERY)
        self.cursor.execute(self.CREATE_TABLE_QUERY)

