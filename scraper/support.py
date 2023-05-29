# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LIST OF ALL SUPPORTED CATEGORY @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

sites = ("money-control", "mint")
supported_categories = ("business", "mutual-funds", "ipo", "startups", "market",
                        "premium", "money", "industry", "companies", "tech", "opinion")
categories = {
    "business": [("money-control", "news/business/")],
    "companies": [("money-control", "news/tags/companies.html"), ("mint", "companies")],
    "mutual-funds": [("money-control", "news/business/mutual-funds"), ("mint", "mutual-fund")],
    "ipo": [("money-control", "news/business/ipo/")],
    "startups": [("money-control", "news/business/startups/")],
    "market": [("mint", "market")],
    "premium": [("mint", "premium")],
    "money": [("mint", "money")],
    "industry": [("mint", "industry")],
    "tech": [("mint", "technology")],
    "opinion": [("mint", "opinion")]
}
