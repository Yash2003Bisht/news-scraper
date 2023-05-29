import random

from scraper import *


def supported_category(category: str):
    if category in categories:
        return True
    return False


def get_site_name_and_url(category: str):
    return random.choice(categories.get(category))


def get_object(site: str, url: str):
    if site == "mint":
        return Mint(host="livemint.com", url_structure=url)
    else:
        return MoneyControl(host="moneycontrol.com", url_structure=url)

