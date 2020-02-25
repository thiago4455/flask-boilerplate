from flask_restful import Resource

class Default(Resource):
    def get(self):
        return '/'