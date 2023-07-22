import random
import time
import os
from typing import Dict, Union, List

import requests
from requests.models import Response
from requests.sessions import Session
from bs4 import BeautifulSoup

try:
    # for API
    from .user_agents import USER_AGENTS
except ImportError:
    # for testing
    from user_agents import USER_AGENTS


class BaseScraper:

    def __init__(
            self,
            host: str = None,
            url_structure: str = None,
            method: str = "get",
            max_retries: int = 5,
            headers: Dict = None,
            backoff_time: int = 1,
            parser: str = "lxml"
    ) -> None:
        """Constructor

        Args:
            host (str, optional): Host name of the targeted website. Defaults to None.
            url_structure (str, optional): URL structure of the page. Defaults to None.
            method (str, optional): The request method (e.g., "GET", "POST"). Defaults to "GET".
            max_retries (int, optional): The number of retries to make if the request fails. Defaults to 5.
            headers (Dict, optional): The headers to send with the request. Defaults to None.
            backoff_time (int, optional): The initial backoff time in seconds between retries. Defaults to 1.
            parser (str, optional): Desirable features of the parser to be used. Defaults to "lxml".
        """
        self.url_structure = url_structure
        self.method = method.lower()
        self.max_retries = max_retries
        self.headers = headers
        self.backoff_time = backoff_time
        self.parser = parser
        self.session: Session = requests.session()
        self.soup = None  # Stores Beautiful soup object
        self.json_data = None  # Stores Json data
        self.base_url = None  # Stores base url ex. https://testing.com

        # Check the header if it is None, then convert it to Dict
        if not self.headers:
            self.headers = {}

        # Set base_url if host is not None
        if host:
            self.base_url = f"https://{host}"

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

        # Below check is to handle the case where we need to switch to another host/subdomain/url.
        # Although this is not the right way to handle this, it will update in the future.
        if self.url_structure and not self.url_structure.startswith("http"):
            url: str = os.path.join(self.base_url, self.url_structure)
        elif self.url_structure:
            url: str = self.url_structure
        else:
            url = self.base_url

        # Check if User-Agent is present in the header, add it if not present
        if not self.headers.get("User-Agent"):
            self.headers["User-Agent"] = self.get_random_user_agent()

        # update the session headers
        self.session.headers.update(self.headers)

        # bound the session object with specified method
        session_method = getattr(self.session, self.method)

        for _ in range(self.max_retries):
            response: Response = session_method(url)

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

    def get_json_response(self) -> Union[List, Dict]:
        """Make a request and return json response

        Returns:
            Union[List, Dict]: List or Dict
        """
        resp: Response = self.make_reqeust()
        return resp.json()

    def follow(self, url_structure: str, method: str = "get", data_type: str = "soup") -> None:
        """Use this method to update the soup/json object

        Args:
            url_structure (str): Nested URL structure or full URL
            method (str, optional): The request method (e.g., "GET", "POST"). Defaults to "GET".
            data_type (str, optional): Json or Soup. Defaults to "soup"
        """
        self.url_structure = url_structure
        self.method = method

        # Check the data_type
        if data_type == "json":
            self.json_data = self.get_json_response()
        else:
            self.soup = self.get_soup_object()


if __name__ == "__main__":
    news_scraper = BaseScraper("google.com")
    print(news_scraper.soup.prettify())
