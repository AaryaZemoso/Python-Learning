from random import randint
from typing import List, Union
from dao.PostDAO import PostDAO
from models.Post import Post

class PostService:
    
    def __init__(self, post_dao: PostDAO) -> None:
        self.post_dao = post_dao

    def create(self, post: Post) -> bool:
        try:
            post.id = randint(0, 1000000)
            self.post_dao.create(post)
            return True
        except Exception:
            print("Error in PostService : Create")
            return False

    def update(self, post: Post) -> bool:
        try:
            self.post_dao.update(post)
            return True
        except Exception:
            print("Error in PostService : Update")
            return False

    def delete(self, id: int) -> bool:
        try:
            self.post_dao.delete(id)
            return True
        except Exception:
            print("Error in PostService : Delete")
            return False

    def get_by_id(self, id: int) -> Union[Post, None]:
        try:
            return self.post_dao.get_by_id(id)
        except Exception:
            print("Error in PostService : Get All")
            return None

    def get_all(self) -> Union[List[Post], None]:
        try:
            return self.post_dao.get_all()
        except Exception as e:
            print(e)
            print("Error in PostService : Get All")
            return None