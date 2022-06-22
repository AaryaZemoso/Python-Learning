class Post:

    def __init__(self, _id: int, title: str, content: str) -> None:
        self.id = _id
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"<Post id={self.id}>"

    def __str__(self) -> str:
        return f"Post[id = {self.id}, title = {self.title}, content = {self.content}]"
    
    def json(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content
        }
