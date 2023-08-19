import os
import logging
from os.path import join, dirname

import sentry_sdk
from flask import Flask, json
from sentry_sdk.integrations.flask import FlaskIntegration
from dotenv import load_dotenv


# ------------- load env -------------
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
# -----------------------------------------


# ------------- sentry integration -------------
if os.environ.get("PRODUCTION", "false") != "false":
    sentry_sdk.init(
        dsn=os.environ["DSN"],
        integrations=[
            FlaskIntegration(),
        ],
        traces_sample_rate=1.0,
        release="news-scraper@v1.8.7"
    )
# -----------------------------------------


# ------------- logger config -------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("[%(levelname)s] - %(asctime)s - %(name)s - %(message)s")

ch.setFormatter(formatter)

logger.addHandler(ch)
# -----------------------------------------


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADLINE_DATA_FILE = os.path.join(BASE_DIR, "headlines_data.json")

app = Flask(__name__)


def configure_app():
    from .endpoints import routes

    # add a secret key
    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

    # register blueprint
    app.register_blueprint(routes, url_prefix="/")

    # default route
    @app.route("/", methods=["GET"])
    def index():
        return json.dumps({"message": "Welcome"}), 200

    return app

