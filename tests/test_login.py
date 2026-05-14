

def test_valid_login(login_page):
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in login_page.page.url


def test_invalid_login(login_page):

    login_page.login("no_real_user", "secret_sauce")
    error_text = login_page.error_message.inner_text()
    assert "do not match any user" in error_text


def test_locked_out_user(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    error_text = login_page.error_message.inner_text()
    assert "has been locked out" in error_text


def test_empty_username(login_page):

    login_page.login("", "secret_sauce")
    error_text = login_page.error_message.inner_text()
    assert "Username is required" in error_text


def test_empty_password(login_page):

    login_page.login("standard_user", "")
    error_text = login_page.error_message.inner_text()
    assert "Password is required" in error_text
