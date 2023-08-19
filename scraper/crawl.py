import os
from typing import List, Dict

from bs4.element import Tag, ResultSet

try:
    # for API
    from .base import BaseScraper
except ImportError:
    # for testing
    from base import BaseScraper


class MoneyControl(BaseScraper):

    def __init__(self) -> None:
        """Constructor"""
        super().__init__(host="moneycontrol.com")

    @staticmethod
    def __add_stats_details(result_set: ResultSet, market_stats: List) -> None:
        """Used to add the market stats details in a dictionary

        Args:
            result_set (ResultSet): Raw scraped data
            market_stats (List): List to store the data
        """
        for tr in result_set[1:]:
            td: List[Tag] = tr.find_all("td")
            market_stats.append([td[0].get_text(), td[1].get_text(), td[2].get_text()])

    def get_headline(self) -> Dict:
        """Get the headline

        Returns:
            Dict: News title, description & url
        """
        if not self.url_structure:
            raise Exception("Unspecified URL structure, please specify a url.")

        # load soup object
        self.soup = self.get_soup_object()

        headline: Tag = self.soup.find("li", {"class": "clearfix"})
        title: str = headline.a.get("title")
        description: str = headline.p.get_text()
        url: str = headline.a.get("href")
        return {
            "title": title,
            "description": description,
            "url": url
        }

    def scrape_news(self, news_count: int = 5) -> List[Dict]:
        """Scrapes the news details

        Args:
            news_count (int, optional): Number of news to scrape. Defaults to 5.

        Returns:
            List[Dict]: List of dict containing news title, description & url
        """
        if not self.url_structure:
            raise Exception("Unspecified URL structure, please specify a URL. Use follow method to update soup object.")

        # load soup object
        self.soup = self.get_soup_object()

        news: Tag = self.soup.find("ul", {"id": "cagetory"})
        news_details: List = []
        news_id, page = 0, 0

        while news_count > 0:
            try:
                headline: Tag = news.find("li", {"id": f"newslist-{news_id}"})
                news_details.append({
                    "title": headline.a.get("title"),
                    "description": headline.p.get_text(),
                    "url": headline.a.get("href")
                })

            except AttributeError:
                self.follow(f"{self.url_structure}/page-{page + 1}")
                news_id = 0
                continue

            news_count -= 1
            news_id += 1

        return news_details

    def stock_market_stats(self, exchange: str) -> Dict:
        """Market overall stats

        Args:
            exchange (str): Stock exchange name (nse or bse).

        Returns:
            Dict: Contains Top 3 gain, lose, 52-week high & 52-week low stocks details
        """
        # load soup object
        self.url_structure = "stocks/marketstats/index.php"
        self.soup = self.get_soup_object()

        # get all the tables
        topgain_table: Tag = self.soup.find("div", {"id": "div1_topgainlose"})
        toplose_table: Tag = self.soup.find("div", {"id": "div2_topgainlose"})
        _52_week_high_table: Tag = self.soup.find("div", {"id": "div1_52weekhighlow"})
        _52_week_low_table: Tag = self.soup.find("div", {"id": "div2_52weekhighlow"})

        exchange_name: str = exchange.lower()
        topgain: ResultSet = topgain_table.find("div", {"id": f"topgain_{exchange_name}"}).find_all("tr")
        toplose: ResultSet = toplose_table.find("div", {"id": f"toplose_{exchange_name}"}).find_all("tr")
        _52_week_high: ResultSet = _52_week_high_table.find("div", {"id": f"52high_{exchange_name}"}).find_all("tr")
        _52_week_low: ResultSet = _52_week_low_table.find("div", {"id": f"52low_{exchange_name}"}).find_all("tr")

        # market stats dict
        market_stats = {"top_gain": [],
                        "top_lose": [],
                        "52_week_high": [],
                        "52_week_low": []}

        # top gain
        self.__add_stats_details(topgain, market_stats["top_gain"])
        market_stats["top_gain"].insert(0, ["company", "current", "percentage_gain"])

        # top lose
        self.__add_stats_details(toplose, market_stats["top_lose"])
        market_stats["top_lose"].insert(0, ["company", "current", "percentage_loss"])

        # 52-week high
        self.__add_stats_details(_52_week_high, market_stats["52_week_high"])
        market_stats["52_week_high"].insert(0, ["company", "days_high", "current"])

        # 52-week low
        self.__add_stats_details(_52_week_low, market_stats["52_week_low"])
        market_stats["52_week_low"].insert(0, ["company", "days_low", "current"])

        return market_stats

    def personal_finance(self):
        """Scrape news about financial planning

        Returns:
            Dict: News title, description & url
        """
        # load soup object
        self.url_structure = "mc/pfspending/investingplanninglisting?&start=0"
        self.soup = self.get_soup_object()

        heading = self.soup.find("h3", {"class": "news_heading"})
        title = heading.get_text()
        description = self.soup.find("p", {"class": "desc_mobile"}).get_text()
        url = self.base_url + heading.a.get("href")

        return {
            "title": title,
            "description": description,
            "url": url
        }


class Mint(BaseScraper):

    def __init__(self) -> None:
        """Constructor"""
        super().__init__(host="livemint.com")

    def get_headline(self) -> Dict:
        """Get the headline

        Returns:
            Dict: News title, description & url
        """
        if not self.url_structure:
            raise Exception("Unspecified URL structure, please specify a url.")

        # load soup object
        self.soup = self.get_soup_object()

        headline: Tag = self.soup.find("h2", {"class": "headline"})
        title: str = headline.a.get_text().replace("\n", "").strip()
        referral_link: str = headline.a.get("href")
        url: str = os.path.join(self.base_url, self.url_structure) + referral_link

        # visiting the article url to scrape the description
        self.follow(self.url_structure + referral_link)
        description: str = self.soup.find("div", {"class": "summary"}).h2.get_text()

        return {
            "title": title,
            "description": description,
            "url": url
        }


class NDTV(BaseScraper):
    def __init__(self) -> None:
        """Constructor"""
        super().__init__(host="ndtv.com")

    def get_headline(self):
        """Get the headline

        Returns:
            Dict: News title, description & url
        """
        if not self.url_structure:
            raise Exception("Unspecified URL structure, please specify a url.")

        # load soup object
        self.soup = self.get_soup_object()

        headline: Tag = self.soup.find("div", {"class": "news_Itm-cont"})
        title: str = headline.h2.a.get_text()
        description: str = headline.p.get_text()
        url: str = headline.a.get("href")

        return {
            "title": title,
            "description": description,
            "url": url
        }


class BusinessToday(BaseScraper):
    def __init__(self) -> None:
        """Constructor"""
        super().__init__(host="businesstoday.in")

    def get_headline(self):
        """Get the headline

        Returns:
           Dict: News title, description & url
        """
        # load soup object
        self.soup = self.get_soup_object()

        headline: Tag = self.soup.find("div", {"class": "bn_item_title"})
        title: str = headline.h3.a.get("title")
        url: str = headline.h3.a.get("href")

        # visiting the article url to scrape the description
        self.follow(url)
        description: str = self.soup.find("div", {"class": "sab-head-tranlate-sec"}).h2.get_text()

        return {
            "title": title,
            "description": description,
            "url": url
        }


class StocksMarket(BaseScraper):
    # livemint's market dashboard feed url
    live_mint = "https://www.livemint.com/lm-img/markets/prod/mintgeniemarketdashboardfeed.json"

    def load_json_data(self, url: str) -> None:
        """Loads the stock data into the json_data variable declared in the parent class

            Args:
                url (str): Nested URL structure or full URL
        """
        self.follow(url, data_type="json")

    def market_stats(self):
        """Detailed market stats

        Returns:
            Dict: Contains Top gain, lose, 52-week high & 52-week low stocks details
        """
        # load json data
        self.load_json_data(self.live_mint)

        top_gainers = self.json_data["data"][2]["data"]["topGainers"] + \
                      self.json_data["data"][3]["data"]["topGainers"]
        top_looser = self.json_data["data"][2]["data"]["topLooser"] + \
                     self.json_data["data"][3]["data"]["topLooser"]
        _52_week_high = self.json_data["data"][4]["data"]["BSE_52WeekHighLow"]["high52Week"] + \
                        self.json_data["data"][4]["data"]["NSE_52WeekHighLow"]["high52Week"]
        _52_week_low = self.json_data["data"][4]["data"]["BSE_52WeekHighLow"]["low52Week"] + \
                       self.json_data["data"][4]["data"]["NSE_52WeekHighLow"]["low52Week"]

        return {
            "top_gainers": top_gainers,
            "top_looser": top_looser,
            "52_weeK_high": _52_week_high,
            "52_week_low": _52_week_low
        }

    def most_active_stocks(self):
        """Most active stocks

        Returns:
            Dict: Most active stocks on NSE & BSE
        """
        # load json data
        self.load_json_data(self.live_mint)

        # most active stocks
        active_stocks_nse = self.json_data["data"][5]["data"]  # NSE
        active_stocks_bse = self.json_data["data"][6]["data"]  # BSE
        return {
            "most_active_nse": active_stocks_nse,
            "most_active_bse": active_stocks_bse
        }

    def market_mutual_funds(self):
        """Gives details of types of mutual funds like debt, index, small cap, mid cap etc.

        Returns:
            Dict: Contains Mutual funds details
        """
        # load json data
        self.load_json_data(self.live_mint)

        mutual_funds = self.json_data["data"][7]["data"]
        return mutual_funds

    def price_volume_shocker(self):
        """A list of stocks that have risen or dived sharply on the BSE & the NSE.

        Returns:
            Dict: Price shocker details
        """
        # load json data
        self.load_json_data(self.live_mint)

        data = self.json_data["data"][8]["data"]
        return data

    def market_indices(self):
        """Market indices like S&P 500, BSE Midcap, BSE SENSEX etc.

        Returns:
            List: Indices details
        """
        # load json data
        self.load_json_data(self.live_mint)

        indices = self.json_data["data"][1]["data"]
        return indices


class HindustanTimes(BaseScraper):

    def __init__(self) -> None:
        """Constructor"""
        super().__init__(host="hindustantimes.com")

    def get_headline(self) -> Dict:
        """Get the headline

        Returns:
            Dict: News title, description & url
        """
        if not self.url_structure:
            raise Exception("Unspecified URL structure, please specify a url.")

        # load soup object
        self.soup = self.get_soup_object()

        headline: Tag = self.soup.find("h3", {"class": "hdg3"})
        title: str = headline.a.get_text()
        referral_link: str = headline.a.get("href")
        url: str = self.base_url + referral_link

        # visiting the article url to scrape the description
        self.follow(referral_link)

        description: str = self.soup.find("h2", {"class": "sortDec"}).get_text()

        return {
            "title": title,
            "description": description,
            "url": url
        }


class BusinessStandard(BaseScraper):
    def __init__(self) -> None:
        """Constructor"""

        # since business-standard.com doesn't support all User-Agents
        # so, this is a list of some User-Agents which business-standard.com is supported
        user_agents = [
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; Win64; x64; Trident/7.0; .NET4.0E; .NET4.0C; "
            ".NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; Microsoft Outlook 15.0.5023; ms-office; "
            "MSOffice 15)",
            "Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
            "Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) "
            "Version/8.0 Mobile/12B466 Safari/600.1.4",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) "
            "Version/9.1.2 Safari/601.7.7"
        ]

        # business-standard headers
        headers = {
            "Authority": "www.business-standard.com",
            "Method": "GET",
            "Scheme": "https",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Linux",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Sec-Gpc": "1",
            "Upgrade-Insecure-Requests": "1",
            # X-Forwarded-For is required to run this on the server
            # they have already blacked listed the servers IP addresses
            "X-Forwarded-For": "102.214.133.35"
        }

        super().__init__(
            host="business-standard.com",
            update_user_agent=True,
            user_agents=user_agents,
            headers=headers
        )

    def get_headline(self) -> Dict:
        """Get the headline

        Returns:
            Dict: News title, description & url
        """
        if not self.url_structure:
            raise Exception("Unspecified URL structure, please specify a url.")

        # load soup object
        self.soup = self.get_soup_object()

        headline: Tag = self.soup.find("div", {"class": "image-title"})
        title: str = headline.a.get_text()
        referral_link: str = headline.a.get("href")

        if not referral_link.startswith("http"):
            url: str = self.base_url + referral_link
        else:
            url: str = referral_link

        # visiting the article url to scrape the description
        self.follow(referral_link)

        # handle AttributeError
        try:
            description: str = self.soup.find("h2", {"class": "strydsc"}).get_text()
        except AttributeError:
            description: str = ""

        return {
            "title": title,
            "description": description,
            "url": url
        }


if __name__ == "__main__":
    business_standard = BusinessStandard()
    business_standard.url_structure = "latest-news"
    print(business_standard.get_headline())
