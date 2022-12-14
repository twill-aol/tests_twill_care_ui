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
    SIGNIN_BUTTON = (By.ID, "loginFormSubmitButton")
    SIGNIN_FACEBOOK_BUTTON = (By.CLASS_NAME, "btn.btn-fb.w-100.px-0")
    SIGNIN_APPLE_BUTTON = (By.CLASS_NAME, "btn.btn-apple.w-100.px-0")
    FORGOT_PASSWORD_LINK = (By.CLASS_NAME, "text-decoration-underline.text-gray-2")
    BACK_BUTTON = (By.CLASS_NAME, "btn.btn-light.btn-back.shadow.btn-icon.btn-sm.btn-back__dark")
    ERROR_MESSAGE = (By.ID, "loginFormAuthError")

class SignupPageLocators():
    BACK_BUTTON = (By.CLASS_NAME, "btn.btn-light.btn-back.shadow.btn-icon.btn-sm.btn-back__dark")
    EMAIL_FIELD = (By.ID, "email")
    PRIVACY_CHECK_BUTTON = (By.ID, "privacy")
    TAC_LINK = (By.CSS_SELECTOR, ".mx-1.text-decoration-underline:first-child")
    PP_LINK = (By.CSS_SELECTOR, ".mx-1.text-decoration-underline:last-child")
    SIGNUP_BUTTON = (By. CLASS_NAME, "mt-3.mt-md-5.w-100.btn.btn-primary.text-uppercase")
    SIGNUP_FACEBOOK_BUTTON = (By.CLASS_NAME, "btn.btn-fb.w-100.px-0")
    SIGNUP_APPLE_BUTTON = (By.CLASS_NAME, "btn.btn-apple.w-100.px-0")
