from pages.checkout_page import CheckoutPage


def test_checkout_starts(cart_page):
    cart_page.checkout()
    assert "checkout-step-one" in cart_page.page.url


def test_checkout_info_filled(cart_page):
    cart_page.checkout()
    checkout_page = CheckoutPage(cart_page.page)
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    assert "checkout-step-two" in cart_page.page.url


def test_checkout_empty_fields(cart_page):
    cart_page.checkout()
    checkout_page = CheckoutPage(cart_page.page)
    checkout_page.fill_checkout_info("", "", "")

    error_text = checkout_page.error_message.inner_text()
    assert "First Name is required" in error_text


def test_checkout_missing_last_name(cart_page):
    cart_page.checkout()

    checkout_page = CheckoutPage(cart_page.page)
    checkout_page.fill_checkout_info("John", "", "")

    error_text = checkout_page.error_message.inner_text()
    assert "Last Name is required" in error_text


def test_checkout_missing_postal_code(cart_page):
    cart_page.checkout()

    checkout_page = CheckoutPage(cart_page.page)
    checkout_page.fill_checkout_info("John", "Doe", "")

    error_text = checkout_page.error_message.inner_text()
    assert "Postal Code is required" in error_text


def test_checkout_completes(cart_page):
    cart_page.checkout()

    checkout_page = CheckoutPage(cart_page.page)
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.finish_checkout()

    assert "checkout-complete" in cart_page.page.url
