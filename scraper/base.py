import random
import time
import os
from typing import Dict, Union

import requests
from requests.models import Response
from requests.sessions import Session
from bs4 import BeautifulSoup

from user_agents import USER_AGENTS


class NewsScraper:

    def __init__(
            self,
            host: str,
            url_structure: str = None,
            method: str = "get",
            max_retries: int = 5,
            headers: Dict = None,
            backoff_time: int = 1,
            parser: str = "lxml"
    ) -> None:
        """Constructor

        Args:
            host (str): Host name of the targeted website
            url_structure (str, optional): URL structure of the page. Defaults to None.
            method (str, optional): The request method (e.g., "GET", "POST"). Defaults to "GET".
            max_retries (int, optional): The number of retries to make if the request fails. Defaults to 5.
            headers (Dict, optional): The headers to send with the request. Defaults to None.
            backoff_time (int, optional): The initial backoff time in seconds between retries. Defaults to 1.
            parser (str, optional): Desirable features of the parser to be used. Defaults to "lxml".
        """
        self.base_url = f"https://{host}"
        self.url_structure = url_structure
        self.method = method.lower()
        self.max_retries = max_retries
        self.headers = headers
        self.backoff_time = backoff_time
        self.parser = parser
        self.session: Session = requests.session()
        self.soup = self.get_soup_object()

    @staticmethod
    def get_random_user_agent() -> str:
        """Generates a random user agents

        Returns:
            str: Random user agent
        """
        return random.choice(USER_AGENTS)["User-Agent"]

    def make_reqeust(self) -> Union[Response, None]:
        """Makes a request to a targeted website and returns the response.

        Returns:
            Union[Response, None]: The response object if the request is successful, or None if all retries fail.
        """
        self.max_retries = max(1, self.max_retries)
        delay = min(self.backoff_time, 32) + random.randint(0, 1000) / 1000.0

        if not self.headers:
            self.headers = {}

        if not self.headers.get("User-Agent"):
            self.headers["User-Agent"] = self.get_random_user_agent()

        if self.url_structure:
            url: str = os.path.join(self.base_url, self.url_structure)
        else:
            url = self.base_url

        for _ in range(self.max_retries):
            # bound the session object with specified method
            session_method = getattr(self.session, self.method)
            response = session_method(url, headers=self.headers)

            if response.ok:
                return response
            else:
                time.sleep(delay)
                delay *= 2

        return None

    def get_soup_object(self) -> BeautifulSoup:
        """Parse the HTML and returns BeautifulSoup object

        Returns:
            BeautifulSoup: BeautifulSoup object to navigate the data.
        """
        resp: Response = self.make_reqeust()
        soup = BeautifulSoup(resp.content, self.parser)
        return soup

    def follow(self, url_structure: str) -> None:
        """Use this method to update the soup object"""
        self.url_structure = url_structure
        self.soup = self.get_soup_object()


if __name__ == "__main__":
    news_scraper = NewsScraper("google.com")
    print(news_scraper.soup.prettify())
