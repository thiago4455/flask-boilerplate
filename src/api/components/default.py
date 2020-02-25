from flask_restful import Resource

from src.api.utils.db_connection import connect

class Default(Resource):
    def get(self):
        print(connect('SELECT * from users'))
        return '/'