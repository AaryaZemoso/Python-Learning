from sqlite3 import Connection
from typing import List
from dao.CommentDAO import CommentDAO

from models.Post import Post

class PostDAO:

    CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS posts (id int PRIMARY KEY, title text, content text)"
    DROP_TABLE_QUERY = "DROP TABLE IF EXISTS posts"

    CREATE_QUERY = "INSERT INTO posts VALUES (?, ?, ?)"
    UPDATE_QUERY = ""
    DELETE_QUERY = ""
    GET_BY_ID_QUERY = ""
    GET_ALL_QUERY = "SELECT * FROM posts"

    def __init__(self, connection: Connection, comment_dao: CommentDAO = None) -> None:
        
        self.connection = connection
        self.cursor = connection.cursor()

        self.comment_dao = CommentDAO(connection) if comment_dao is None else comment_dao

    def create(self, post: Post):
        self.cursor.execute(self.CREATE_QUERY, (
            post._id,
            post.title,
            post.content
        ))

    def update(self):
        pass
    
    def delete(self):
        pass

    def get_by_id(self):
        pass

    def get_all(self) -> List[Post]:
        list_of_posts = self.cursor.execute(self.GET_ALL_QUERY)
        return [Post(*post, self.comment_dao.get_by_post_id(post[0])) for post in list_of_posts]

    def reset_table(self):
        self.cursor.execute(self.DROP_TABLE_QUERY)
        self.cursor.execute(self.CREATE_TABLE_QUERY)

