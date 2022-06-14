import sqlite3
from dao.CommentDAO import CommentDAO
from dao.PostDAO import PostDAO
from models.Comment import Comment
from models.Post import Post

from models.User import User
from dao.UserDAO import UserDAO

database_connection_string = "database/data.db"

connection = sqlite3.connect(database_connection_string)

# user_dao = UserDAO(connection)
comment_dao = CommentDAO(connection)
post_dao = PostDAO(connection, comment_dao)
# user_dao.reset_table()
# user_dao.create(User(1, "Aarya", "Devarla"))
# user_dao.update(User(2, "Luffy", "Meat"))
# for user in user_dao.get_all():
    # print(user)
# user_dao.delete(1)
# print(user_dao.get_by_id(1))

# post_dao.reset_table()
# post_dao.create(Post(2, "Second post", "Already Bored", None))
for post in post_dao.get_all():
    print(post)
    print("Comments : ", post.comments)

# comment_dao.reset_table()
# comment_dao.create(1, Comment(1, "Whoa!!! Nice"))
# for comment in comment_dao.get_by_post_id(1):
    # print(comment)

connection.commit()
connection.close()

