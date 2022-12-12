from selenium.webdriver.common.by import By


class BasePageLocators():
    pass

class MainPageLocators():
    ARTICLES_LINK = (By.CSS_SELECTOR, "ul.nav:nth-child(2) > li:nth-child(1) > a:nth-child(1)")
    EXPERTS_LINK = (By.CSS_SELECTOR, "li.nav-item:nth-child(2) > a:nth-child(1)")
    LOGIN_LINK = (By.CSS_SELECTOR, "li.nav-item:nth-child(3) > a:nth-child(1)")
    SIGNUP_LINK = (By.CSS_SELECTOR, "a.px-4:nth-child(1)")

# class BaseAuthPageLocators():
#     LOGIN_FORM = (By.ID, "login_form")
#     REGISTER_FORM = (By.ID, "register_form")

class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "main-content.col-10.col-md-8.mx-auto.my-auto")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.ID, "loginFormSubmitButton")
    SIGN_IN_FACEBOOK_BUTTON = (By.CLASS_NAME, "btn.btn-fb.w-100.px-0")
    SIGN_IN_APPLE_BUTTON = (By.CLASS_NAME, "btn.btn-apple.w-100.px-0")
    FORGOT_PASSWORD_LINK = (By.CLASS_NAME, "text-decoration-underline.text-gray-2")
    BACK_BUTTON = (By.CLASS_NAME, "btn.btn-light.btn-back.shadow.btn-icon.btn-sm.btn-back__dark")
    ERROR_MESSAGE = (By.ID, "loginFormAuthError")

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
