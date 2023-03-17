from locators.login_page import Login
from page_objects.functions import Functions


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.func = Functions(self.driver)
        self.login = Login()

    # get img alt orange hrm image
    def get_orange_hrm_image_img_alt(self):
        return self.func.get_img_alt(self.login.orange_hrm_image)

    # get text login header
    def get_login_header_text(self):
        return self.func.get_inner_text(self.login.login_header)

    # is displayed credentials section
    def is_credentials_section_displayed(self):
        return self.func.is_displayed(self.login.credentials_section)

    # get text username admin
    def get_username_admin_text(self):
        return self.func.get_inner_text(self.login.username_admin)

    # get text password admin123
    def get_password_admin123_text(self):
        return self.func.get_inner_text(self.login.password_admin123)

    # is displayed username icon
    def is_username_icon_displayed(self):
        return self.func.is_displayed(self.login.username_icon)

    # get text username label
    def get_username_label_text(self):
        return self.func.get_inner_text(self.login.username_label)

    # is displayed username field
    def is_username_field_displayed(self):
        return self.func.is_displayed(self.login.username_field)

    # is displayed password icon
    def is_password_icon_displayed(self):
        return self.func.is_displayed(self.login.password_icon)

    # get text password label
    def get_password_label_text(self):
        return self.func.get_inner_text(self.login.password_label)

    # is displayed password field
    def is_password_field_displayed(self):
        return self.func.is_displayed(self.login.password_field)

    # is displayed login button
    def is_login_button_displayed(self):
        return self.func.is_displayed(self.login.login_button)

    # get text forgot your password
    def get_forgot_your_password_text(self):
        return self.func.get_inner_text(self.login.forgot_your_password)

    # is displayed copyright section
    def is_copyright_section_displayed(self):
        return self.func.is_displayed(self.login.copyright_section)

    # is displayed linkedin icon
    def is_linkedin_icon_displayed(self):
        return self.func.is_displayed(self.login.linkedin_icon)

    # is displayed facebook icon
    def is_facebook_icon_displayed(self):
        return self.func.is_displayed(self.login.facebook_icon)

    # is displayed twitter icon
    def is_twitter_icon_displayed(self):
        return self.func.is_displayed(self.login.twitter_icon)

    # is displayed youtube icon
    def is_youtube_icon_displayed(self):
        return self.func.is_displayed(self.login.youtube_icon)

    # enter text username field
    def enter_username_field_text(self, text):
        return self.func.enter_text(self.login.username_field, text)

    # get text value username field
    def get_username_field_text_value(self):
        return self.func.get_text_value(self.login.username_field)

    # enter text password field
    def enter_password_field_text(self, text):
        return self.func.enter_text(self.login.password_field, text)

    # get text value password field
    def get_password_field_text_value(self):
        return self.func.get_text_value(self.login.password_field)

    # click login button
    def click_login_button(self):
        self.func.click(self.login.login_button)

    # get text invalid credentials
    def get_invalid_credentials_text(self):
        return self.func.get_inner_text(self.login.invalid_credentials)

    # clear username field
    def clear_username_field(self):
        self.func.clear(self.login.username_field)

    # clear password field
    def clear_password_field(self):
        self.func.clear(self.login.password_field)
