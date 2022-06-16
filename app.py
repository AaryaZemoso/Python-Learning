from flask import Flask
from flask_restful import Api

import sqlite3

from dao.CommentDAO import CommentDAO
from dao.PostDAO import PostDAO
from dao.UserDAO import UserDAO
from routes.CommentRoute import CommentIDRoute, CommentRoute

from services.CommentService import CommentService
from services.PostService import PostService

from routes.PostRoute import PostRoute, PostIDRoute

if __name__ == "__main__":
    
    database_connection_string = "database/data.db"

    connection = sqlite3.connect(database_connection_string, check_same_thread = False)
    app = Flask(__name__)
    api = Api(app)

    user_dao = UserDAO(connection)
    comment_dao = CommentDAO(connection)
    post_dao = PostDAO(connection)
    
    comment_service = CommentService(comment_dao)
    post_service = PostService(post_dao)

    api.add_resource(PostRoute, "/posts", resource_class_args = (post_service, ))
    api.add_resource(PostIDRoute, "/posts/<int:id>", resource_class_args = (post_service, ))
    api.add_resource(CommentRoute, "/posts/<int:post_id>/comments", resource_class_args = (comment_service, ))
    api.add_resource(CommentIDRoute, "/posts/<int:post_id>/comments/<int:comment_id>", resource_class_args = (comment_service, ))

    app.run(port = 8011)

    connection.commit()
    connection.close()