from sqlite3 import Connection
from typing import List, Union
from models.Comment import Comment

class CommentDAO:

    CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS comments (post_id int, comment_id int, content text, PRIMARY KEY(post_id, comment_id), FOREIGN KEY (post_id) REFERENCES posts(id))"
    DROP_TABLE_QUERY = "DROP TABLE IF EXISTS comments"

    CREATE_QUERY = "INSERT INTO comments VALUES ( ?, ?, ? )"
    UPDATE_QUERY = "UPDATE comments SET content = ? WHERE post_id = ? AND comment_id = ?"
    DELETE_QUERY = "DELETE FROM comments WHERE post_id = ? AND comment_id = ?"
    GET_BY_POST_ID_QUERY = "SELECT * FROM comments WHERE post_id = ?"
    GET_BY_POST_ID_AND_COMMENT_ID_QUERY = "SELECT * FROM comments WHERE post_id = ? AND comment_id = ?"

    def __init__(self, connection: Connection) -> None:
       
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.execute(self.CREATE_TABLE_QUERY)


    def create(self, post_id: int, comment: Comment):
        self.cursor.execute(
            self.CREATE_QUERY, 
            (
                post_id, 
                comment.id, 
                comment.content
            )
        )

    def update(self, post_id: int, comment: Comment):
        self.cursor.execute(
            self.UPDATE_QUERY, 
            (
                comment.content, 
                post_id, 
                comment.id
            )
        )
    
    def delete(self, post_id: int, cursor_id: int):
        self.cursor.execute(
            self.DELETE_QUERY, 
            (
                post_id, 
                cursor_id
            )
        )

    def get_by_post_id(self, post_id: int) -> List[Comment]:
        list_of_comments = self.cursor.execute(self.GET_BY_POST_ID_QUERY, (post_id, ))
        return [Comment(comment[1], comment[2]) for comment in list_of_comments]

    def get_by_post_id_and_comment_id(self, post_id: int, comment_id: int) -> Union[Comment, None]:
        try:
            comment = next(self.cursor.execute(self.GET_BY_POST_ID_AND_COMMENT_ID_QUERY, (post_id, comment_id)))
            return Comment(comment[1], comment[2])
        except StopIteration:
            return None

    def reset_table(self):
        self.cursor.execute(self.DROP_TABLE_QUERY)
        self.cursor.execute(self.CREATE_TABLE_QUERY)