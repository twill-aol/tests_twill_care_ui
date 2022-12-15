from selenium.webdriver.common.by import By


class BasePageLocators():
    pass

class MainPageLocators():
    ARTICLES_LINK = (By.CSS_SELECTOR, "ul.nav:nth-child(2) > li:nth-child(1) > a:nth-child(1)")
    EXPERTS_LINK = (By.CSS_SELECTOR, "li.nav-item:nth-child(2) > a:nth-child(1)")
    LOGIN_LINK = (By.CSS_SELECTOR, "li.nav-item:nth-child(3) > a:nth-child(1)")
    SIGNUP_LINK = (By.CSS_SELECTOR, "a.px-4:nth-child(1)")

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

class BaseAuthPageLocators():
    LOGO_LINK = (By.CLASS_NAME, "Grid_col.Grid_col-xs6.Grid_col-mdPlus2")
    TOP_NAV = (By.CLASS_NAME, "TopNav")
    SEARCH_BUTTON = (By.CLASS_NAME, "fa-regular.fa-magnifying-glass")
    SAVED_POSTS_BUTTON = (By.CLASS_NAME, "fa-regular.fa-magnifying-glass")
    NOTIFICATIONS_BUTTON = (By.CLASS_NAME, "fa-regular.fa-magnifying-glass")
    USER_MENU_LINK = (By.CLASS_NAME, "dropdown")
    CREATE_POST_BUTTON = (By.CSS_SELECTOR, ".MainNav_link:nth-child(1)")
    FEED_BUTTON = (By.CSS_SELECTOR, ".MainNav_link:nth-child(2)")
    EXPLORE_BUTTON = (By.CSS_SELECTOR, ".MainNav_link:nth-child(3)")
    TOOLS_BUTTON = (By.CSS_SELECTOR, ".MainNav_link:nth-child(4)")
    MORE_BUTTON = (By.CSS_SELECTOR, ".MainNav_link:nth-child(5)")
    FACEBOOK_LINK = (By.CLASS_NAME, "fa-brands.fa-facebook-f")
    INSTAGRAM_LINK = (By.CLASS_NAME, "fa-brands.fa-instagram")
    ADDITIONAL_INFO_LINK = (By.CSS_SELECTOR, 'data-track-click="Additional_info_navigated"')
