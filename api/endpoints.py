import json
from typing import Dict

from flask import Blueprint, request

from .helper_functions import *
from . import logger

routes = Blueprint("routes", __name__)


@routes.route("/headline", methods=["GET"])
def get_headline():
    """Headline endpoint"""
    try:
        data: Dict = json.loads(request.data)
        category = data["category"]

        if supported_category(category):
            site, url = get_site_name_and_url(category)
            scraper_obj = get_object(site)
            scraper_obj.follow(url)
            headline: Dict = scraper_obj.get_headline()
            return json.dumps({"message": f"success", "data": headline}), 200

        return json.dumps({"message": f"category {category} is not supported", "error_id": "unsupported_category"}), 501

    # invalid json format
    except json.JSONDecodeError:
        return json.dumps({"message": "Invalid json format", "error_id": "invalid_json_format"}), 400

    # key is missing
    except KeyError as key:
        return json.dumps({"message": f"{key} value is missing", "error_id": "missing_value"}), 422

    # Internal server error
    except Exception as err:
        logger.error(err)
        return json.dumps({"message": "Internal server error", "error_id": "internal_server_id"}), 500


@routes.route("/market-stats", methods=["GET"])
def market_stats():
    """Market stats endpoint"""
    try:
        data: Dict = json.loads(request.data)
        exchange: str = data["exchange"].lower()

        if exchange not in ["nse", "bse"]:
            return json.dumps({"message": f"exchange {exchange} is not supported", "error_id": "unsupported_exchange"}), 501

        # scrape market stats
        money_control: MoneyControl  = MoneyControl(host="moneycontrol.com")
        stats = money_control.stock_market_stats(exchange)
        return json.dumps({"message": "success", "data": stats}), 200

    # invalid json format
    except json.JSONDecodeError:
        return json.dumps({"message": "Invalid json format", "error_id": "invalid_json_format"}), 400

    # key is missing
    except KeyError as key:
        return json.dumps({"message": f"{key} value is missing", "error_id": "missing_value"}), 422

    except Exception as err:
        logger.error(err)
        return json.dumps({"message": "Internal server error", "error_id": "internal_server_error"}), 500


@routes.route("/all-category", methods=["GET"])
def all_category():
    """All category endpoint, returns list of all categories"""
    return json.dumps({"message": "success", "categories": list(supported_categories)}), 200
