import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.create_account_page import CreateAccountPage
from pages.eco_friendly_collection_page import EcoCollectionPage
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)


@pytest.fixture()
def eco_collection_page(driver):
    return EcoCollectionPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
