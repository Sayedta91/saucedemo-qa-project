import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture
def login_page(page):
    page.goto(BASE_URL)
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    page.goto(BASE_URL)

    login = LoginPage(page)
    login.login("standard_user", "secret_sauce")

    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    page.goto(BASE_URL)

    login = LoginPage(page)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.go_to_cart()

    return CartPage(page)
