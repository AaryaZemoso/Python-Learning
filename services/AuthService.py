from dao.UserDAO import UserDAO

class AuthService:
    
    def __init__(self, user_dao: UserDAO) -> None:
        self.user_dao = user_dao

    def authenticate(self, username, password):
        user = self.user_dao.user_exists(username, password)
        if user:
            return user

    def identity(self, payload):
        user_id = payload["identity"]
        return self.user_dao.get_by_id(user_id)