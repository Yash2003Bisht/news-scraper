import json
import random
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
            # get & randomly shuffle all sites and URLs for the category
            sites_and_urls = get_all_site_name_and_url(category)
            random.shuffle(sites_and_urls)

            # iterate through all sites and URLs, and return whichever works
            for site_url in sites_and_urls:
                site, url = site_url

                try:
                    scraper_obj = get_object(site)
                    scraper_obj.follow(url)
                    headline: Dict = scraper_obj.get_headline()
                    return json.dumps({"message": f"success", "data": headline}), 200

                # handle AttributeError and log a message
                except AttributeError:
                    logger.error(f"Attribute Error for {site}")

            # if all sites don't work, log events to Sentry
            logger.critical("Iterated through all sites but no one works")
            return json.dumps({"message": "Something went Wrong", "error_id": "unknown_error"}), 500

        return json.dumps({"message": f"category {category} is not supported", "error_id": "unsupported_category"}), 501

    # invalid json format
    except json.JSONDecodeError:
        return json.dumps({"message": "Invalid json format", "error_id": "invalid_json_format"}), 400

    # key is missing
    except KeyError as key:
        return json.dumps({"message": f"{key} value is missing", "error_id": "missing_value"}), 422

    # Internal server error
    except Exception as err:
        logger.critical(err)
        return json.dumps({"message": "Internal server error", "error_id": "internal_server_id"}), 500


@routes.route("/market-stats", methods=["GET"])
def market_stats():
    """Market stats endpoint"""
    try:
        data: Dict = json.loads(request.data)
        exchange: str = data["exchange"].lower()

        if exchange not in ["nse", "bse"]:
            return json.dumps({"message": f"exchange {exchange} is not supported",
                               "error_id": "unsupported_exchange"}), 501

        # scrape market stats
        money_control: MoneyControl = MoneyControl()
        stats = money_control.stock_market_stats(exchange)
        return json.dumps({"message": "success", "data": stats}), 200

    # invalid json format
    except json.JSONDecodeError:
        return json.dumps({"message": "Invalid json format", "error_id": "invalid_json_format"}), 400

    # key is missing
    except KeyError as key:
        return json.dumps({"message": f"{key} value is missing", "error_id": "missing_value"}), 422

    # Internal server error
    except Exception as err:
        logger.critical(err)
        return json.dumps({"message": "Internal server error", "error_id": "internal_server_error"}), 500


@routes.route("/markets", methods=["GET"])
def stock_market():
    """Most active stock endpoint"""
    try:
        market_type = request.args["market"]

        # Check if the market_type is supported
        if market_type not in market_types:
            return json.dumps({"message": f"request type '{market_type}' is not supported",
                               "error_id": "unsupported_request_type"}), 501

        # Create StocksMarket object
        stock_market_obj: StocksMarket = StocksMarket()

        match market_type:

            case "market-stats":
                stock_market_stats = stock_market_obj.market_stats()
                return json.dumps({"message": "success", "data": stock_market_stats}), 200

            case "most-active-stock":
                most_active_stock = stock_market_obj.most_active_stocks()
                return json.dumps({"message": "success", "data": most_active_stock}), 200

            case "mutual-funds":
                mutual_funds = stock_market_obj.market_mutual_funds()
                return json.dumps({"message": "success", "data": mutual_funds}), 200

            case "price-volume-shocker":
                price_volume_shocker = stock_market_obj.price_volume_shocker()
                return json.dumps({"message": "success", "data": price_volume_shocker}), 200

            case "market-indices":
                market_indices = stock_market_obj.market_indices()
                return json.dumps({"message": "success", "data": market_indices}), 200

        # This should never happen because we are checking market_type first
        return json.dumps({"message": "Internal server error"}), 500

    # key is missing
    except KeyError as key:
        return json.dumps({"message": f"'market' parameter is missing", "error_id": "missing_parameter"}), 422

    # Internal server error
    except Exception as err:
        logger.critical(err)
        return json.dumps({"message": "Internal server error", "error_id": "internal_server_error"}), 500


@routes.route("/all-category", methods=["GET"])
def all_category():
    """All category endpoint, returns list of all categories"""
    return json.dumps({"message": "success", "categories": list(supported_categories)}), 200


@routes.route("/market-types", methods=["GEt"])
def markets_tpes():
    """Returns list of all market types"""
    return json.dumps({"message": "success", "market-types": list(market_types)}), 200
