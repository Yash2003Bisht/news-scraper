import random
from typing import List, Tuple

from scraper import *


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


def get_site_name_and_url(category: str) -> List[Tuple]:
    """Returns the site name and the url structure for the category

    Args:
        category (str): category name

    Returns:
        List[Tuple]: List of tuple, each tuple contains two things site name and  url structure
    """
    return random.choice(categories.get(category))


def get_object(site: str):
    """Returns a site object for scraping news

    Args:
        site (str): name of the site
    """
    match site:
        case "mint":
            return Mint()
        case "ndtv":
            return NDTV()
        # case "business-today":
        #     return BusinessToday()
        case _:
            return MoneyControl()
