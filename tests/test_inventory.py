
def test_inventory_count(inventory_page):
    product_count = inventory_page.get_product_count()
    assert product_count == 6


def test_sort_az(inventory_page):
    inventory_page.sort_products("az")
    product_names = inventory_page.get_product_names()
    assert product_names == sorted(product_names)


def test_sort_za(inventory_page):
    inventory_page.sort_products("za")
    product_names = inventory_page.get_product_names()
    assert product_names == sorted(product_names, reverse=True)


def test_sort_price_low_high(inventory_page):
    inventory_page.sort_products("lohi")
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices)


def test_sort_price_high_low(inventory_page):
    inventory_page.sort_products("hilo")
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices, reverse=True)


# def test_sort_persists_after_reload(inventory_page):
#     inventory_page.sort_products("za")

#     before_refresh = inventory_page.get_product_names()
#     inventory_page.page.reload()
#     after_refresh = inventory_page.get_product_names()

#     assert before_refresh == after_refresh

