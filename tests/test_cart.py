def test_add_backpack_to_cart(inventory_page):
    inventory_page.add_backpack_to_cart()
    cart_count = inventory_page.get_cart_item_count()
    assert cart_count == "1"


def test_remove_backpack_from_cart(inventory_page):
    inventory_page.add_backpack_to_cart()
    inventory_page.remove_backpack_from_cart()

    assert inventory_page.cart_badge.is_hidden()


def test_cart_retains_items_after_navigation(inventory_page):
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    inventory_page.page.go_back()

    assert inventory_page.get_cart_item_count() == "1"
