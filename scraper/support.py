# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LIST OF ALL SUPPORTED THINGS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# ---------------------------------------------- CATEGORIES ----------------------------------------------
categories = {

    # ---------------- Business, Investing & Stock Market ----------------
    "business": [("MoneyControl", "news/business/"), ("FinancialExpress", "business/industry/"),
                 ("FinancialExpress", "business/sme/"), ("FinancialExpress", "business/banking-finance/"),
                 ("FinancialExpress", "business/roadways/"), ("FinancialExpress", "business/airlines-aviation/"),
                 ("FinancialExpress", "business/railways/"), ("FinancialExpress", "business/infrastructure/"),
                 ("ANI", "category/business/corporate/")],
    "companies": [("MoneyControl", "news/tags/companies.html"), ("Mint", "companies"),
                  ("BusinessStandard", "companies")],
    "mutual-funds": [("MoneyControl", "news/business/mutual-funds"), ("Mint", "mutual-fund")],
    "startups": [("MoneyControl", "news/business/startups/")],
    "market": [("MoneyControl", "news/business/markets/"), ("Mint", "market"), ("BusinessStandard", "markets"),
               ("FinancialExpress", "market/")],
    "stocks": [("MoneyControl", "news/business/stocks/")],
    "ipo": [("MoneyControl", "news/business/ipo/")],
    "technical-analysis": [("MoneyControl", "news/tags/technical-analysis.html")],
    "commodity": [("MoneyControl", "news/business/commodity/")],
    "fixed-deposite": [("MoneyControl", "news/tags/company-fixed-deposits.html")],
    "currency": [("MoneyControl", "news/tags/currency.html")],
    "money": [("Mint", "money"), ("FinancialExpress", "money/")],
    "industry": [("Mint", "industry"), ("BusinessStandard", "industry"), ("FinancialExpress", "business/industry/")],
    "management": [("BusinessStandard", "management")],
    "banking": [("FinancialExpress", "business/banking-finance/")],

    # ------------------------------ Technology -----------------------------
    "tech": [("MoneyControl", "news/technology/"), ("Mint", "technology"), ("TheHindu", "sci-tech/"),
             ("TheHindu", "sci-tech/technology/"), ("TheHindu", "sci-tech/technology/gadgets/"),
             ("ANI", "category/tech/mobile/"), ("ANI", "category/tech/internet/"), ("ANI", "category/tech/computer/"),
             ("ANI", "category/tech/others/")],
    "sci-tech": [("MoneyControl", "news/technology/"), ("Mint", "technology"), ("TheHindu", "sci-tech/"),
                 ("TheHindu", "sci-tech/technology/"), ("TheHindu", "sci-tech/technology/gadgets/")],
    "technology": [("MoneyControl", "news/technology/"), ("Mint", "technology"), ("TheHindu", "sci-tech/"),
                   ("TheHindu", "sci-tech/technology/"), ("TheHindu", "sci-tech/technology/gadgets/"),
                   ("FinancialExpress", "about/business-technology/")("ANI", "category/tech/mobile/"),
                   ("ANI", "category/tech/internet/"), ("ANI", "category/tech/computer/"), ("ANI", "category/tech/others/")],
    "gadgets": [("MoneyControl", "news/technology/"), ("Mint", "technology"), ("TheHindu", "sci-tech/"),
                ("TheHindu", "sci-tech/technology/"), ("TheHindu", "sci-tech/technology/gadgets/")],
    "internet": [("TheHindu", "sci-tech/technology/internet/")],

    # ------------------------------ Sports ------------------------------
    "sports": [("HindustanTimes", "cricket"), ("BusinessStandard", "sports"), ("TheHindu", "sport"),
               ("ANI", "category/sports/cricket/"), ("ANI", "category/sports/football/"), ("ANI", "category/sports/tennis/"),
               ("ANI", "category/sports/others/"), ("ANI", "category/sports/hockey/")],
    "cricket": [("HindustanTimes", "cricket"), ("TheHindu", "sport/cricket/"), ("ANI", "category/sports/cricket/")],
    "football": [("TheHindu", "sport/football/"), ("ANI", "category/sports/football/")],
    "hockey": [("TheHindu", "sport/hockey/"), ("ANI", "category/sports/hockey/")],
    "tennis": [("TheHindu", "sport/tennis/"), ("ANI", "category/sports/tennis/")],
    "athletics": [("TheHindu", "sport/athletics/")],
    "moto-sport": [("TheHindu", "sport/motosport/")],
    "races": [("TheHindu", "sport/races/")],
    "others": [("ANI", "category/sports/others/")],

    # ------------------------------ General News ----------------------------
    "latest-news": [("MoneyControl", "news/news-all/"), ("Mint", "latest-news"), ("NDTV", "latest"),
                    ("HindustanTimes", "latest-news"), ("BusinessStandard", "latest-news"), ("TheHindu", ""),
                    ("FinancialExpress", "latest-news"), ("ANI", "latest-news")],
    "news": [("MoneyControl", "news/news-all/"), ("Mint", "news"), ("NDTV", "latest"),
             ("HindustanTimes", "latest-news"), ("BusinessStandard", "latest-news"), ("TheHindu", "news"),
             ("FinancialExpress", "latest-news"), ("ANI", "latest-news"), ("ANI", "category/national/general-news")],
    "india": [("MoneyControl", "news/india/"), ("NDTV", "india"), ("HindustanTimes", "india-news"),
              ("BusinessStandard", "indian-news"), ("TheHindu", "news/national/"), ("FinancialExpress", "india-news")],
    "national": [("MoneyControl", "news/india/"), ("NDTV", "india"), ("HindustanTimes", "india-news"),
                 ("BusinessStandard", "indian-news"), ("TheHindu", "news/national/")],
    "world": [("MoneyControl", "news/world/"), ("NDTV", "world-news"), ("HindustanTimes", "world-news"),
              ("TheHindu", "news/international/"), ("ANI", "category/world/asia/"), ("ANI", "category/world/us/"),
              ("ANI", "category/world/europe/"), ("ANI", "category/world/pacific/"), ("ANI", "category/world/middle-east/")],
    "international": [("MoneyControl", "news/world/"), ("NDTV", "world-news"), ("HindustanTimes", "world-news"),
                      ("TheHindu", "news/international/")],

    # ------------------ Entertainment, Lifestyle & Health -------------------
    "entertainment": [("MoneyControl", "news/trends/entertainment/"), ("HindustanTimes", "entertainment"),
                      ("BusinessStandard", "entertainment")],
    "lifestyle": [("MoneyControl", "news/trends/lifestyle/"), ("HindustanTimes", "lifestyle"),
                  ("BusinessStandard", "lifestyle")],
    "health": [("MoneyControl", "news/health-and-fitness/"), ("BusinessStandard", "health"),
               ("TheHindu", "sci-tech/health/"), ("FinancialExpress", "lifestyle/health/"), ("ANI", "category/health/")],
    "trends": [("MoneyControl", "news/trends/")],
    "photos": [("MoneyControl", "news/photos/")],
    "travel": [("MoneyControl", "news/trends/travel/")],
    "social-media": [("BusinessStandard", "social-viral")],
    "agriculture": [("TheHindu", "sci-tech/agriculture/")],
    "bollywood": [("ANI", "category/entertainment/bollywood/")],
    "hollywood": [("ANI", "category/entertainment/hollywodd/")],
    "music": [("ANI", "category/entertainment/music/")],
    "out-of-box": [("ANI", "category/entertainment/out-of-box/")],

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
    "politics": [("MoneyControl", "news/politics/"), ("BusinessStandard", "politics"),
                 ("FinancialExpress", "policy/economy/"), ("ANI", "category/national/politics/")],
    "elections": [("BusinessStandard", "elections")],

    # ------------------------------ Education ------------------------------
    "science": [("MoneyControl", "news/tags/science.html"), ("TheHindu", "sci-tech/science/"),
                ("FinancialExpress", "life/science/"), ("ANI", "category/science/")],
    "books": [("MoneyControl", "news/tags/books.html"), ("BusinessStandard", "book")],
    "infographic": [("MoneyControl", "news/infographic/")],
    "environment": [("TheHindu", "sci-tech/energy-and-environment")],
    "education": [("MoneyControl", "news/tags/education.html"), ("NDTV", "education"),
                  ("BusinessStandard", "education"), ("FinancialExpress", "jobs-career/education/")],

    # ------------------------------- Others --------------------------------
    "premium": [("Mint", "premium")],
    "opinion": [("Mint", "opinion"), ("NDTV", "opinion")],
    "interview": [("TheHindu", "opinion/interview/")],
    "offbeat": [("NDTV", "offbeat")],
    "feature": [("NDTV", "feature"), ("ANI", "category/national/features/")],
    "others": [("HindustanTimes", "cities/others-news"), ("TheHindu", "news/national/other-states/"),
               ("TheHindu", "sport/other-sports/"), ("TheHindu", "data/"), ("TheHindu", "opinion/lead/"),
               ("ANI", "category/world/others/")],
    "cloud-verse": [("FinancialExpress", "about/cloud-verse/")],
    "safety-privacy": [("FinancialExpress", "about/safety-privacy/")],
    "artificial-intelligence": [("FinancialExpress", "about/artificial-intelligence/")],
    "information-governance": [("FinancialExpress", "about/information-governance/")],
    "sme": [("FinancialExpress", "business/sme/")],
    "economy": [("FinancialExpress", "policy/economy/")],
}
supported_categories = categories.keys()

# --------------------------------------------------------------------------------------------


# ----------------------------------------- CRAWLERS -----------------------------------------
crawlers = ["MoneyControl", "Mint", "NDTV", "BusinessStandard", "TheHindu", "HindustanTimes",
            "FinancialExpress", "ANI"]

# --------------------------------------------------------------------------------------------


# --------------------------------------- MARKET TYPES ---------------------------------------
market_types = ["market-stats", "most-active-stock", "mutual-funds", "price-volume-shocker", "market-indices"]

# --------------------------------------------------------------------------------------------
