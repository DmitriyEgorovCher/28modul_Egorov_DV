from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_main_link(self):
        url = urlparse(self.driver.current_url)
        return url.netloc

    def get_windows_title(self, text) -> bool:
        windows_title = WebDriverWait(self.driver, 5).until(EC. title_contains(text))
        return bool(windows_title)
