from flask_restful import Resource
from flask import jsonify, request, make_response
from models.Post import Post

from services.PostService import PostService


class PostIDRoute(Resource):

    def __init__(self, service: PostService) -> None:
        super().__init__()
        self.service = service

    def get(self, id: int):
        return jsonify(self.service.get_by_id(id).json())

    def put(self, id: int):
        data = request.get_json()
        try:
            if self.service.update(Post(id, data["title"], data["content"])):
                return jsonify({
                    'message': 'updated post'
                })
            else:
                return make_response(jsonify({
                    'message': 'internal server error'
                }), 500)
        except Exception:
            return make_response(jsonify({
                'message': 'bad request'
            }), 400)

    def delete(self, id: int):
        if self.service.delete(id):
            return jsonify({
                'message': 'deleted post'
            })
        else:
            return make_response(jsonify({
                'message': 'internal server error'
            }), 500)


class PostRoute(Resource):
    
    def __init__(self, service: PostService) -> None:
        super().__init__()
        self.service = service

    def post(self):
        data = request.get_json()
        try:
            post = Post(0, data["title"], data["content"])
            if not self.service.create(post):
                return make_response(jsonify({
                    "message": "internal server error"
                }), 500)
            else:
                return make_response(jsonify({
                    "message": "created new post"
                }), 201)
        except Exception:
            return make_response(jsonify({
                "message": "error parsing the body"
            }), 400)
        
    def get(self):
        list_of_posts = self.service.get_all()
        if list_of_posts:
            return jsonify([post.json() for post in list_of_posts])
        else: 
            return jsonify([])