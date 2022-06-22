from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from flask_jwt_extended.jwt_manager import JWTManager

import sqlite3

from properties import JWT_SECRET

from dao.UserDAO import UserDAO
from dao.PostDAO import PostDAO
from dao.CommentDAO import CommentDAO

from services.AuthService import AuthService
from services.PostService import PostService
from services.CommentService import CommentService

from routes.PostRoute import PostRoute, PostIDRoute
from routes.CommentRoute import CommentIDRoute, CommentRoute

if __name__ == "__main__":
    
    database_connection_string = "database/data.db"

    app = Flask(__name__)
    api = Api(app)
   
    db_connection = sqlite3.connect(database_connection_string, check_same_thread = False)

    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.secret_key = JWT_SECRET

    user_dao = UserDAO(db_connection)
    post_dao = PostDAO(db_connection)
    comment_dao = CommentDAO(db_connection)
    
    post_service = PostService(post_dao)
    auth_service = AuthService(user_dao)
    comment_service = CommentService(comment_dao)

    jwt = JWT(app, auth_service.authenticate, auth_service.identity)

    api.add_resource(PostRoute, "/posts", resource_class_args = (post_service, ))
    api.add_resource(PostIDRoute, "/posts/<int:id>", resource_class_args = (post_service, ))
    api.add_resource(CommentRoute, "/posts/<int:post_id>/comments", resource_class_args = (comment_service, ))
    api.add_resource(CommentIDRoute, "/posts/<int:post_id>/comments/<int:comment_id>", resource_class_args = (comment_service, ))

    app.run(port = 8011)

    db_connection.commit()
    db_connection.close()