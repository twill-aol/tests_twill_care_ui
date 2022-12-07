from selenium.webdriver.common.by import By


class BasePageLocators():
    pass

class MainPageLocators():
    ARTICLES_LINK = (By.CSS_SELECTOR, "ul.nav:nth-child(2) > li:nth-child(1) > a:nth-child(1)")
    EXPERTS_LINK = (By.CSS_SELECTOR, "li.nav-item:nth-child(2) > a:nth-child(1)")
    LOGIN_LINK = (By.CSS_SELECTOR, "li.nav-item:nth-child(3) > a:nth-child(1)")
    SIGNUP_LINK = (By.CSS_SELECTOR, "a.px-4:nth-child(1)")

class BaseAuthPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    BUTTON_REVIEW = (By.ID, "write_review")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MESSAGE_BLOCK = (By.ID, "messages")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME_IN_ALLERT = (By.CLASS_NAME, "alertinner ")
    PRODUCT_PRICE_IN_CART_MINI = (By.CLASS_NAME, "basket-mini.pull-right.hidden-xs")
    PRODUCT_PRICE_IN_CART_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
