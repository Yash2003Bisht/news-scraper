from flask import Flask, json
import logging

app = Flask(__name__)

# ------------- logger config -------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("[%(levelname)s] - %(asctime)s - %(name)s - %(message)s")

ch.setFormatter(formatter)

logger.addHandler(ch)
# -----------------------------------------


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

