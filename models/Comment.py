class Comment:

    def __init__(self, _id: int, content: str) -> None:
        self.id = _id
        self.content = content

    def __repr__(self) -> str:
        return f"<Comment id={self.id}>"

    def __str__(self) -> str:
        return f"Comment[id = {self.id}, content = {self.content}]"