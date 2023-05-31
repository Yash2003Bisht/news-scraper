# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LIST OF ALL SUPPORTED CATEGORY @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

categories = {

    # ---------------- Business, Investing & Stock Market ----------------
    "business": [("money-control", "news/business/")],
    "companies": [("money-control", "news/tags/companies.html"), ("mint", "companies")],
    "mutual-funds": [("money-control", "news/business/mutual-funds"), ("mint", "mutual-fund")],
    "startups": [("money-control", "news/business/startups/")],
    "market": [("money-control", "news/business/markets/"), ("mint", "market")],
    "stocks": [("money-control", "news/business/stocks/")],
    "ipo": [("money-control", "news/business/ipo/")],
    "technical-analysis": [("money-control", "news/tags/technical-analysis.html")],
    "commodity": [("money-control", "news/business/commodity/")],
    "fixed-deposite": [("money-control", "news/tags/company-fixed-deposits.html")],
    "currency": [("money-control", "news/tags/currency.html")],
    "money": [("mint", "money")],
    "industry": [("mint", "industry")],

    # ------------------------------ Technology -----------------------------
    "tech": [("money-control", "news/technology/"), ("mint", "technology")],

    # ------------------------------ General News ----------------------------
    "latest-news": [("money-control", "news/news-all/"), ("mint", "latest-news")],
    "news": [("money-control", "news/news-all/"), ("mint", "news")],
    "india": [("money-control", "news/india/")],
    "world": [("money-control", "news/world/")],

    # -------------------- Entertainment, Lifestyle & Health -----------------
    "entertainment": [("money-control", "news/trends/entertainment/")],
    "lifestyle": [("money-control", "news/trends/lifestyle/")],
    "health": [("money-control", "news/health-and-fitness/")],
    "trends": [("money-control", "news/trends/")],
    "photos": [("money-control", "news/photos/")],
    "travel": [("money-control", "news/trends/travel/")],

    # ------------------------------ Others ---------------------------------
    "infographic": [("money-control", "news/infographic/")],
    "books": [("money-control", "news/tags/books.html")],
    "politics": [("money-control", "news/politics/")],
    "science": [("money-control", "news/tags/science.html")],
    "education": [("money-control", "news/tags/education.html")],
    "premium": [("mint", "premium")],
    "opinion": [("mint", "opinion")]
}
sites = ["money-control", "mint"]
supported_categories = categories.keys()
