import urllib
from selenium.webdriver.common.by import By
import browser_cookie3

from .driver import Driver


class Client:

    def __init__(self):
        domain = "linkedin.com"
        url = f"https://{domain}/"
        cookie_name = "li_at"
        cookie_value = self.getCookiesFromDomain(domain, cookie_name)
        cookie = {
            "name": cookie_name,
            "value": cookie_value,
            "domain": f".{domain}",
        }

        self.driver = Driver(url, cookie)

    @staticmethod
    def getCookiesFromDomain(domain, cookieName=""):
        """
        Get cookies from Firefox browser for a specific domain.

        Args:
            domain: The domain to extract cookies for
            cookieName: Specific cookie name to extract (optional)

        Returns:
            Dictionary of cookies or a specific cookie value
        """
        Cookies = {}
        cookiesList = list(browser_cookie3.firefox())

        for cookie in cookiesList:
            if domain in cookie.domain:
                # print (cookie.name, cookie.domain,cookie.value)
                Cookies[cookie.name] = cookie.value

        if cookieName != "":
            try:
                return Cookies[cookieName]  # return specified cookie
            except KeyError:
                return {}  # if cookie not found return an empty dictionary
        else:
            return Cookies  # return all cookies or nothing

    def find_positions(self, skills):
        pass

    def find_people(self, skills):
        skills = skills.split(",")
        search = " ".join(skills)

        # Use quote_plus instead of quote to properly encode spaces as %20
        encoded_string = urllib.parse.quote_plus(search.lower())

        # Print the URL for debugging
        base_url = "https://www.linkedin.com/search/results/people/"
        url = f"{base_url}?keywords={encoded_string}"
        print(f"Navigating to URL: {url}")

        self.driver.navigate(url)

        people = self.driver.get_elements("ul li div div.linked-area")

        results = []
        for person in people:
            try:
                result = {}

                # Get name
                name_selector = (
                    "a[data-test-app-aware-link] "
                    "span[aria-hidden='true']"
                )
                result["name"] = person.find_element(
                    By.CSS_SELECTOR,
                    name_selector
                ).text.strip()

                # Get position
                try:
                    # Using XPath to find the position element
                    xpath_position = (
                        ".//div[contains(@class, 't-14') and "
                        "contains(@class, 't-black')]"
                    )
                    position_element = person.find_element(
                        By.XPATH, xpath_position
                    )
                    result["position"] = position_element.text.strip()
                except Exception:
                    result["position"] = "Position not found"

                # Get location by looking at the second t-14 t-normal div
                try:
                    # Using XPath to find the location element
                    xpath_location = (
                        ".//div[contains(@class, 't-14') and "
                        "contains(@class, 't-normal') and "
                        "not(contains(@class, 't-black'))]"
                    )
                    location_element = person.find_element(
                        By.XPATH, xpath_location
                    )
                    result["location"] = location_element.text.strip()
                except Exception:
                    result["location"] = "Location not found"

                # Get profile link which is more reliable
                result["profile_link"] = person.find_element(
                    By.CSS_SELECTOR,
                    "a[data-test-app-aware-link]"
                ).get_attribute("href")
            except Exception as e:
                print(f"Error extracting data: {e}")
                continue
            results.append(result)
        return results

    def close(self):
        self.driver.close()
