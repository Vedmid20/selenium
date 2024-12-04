import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestGoogleSearch:
    def __init__(self, driver):
        self.driver = driver

    def search_in_google_input(self):
        element = self.driver.find_element(By.XPATH, '//div//textarea[@class="gLFyf"]')
        element.click()
        element.send_keys('Ліонель Мессі')
        element.send_keys(Keys.RETURN)
        time.sleep(2)

    def go_to_page(self):
        link_to_wiki = self.driver.find_element(By.XPATH, '//h3[contains(text(), "Ліонель Мессі")]')
        link_to_wiki.click()
        time.sleep(4)

    def assert_check(self):
        assert 'Ліонель Мессі' in self.driver.page_source
        result = self.driver.find_element(By.ID, 'firstHeading')
        assert result.text == 'Ліонель Мессі'
        time.sleep(2)

    def driver_quit(self):
        self.driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def test_class(driver):
    test = TestGoogleSearch(driver)
    return test


def test_google_search(test_class):
    test_class.driver.get('https://www.google.com/')
    test_class.search_in_google_input()
    test_class.go_to_page()
    test_class.assert_check()
