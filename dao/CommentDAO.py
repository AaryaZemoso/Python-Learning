from sqlite3 import Connection
from models.Comment import *

class CommentDAO:

    CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS comments (post_id int, comment_id int, context text, PRIMARY KEY(post_id, comment_id), FOREIGN KEY (post_id) REFERENCES posts(id))"
    DROP_TABLE_QUERY = "DROP TABLE IF EXISTS comments"

    CREATE_QUERY = "INSERT INTO comments VALUES ( ?, ?, ? )"
    UPDATE_QUERY = ""
    DELETE_QUERY = ""
    GET_BY_POST_ID_QUERY = "SELECT * FROM comments WHERE post_id = ?"
    GET_BY_POST_ID_AND_COMMENT_ID_QUERY = "SELECT * FROM comments WHERE post_id = ? AND comment_id = ?"

    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        self.cursor = connection.cursor()

    def create(self, post_id: int, comment: Comment):
        self.cursor.execute(self.CREATE_QUERY, (post_id, comment.id, comment.content))

    def update(self):
        pass
    
    def delete(self):
        pass

    def get_by_post_id(self, post_id: int):
        list_of_comments = self.cursor.execute(self.GET_BY_POST_ID_QUERY, (post_id, ))
        return [Comment(comment[1], comment[2]) for comment in list_of_comments]

    def get_by_post_id_and_comment_id(self, post_id: int, comment_id: int):
        try:
            comment = next(self.cursor.execute(self.GET_BY_ID_QUERY, (post_id, comment_id)))
            return Comment(comment.comment_id, comment.name)
        except StopIteration:
            return None

    def reset_table(self):
        self.cursor.execute(self.DROP_TABLE_QUERY)
        self.cursor.execute(self.CREATE_TABLE_QUERY)