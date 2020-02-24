from flask import Flask

app = Flask(__name__)

from .api.routes import router_blueprint
app.register_blueprint(router_blueprint)