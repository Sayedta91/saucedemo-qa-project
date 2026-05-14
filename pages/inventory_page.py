class InventoryPage:
    def __init__(self, page):
        self.page = page

        self.products = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.add_backpack_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.remove_backpack_button = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )

    def get_product_count(self):
        return self.products.count()

    def get_product_names(self):
        return self.product_names.all_inner_texts()

    def get_product_prices(self):
        prices = self.product_prices.all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]

    def sort_products(self, sort_option):
        self.sort_dropdown.wait_for()
        self.sort_dropdown.select_option(sort_option)

    def add_backpack_to_cart(self):
        self.add_backpack_button.click()

    def remove_backpack_from_cart(self):
        self.remove_backpack_button.click()

    def get_cart_item_count(self):
        return self.cart_badge.inner_text()

    def go_to_cart(self):
        self.cart_link.click()
