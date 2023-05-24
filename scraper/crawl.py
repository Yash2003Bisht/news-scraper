from typing import List, Tuple, Dict

from base import NewsScraper

from bs4.element import Tag, ResultSet


class MoneyControl(NewsScraper):

    @staticmethod
    def __add_stats_details(result_set: ResultSet, market_stats: Dict, column_names: List) -> None:
        for tr in result_set[1:]:
            td: List[Tag] = tr.find_all("td")
            market_stats[column_names[0]].append(td[0].get_text())
            market_stats[column_names[1]].append(td[1].get_text())
            market_stats[column_names[2]].append(td[2].get_text())

    def get_headline(self) -> Tuple[str, str, str]:
        """Get the headline

        Returns:
            Tuple[str, str, str]: News title, description & url
        """
        if not self.url_structure:
            raise Exception("Unspecified URL structure, please specify a url.")

        headline: Tag = self.soup.find("li", {"class": "clearfix"})
        title: str = headline.a.get("title")
        description: str = headline.p.get_text()
        url: str = headline.a.get("href")
        return title, description, url

    def scrape_news(self, news_count: int = 5) -> List[Dict]:
        """Scrapes the news details

        Args:
            news_count (int, optional): Number of news to scrape. Defaults to 5.

        Returns:
            List[Dict]: List of dict containing news title, description & url
        """
        if not self.url_structure:
            raise Exception("Unspecified URL structure, please specify a URL. Use follow method to update soup object.")

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
        # update the soup object
        self.follow("stocks/marketstats/index.php")

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
        market_stats = {"top_gain": {"company": [], "current": [], "percentage_gain": []},
                        "top_lose": {"company": [], "current": [], "percentage_gain": []},
                        "52_week_high": {"company": [], "days_high": [], "current": []},
                        "52_week_low": {"company": [], "days_low": [], "current": []}}

        # top gain
        self.__add_stats_details(topgain, market_stats["top_gain"], ["company", "current", "percentage_gain"])

        # top lose
        self.__add_stats_details(toplose, market_stats["top_lose"], ["company", "current", "percentage_gain"])

        # 52-week high
        self.__add_stats_details(_52_week_high, market_stats["52_week_high"], ["company", "days_high", "current"])

        # 52-week low
        self.__add_stats_details(_52_week_low, market_stats["52_week_low"], ["company", "days_low", "current"])

        return market_stats


if __name__ == "__main__":
    money_control = MoneyControl(host="moneycontrol.com")
    money_control.follow("news/business/economy/")
    data = money_control.get_headline()
    print(data)

    # money_control.follow("news/business/personal-finance/")
    # data = money_control.scrape_news()

    # import json
    #
    # with open("data4.json", "w") as file:
    #     json.dump(data, file, indent=4)
