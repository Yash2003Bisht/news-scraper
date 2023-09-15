# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LIST OF ALL SUPPORTED THINGS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# ---------------------------------------------- CATEGORIES ----------------------------------------------
categories = {

    # ---------------- Business, Investing & Stock Market ----------------
    "business": [("MoneyControl", "news/business/")],
    "companies": [("MoneyControl", "news/tags/companies.html"), ("Mint", "companies"),
                  ("BusinessStandard", "companies")],
    "mutual-funds": [("MoneyControl", "news/business/mutual-funds"), ("Mint", "mutual-fund")],
    "startups": [("MoneyControl", "news/business/startups/")],
    "market": [("MoneyControl", "news/business/markets/"), ("Mint", "market"), ("BusinessStandard", "markets")],
    "stocks": [("MoneyControl", "news/business/stocks/")],
    "ipo": [("MoneyControl", "news/business/ipo/")],
    "technical-analysis": [("MoneyControl", "news/tags/technical-analysis.html")],
    "commodity": [("MoneyControl", "news/business/commodity/")],
    "fixed-deposite": [("MoneyControl", "news/tags/company-fixed-deposits.html")],
    "currency": [("MoneyControl", "news/tags/currency.html")],
    "money": [("Mint", "money")],
    "industry": [("Mint", "industry"), ("BusinessStandard", "industry")],
    "management": [("BusinessStandard", "management")],

    # ------------------------------ Technology -----------------------------
    "tech": [("MoneyControl", "news/technology/"), ("Mint", "technology"), ("TheHindu", "sci-tech/"),
             ("TheHindu", "sci-tech/technology/"), ("TheHindu", "sci-tech/technology/gadgets/")],
    "sci-tech": [("MoneyControl", "news/technology/"), ("Mint", "technology"), ("TheHindu", "sci-tech/"),
                 ("TheHindu", "sci-tech/technology/"), ("TheHindu", "sci-tech/technology/gadgets/")],
    "technology": [("MoneyControl", "news/technology/"), ("Mint", "technology"), ("TheHindu", "sci-tech/"),
                   ("TheHindu", "sci-tech/technology/"), ("TheHindu", "sci-tech/technology/gadgets/")],
    "gadgets": [("MoneyControl", "news/technology/"), ("Mint", "technology"), ("TheHindu", "sci-tech/"),
                ("TheHindu", "sci-tech/technology/"), ("TheHindu", "sci-tech/technology/gadgets/")],
    "internet": [("TheHindu", "sci-tech/technology/internet/")],

    # ------------------------------ Sports ------------------------------
    "sports": [("HindustanTimes", "cricket"), ("BusinessStandard", "sports"), ("TheHindu", "sport")],
    "cricket": [("HindustanTimes", "cricket"), ("TheHindu", "sport/cricket/")],
    "football": [("TheHindu", "sport/football/")],
    "hockey": [("TheHindu", "sport/hockey/")],
    "tennis": [("TheHindu", "sport/tennis/")],
    "athletics": [("TheHindu", "sport/athletics/")],
    "moto-sport": [("TheHindu", "sport/motosport/")],
    "races": [("TheHindu", "sport/races/")],

    # ------------------------------ General News ----------------------------
    "latest-news": [("MoneyControl", "news/news-all/"), ("Mint", "latest-news"), ("NDTV", "latest"),
                    ("HindustanTimes", "latest-news"), ("BusinessStandard", "latest-news"), ("TheHindu", "")],
    "news": [("MoneyControl", "news/news-all/"), ("Mint", "news"), ("NDTV", "latest"),
             ("HindustanTimes", "latest-news"), ("BusinessStandard", "latest-news"), ("TheHindu", "news")],
    "india": [("MoneyControl", "news/india/"), ("NDTV", "india"), ("HindustanTimes", "india-news"),
              ("BusinessStandard", "indian-news"), ("TheHindu", "news/national/")],
    "national": [("MoneyControl", "news/india/"), ("NDTV", "india"), ("HindustanTimes", "india-news"),
                 ("BusinessStandard", "indian-news"), ("TheHindu", "news/national/")],
    "world": [("MoneyControl", "news/world/"), ("NDTV", "world-news"), ("HindustanTimes", "world-news"),
              ("TheHindu", "news/international/")],
    "international": [("MoneyControl", "news/world/"), ("NDTV", "world-news"), ("HindustanTimes", "world-news"),
                      ("TheHindu", "news/international/")],

    # ------------------ Entertainment, Lifestyle & Health -------------------
    "entertainment": [("MoneyControl", "news/trends/entertainment/"), ("HindustanTimes", "entertainment"),
                      ("BusinessStandard", "entertainment")],
    "lifestyle": [("MoneyControl", "news/trends/lifestyle/"), ("HindustanTimes", "lifestyle"),
                  ("BusinessStandard", "lifestyle")],
    "health": [("MoneyControl", "news/health-and-fitness/"), ("BusinessStandard", "health"),
               ("TheHindu", "sci-tech/health/")],
    "trends": [("MoneyControl", "news/trends/")],
    "photos": [("MoneyControl", "news/photos/")],
    "travel": [("MoneyControl", "news/trends/travel/")],
    "social-media": [("BusinessStandard", "social-viral")],
    "agriculture": [("TheHindu", "sci-tech/agriculture/")],

    # ------------------------------ States & Cities News ------------------------------
    "delhi": [("HindustanTimes", "cities/delhi-news"), ("TheHindu", "news/cities/Delhi/")],
    "mumbai": [("HindustanTimes", "cities/mumbai-news"), ("TheHindu", "news/cities/mumbai/")],
    "bengaluru": [("HindustanTimes", "cities/bengaluru-news")],
    "gurugram": [("HindustanTimes", "cities/gurugram-news")],
    "noida": [("HindustanTimes", "cities/noida-news")],
    "hyderabad": [("HindustanTimes", "topic/hyderabad"), ("TheHindu", "news/cities/Hyderabad/")],
    "chennai": [("HindustanTimes", "topic/chennai"), ("TheHindu", "news/cities/chennai/")],
    "kolkata": [("HindustanTimes", "cities/kolkata-news"), ("TheHindu", "news/cities/kolkata/")],
    "bhopal": [("HindustanTimes", "cities/bhopal-news")],
    "chandigarh": [("HindustanTimes", "cities/chandigarh-news")],
    "dehradun": [("HindustanTimes", "cities/dehradun-news")],
    "indore": [("HindustanTimes", "cities/indore-news")],
    "jaipur": [("HindustanTimes", "cities/jaipur-news")],
    "lucknow": [("HindustanTimes", "cities/lucknow-news")],
    "patna": [("HindustanTimes", "cities/patna-news")],
    "pune": [("HindustanTimes", "cities/pune-news")],
    "ranchi": [("HindustanTimes", "cities/ranchi-news")],
    "andhra-pradesh": [("TheHindu", "news/national/andhra-pradesh/")],
    "karnataka": [("TheHindu", "news/national/karnataka/")],
    "kerala": [("TheHindu", "news/national/kerala/")],
    "tamil-nadu": [("TheHindu", "news/national/tamil-nadu/")],
    "telangana": [("TheHindu", "news/national/telangana/")],
    "bangalore": [("TheHindu", "news/cities/bangalore/")],
    "coimbatore": [("TheHindu", "news/cities/Coimbatore/")],
    "kochi": [("TheHindu", "news/cities/Kochi/")],
    "kozhikode": [("TheHindu", "news/cities/kozhikode/")],
    "madurai": [("TheHindu", "news/cities/Madurai/")],
    "mangalore": [("TheHindu", "news/cities/Mangalore/")],
    "puducherry": [("TheHindu", "news/cities/puducherry/")],
    "thiruvananthapuram": [("TheHindu", "news/cities/Thiruvananthapuram/")],
    "tiruchirapalli": [("TheHindu", "news/cities/Tiruchirapalli/")],
    "vijayawada": [("TheHindu", "news/cities/Vijayawada/")],
    "visakhapatnam": [("TheHindu", "news/cities/Visakhapatnam/")],
    "cities": [("NDTV", "cities"), ("TheHindu", "news/cities/")],
    "states": [("TheHindu", "news/states/")],

    # ------------------------------ Politics ------------------------------
    "politics": [("MoneyControl", "news/politics/"), ("BusinessStandard", "politics")],
    "elections": [("BusinessStandard", "elections")],

    # ------------------------------ Education ------------------------------
    "science": [("MoneyControl", "news/tags/science.html"), ("TheHindu", "sci-tech/science/")],
    "books": [("MoneyControl", "news/tags/books.html"), ("BusinessStandard", "book")],
    "infographic": [("MoneyControl", "news/infographic/")],
    "environment": [("TheHindu", "sci-tech/energy-and-environment")],
    "education": [("MoneyControl", "news/tags/education.html"), ("NDTV", "education"),
                  ("BusinessStandard", "education")],

    # ------------------------------- Others --------------------------------
    "premium": [("Mint", "premium")],
    "opinion": [("Mint", "opinion"), ("NDTV", "opinion")],
    "interview": [("TheHindu", "opinion/interview/")],
    "offbeat": [("NDTV", "offbeat")],
    "feature": [("NDTV", "feature")],
    "others": [("HindustanTimes", "cities/others-news"), ("TheHindu", "news/national/other-states/"),
               ("TheHindu", "sport/other-sports/"), ("TheHindu", "data/"), ("TheHindu", "opinion/lead/")],

}
supported_categories = categories.keys()

# --------------------------------------------------------------------------------------------


# ----------------------------------------- CRAWLERS -----------------------------------------
crawlers = ["MoneyControl", "Mint", "NDTV", "BusinessStandard", "TheHindu", "HindustanTimes"]

# --------------------------------------------------------------------------------------------


# --------------------------------------- MARKET TYPES ---------------------------------------
market_types = ["market-stats", "most-active-stock", "mutual-funds", "price-volume-shocker", "market-indices"]

# --------------------------------------------------------------------------------------------
