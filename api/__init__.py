from flask import Flask, json

app = Flask(__name__)

def configure_app():
    from .endpoints import routes

    # add a secret key
    app.config["SECRET_KEY"] = "5fsyuadigohkfg\g54d1fsggrteG45wtref4ad567f89gohp["

    # register blueprint
    app.register_blueprint(routes, url_prefix="/")

    # default route
    @app.route("/", methods=["GET"])
    def index():
        return json.dumps({"message": "Welcome"}), 200

    return app

