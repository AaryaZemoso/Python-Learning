class User:
    
    def __init__(self, _id, name, password) -> None:
        self.id = _id
        self.name = name
        self.password = password

    def __str__(self) -> str:
        return f"User[id={self.id}, name={self.name}, password={self.password}]"

    def __repr__(self) -> str:
        return f"<User id={self.id}>"