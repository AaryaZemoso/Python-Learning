from random import randint
from typing import List, Union
from dao.CommentDAO import CommentDAO
from models.Comment import Comment

class CommentService:
    
    def __init__(self, comment_dao: CommentDAO) -> None:
        self.comment_dao = comment_dao

    def create(self, post_id: int, comment: Comment) -> bool:
        try:
            comment.id = randint(0, 1000000)
            self.comment_dao.create(post_id, comment)
            return True
        except Exception:
            print("Error in CommentService : Create")
            return False

    def update(self, post_id: int, comment: Comment) -> bool:
        try:
            self.comment_dao.update(post_id, comment)
            return True
        except Exception as e:
            print(e)
            print("Error in CommentService : Update")
            return False

    def delete(self, post_id: int, comment_id: int) -> bool:
        try:
            self.comment_dao.delete(post_id, comment_id)
            return True
        except Exception:
            print("Error in CommentService : Delete")
            return False

    def get_by_id(self, post_id: int, comment_id: int) -> Union[Comment, None]:
        try:
            return self.comment_dao.get_by_post_id_and_comment_id(post_id, comment_id)
        except Exception as e:
            print(e)
            print("Error in CommentService : Get by ID")
            return None

    def get_all(self, post_id: int) -> Union[List[Comment], None]:
        try:
            return self.comment_dao.get_by_post_id(post_id)
        except Exception:
            print("Error in CommentService : Get All")
            return None