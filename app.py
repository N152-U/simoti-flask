from flask import Flask
from flask_cors import CORS, cross_origin

from config import config

# Routes
from routes import PermissionRouter, RoleRouter, UserRouter, MeasurementRouter, CatalogRouter

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "*"}})


def page_not_found(error):
    return "<h1>Bienvenido a la API de SIMOTI</h1>", 404


if __name__ == "app":
    app.config.from_object(config["production"])

    # Blueprints
    app.register_blueprint(PermissionRouter.main, url_prefix="/simoti/api/v1/permissions")
    app.register_blueprint(RoleRouter.main, url_prefix="/simoti/api/v1/roles")
    app.register_blueprint(UserRouter.main, url_prefix="/simoti/api/v1/users")
    app.register_blueprint(MeasurementRouter.main, url_prefix="/simoti/api/v1/measurements")
    app.register_blueprint(CatalogRouter.main, url_prefix="/simoti/api/v1/catalog")

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(port=5001)
elif __name__ == "__main__":
    app.config.from_object(config["production"])

    # Blueprints
    app.register_blueprint(PermissionRouter.main, url_prefix="/simoti/api/v1/permissions")
    app.register_blueprint(RoleRouter.main, url_prefix="/simoti/api/v1/roles")
    app.register_blueprint(UserRouter.main, url_prefix="/simoti/api/v1/users")
    app.register_blueprint(MeasurementRouter.main, url_prefix="/simoti/api/v1/measurements")
    app.register_blueprint(CatalogRouter.main, url_prefix="/simoti/api/v1/catalog")

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(port=5002)
