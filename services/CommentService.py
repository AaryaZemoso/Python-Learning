from ctypes import Union
from random import randint
from types import NoneType
from typing import List
from dao.CommentDAO import CommentDAO
from models.Comment import Comment

class CommentService:
    
    def __init__(self, comment_dao: CommentDAO) -> None:
        self.comment_dao = comment_dao

    def create(self, comment: Comment) -> bool:
        try:
            comment.id = randint(0, 1000000)
            self.comment_dao.create(comment)
            return True
        except Exception:
            print("Error in PostService : Create")
            return False

    def update(self, comment: Comment) -> bool:
        try:
            self.comment_dao.update(comment)
            return True
        except Exception:
            print("Error in PostService : Update")
            return False

    def delete(self, id: int) -> bool:
        try:
            self.comment_dao.delete(id)
            return True
        except Exception:
            print("Error in PostService : Delete")
            return False

    def get_by_id(self, id: int) -> Union[Comment, NoneType]:
        try:
            return self.comment_dao.get_by_id(id)
        except Exception:
            print("Error in PostService : Get All")
            return None

    def get_all(self) -> Union[List[Comment], NoneType]:
        try:
            return self.comment_dao.get_all()
        except Exception:
            print("Error in PostService : Get All")
            return None