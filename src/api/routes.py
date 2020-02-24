from flask import Blueprint
from flask_restful import Api

router_blueprint = Blueprint('router', __name__)
api = Api(router_blueprint)


from .components import Default

api.add_resource(Default,'/')