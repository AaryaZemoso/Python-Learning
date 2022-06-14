from typing import List
from models.Comment import Comment


class Post:

    def __init__(self, _id: int, title: str, content: str, comments: List[Comment]) -> None:
        self._id = _id
        self.title = title
        self.content = content
        self.comments = comments

    def __repr__(self) -> str:
        return f"<Post id={self._id}>"

    def __str__(self) -> str:
        return f"Post[id = {self._id}, title = {self.title}, content = {self.content}]"
