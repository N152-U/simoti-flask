from flask import Flask
from flask_cors import CORS, cross_origin

from config import config

# Routes
from routes import PermissionRouter, RoleRouter

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost:8843"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == "__main__":
    app.config.from_object(config["development"])

    # Blueprints
    app.register_blueprint(PermissionRouter.main, url_prefix="/api/v1/permissions")
    app.register_blueprint(RoleRouter.main, url_prefix="/api/v1/roles")

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
