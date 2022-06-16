from flask import jsonify, make_response, request
from flask_restful import Resource
from models.Comment import Comment

from services.CommentService import CommentService


class CommentIDRoute(Resource):

    def __init__(self, service: CommentService) -> None:
        super().__init__()
        self.service = service

    def get(self, post_id: int, comment_id: int):
        return jsonify(self.service.get_by_id(post_id, comment_id).json())

    def put(self, post_id: int, comment_id: int):
        data = request.get_json()
        try:
            if self.service.update(post_id, Comment(comment_id, data["content"])):
                return jsonify({
                    'message': 'updated comment'
                })
            else:
                return make_response(jsonify({
                    'message': 'internal server error'
                }), 500)
        except Exception:
            return make_response(jsonify({
                'message': 'bad request'
            }), 400)

    def delete(self, post_id: int, comment_id: int):
        if self.service.delete(post_id, comment_id):
            return jsonify({
                'message': 'deleted comment'
            })
        else:
            return make_response(jsonify({
                'message': 'internal server error'
            }), 500)

class CommentRoute(Resource):
    
    def __init__(self, service: CommentService) -> None:
        super().__init__()
        self.service = service

    def post(self, post_id: int):
        data = request.get_json()
        try:
            comment = Comment(0, data["content"])
            if not self.service.create(post_id, comment):
                return make_response(jsonify({
                    "message": "internal server error"
                }), 500)
            else:
                return make_response(jsonify({
                    "message": "created new comment"
                }), 201)
        except Exception:
            return make_response(jsonify({
                "message": "error parsing the body"
            }), 400)

    def get(self, post_id: int):
        list_of_comments = self.service.get_all(post_id)
        if list_of_comments:
            return jsonify([comment.json() for comment in list_of_comments])
        else: 
            return jsonify([])