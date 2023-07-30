import logging
import os
import json
from typing import List, Tuple, Any

from scraper import *
from . import HEADLINE_DATA_FILE


def supported_category(category: str) -> bool:
    """Checks if the category is supported or not

    Args:
        category (str): category name to check

    Returns:
        bool: True if category is supported, False otherwise
    """
    if category in categories:
        return True
    return False


def get_all_site_name_and_url(category: str) -> List[Tuple]:
    """Returns the list of site name and the url structure for the category

    Args:
        category (str): category name

    Returns:
        List[Tuple]: List of tuple, each tuple contains two things site name and  url structure
    """
    return categories.get(category)


def get_object(site: str) -> Any:
    """Returns a site object for scraping news

    Args:
        site (str): name of the site

    Returns:
        Any: News scraper object
    """
    match site:
        case "mint":
            return Mint()
        case "ndtv":
            return NDTV()
        case "hindustantimes":
            return HindustanTimes()
        # case "business-today":
        #     return BusinessToday()
        case _:
            return MoneyControl()


def repeated_headline(site: str, headline_title: str) -> bool:
    """Checks if a headline is repeated

    Args:
        site (str): Site name
        headline_title (str): Headline title

    Returns:
        bool: Returns True if a headline is repeated otherwise False
    """

    if os.path.exists(HEADLINE_DATA_FILE):
        with open(HEADLINE_DATA_FILE) as headlines:
            try:
                headlines = json.load(headlines)
                return headlines.get(site) == headline_title
            # Catch JSONDecodeError, it can be raised if the file is empty
            except json.JSONDecodeError:
                pass
    return False


def add_headline(site: str, headline_title: str) -> None:
    """Adds a headline to headline_data.json

    Args:
        site (str): Site name
        headline_title (str): Headline title
    """

    # Check if the file exists
    if not os.path.exists(HEADLINE_DATA_FILE):
        # Create a file if it doesn't already exist
        os.system(f"touch {HEADLINE_DATA_FILE}")

    with open(HEADLINE_DATA_FILE) as headline_fp_read:
        try:
            headlines = json.load(headline_fp_read)
        # Catch JSONDecodeError, it can be raised if the file is empty
        except json.JSONDecodeError:
            headlines = {}

    # Check if this headline is already in the headline_data.json file.
    # This should never happen since we have already checked this condition on the "repeated_headline" function
    if headlines.get(site) != headline_title:
        headlines[site] = headline_title

        with open(HEADLINE_DATA_FILE, "w") as headline_fp_write:
            json.dump(headlines, headline_fp_write, indent=4)

    # Log this event on sentry
    else:
        logging.critical("Something went wrong with repeated_headline function. Its pass a repeated headline")
