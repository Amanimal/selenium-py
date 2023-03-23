from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from utilities.custom_logger import LogGen
from utilities.readProperties import ReadConfig


class Test001LoginPage:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    def start(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)

    def test_001_logo_and_title(self, setup):
        self.logger.info("************Test_001_Login_Page************")
        self.logger.info("************Validate Logo and Title************")
        self.start(setup=setup)

        # tc-1
        assert self.login.get_orange_hrm_image_img_alt() == "company-branding", \
            "Orange hrm image alt value is incorrect"
        self.logger.info("Orange hrm image alt value is correct. Value: 'company-branding'")

        # tc-2
        assert self.login.get_login_header_text() == "Login", "Login header text is not displayed correctly"
        self.logger.info("Login header text is displayed correctly. Text: 'Login'")

        # tc-3
        assert self.login.is_credentials_section_displayed() is True, "Credentials section is not displayed"
        self.logger.info("Credentials section is displayed, value: True")

        # tc-4
        assert self.login.get_username_admin_text() == "Username : Admin", \
            "Username admin text is not displayed correctly "
        self.logger.info("Username admin text is correctly displayed. Text: 'Username : Admin'")

        # tc-5
        assert self.login.get_password_admin123_text() == "Password : admin123", \
            "Password admin123 text is not displayed correctly "
        self.logger.info("Password admin123 text is correctly displayed. Text: 'Password : admin123'")

        # tc-6
        assert self.login.is_username_icon_displayed() is True, "Username icon is not displayed"
        self.logger.info("Username icon is displayed, value: True")

        # tc-7
        assert self.login.get_username_label_text() == "Username", "Username label text is not displayed correctly"
        self.logger.info("Username label text is correctly displayed. Text: 'Username'")

        # tc-8 -action
        assert self.login.is_username_field_displayed() is True, "Username field is not displayed"
        self.logger.info("Username field is displayed, value: True")

        # tc-9
        assert self.login.is_password_icon_displayed() is True, "Password icon is not displayed"
        self.logger.info("Password icon is displayed, value: True")

        # tc-10
        assert self.login.get_password_label_text() == "Password", "Password label text is not displayed correctly"
        self.logger.info("Password label text is correctly displayed. Text: 'Password'")

        # tc-11 -action
        assert self.login.is_password_field_displayed() is True, "Password field is not displayed"
        self.logger.info("Password field is displayed, value: True")

        # tc-12
        assert self.login.is_login_button_displayed() is True, "Login button is not displayed"
        self.logger.info("Login button is displayed, value: True")

        # tc-13
        assert self.login.get_forgot_your_password_text() == "Forgot your password?", "Forgot your password text is " \
                                                                                      "not displayed correctly"
        self.logger.info("Forgot your password text is correctly displayed. Text: 'Forgot your password?'")

        # tc-14
        assert self.login.is_copyright_section_displayed() is True, "Copyright section is not displayed"
        self.logger.info("Copyright section is displayed, value: True")

        # tc-15
        assert self.login.is_linkedin_icon_displayed() is True, "Linkedin icon is not displayed"
        self.logger.info("Linkedin icon is displayed, value: True")

        # tc-16
        assert self.login.is_facebook_icon_displayed() is True, "Facebook icon is not displayed"
        self.logger.info("Facebook icon is displayed, value: True")

        # tc-17
        assert self.login.is_twitter_icon_displayed() is True, "Twitter icon is not displayed"
        self.logger.info("Twitter icon is displayed, value: True")

        # tc-18
        assert self.login.is_youtube_icon_displayed() is True, "Youtube icon is not displayed"
        self.logger.info("Youtube icon is displayed, value: True")

    def test_002_incorrect_login(self, setup):
        self.logger.info("************Test_002_Incorrect_Login************")
        self.logger.info("************Verify Incorrect Login************")
        self.start(setup=setup)

        # tc-19
        self.login.enter_username_field_text("testuser")
        self.logger.info("Set username field to 'testuser'")

        # tc-20
        assert self.login.get_username_field_text_value() == "testuser", "Username field text is " \
                                                                         "not displayed correctly"
        self.logger.info("Username field text is correctly displayed. Text: 'testuser'")

        # tc-21
        self.login.enter_password_field_text(ReadConfig.get_user_password())
        self.logger.info("Set password field to '******")

        # tc-22
        assert self.login.get_password_field_text_value() == ReadConfig.get_user_password(), \
            "Password field text is not displayed correctly"
        self.logger.info("Password field text is correctly displayed. Text: '******'")

        # tc-23 -action
        self.login.click_login_button()
        self.logger.info("Login button is clicked")

        # tc-24
        assert self.login.get_invalid_credentials_text() == 'Invalid credentials', \
            "Invalid credentials text is not displayed correctly"
        self.logger.info("Invalid credentials text is correctly displayed. Text: 'Invalid credentials'")

        # tc-25
        self.login.clear_username_field()
        self.login.clear_password_field()
        self.logger.info("Username and Password fields are cleared!")

        # tc-26 - action
        self.login.enter_username_field_text(ReadConfig.get_user_name())
        self.logger.info("Set username field to '******'")

        # tc-27
        assert self.login.get_username_field_text_value() == ReadConfig.get_user_name(), "Username field text is " \
                                                                                         "not displayed correctly"
        self.logger.info("Username field text is correctly displayed. Text: '******'")

        # tc-28
        self.login.enter_password_field_text("testpassword")
        self.logger.info("Set password field to 'testpassword'")

        # tc-29
        assert self.login.get_password_field_text_value() == "testpassword", "Password field text is " \
                                                                             "not displayed correctly"
        self.logger.info("Password field text is correctly displayed. Text: 'testpassword'")

        # tc-30 -action
        self.login.click_login_button()
        self.logger.info("Login button is clicked")

        # tc-31
        assert self.login.get_invalid_credentials_text() == 'Invalid credentials', \
            "Invalid credentials text is not displayed correctly"
        self.logger.info("Invalid credentials text is correctly displayed. Text: 'Invalid credentials'")

    def test_003_login_and_logout(self, setup):
        self.logger.info("************Test_003_Login_And_Logout************")
        self.logger.info("************Verify Login and Logout************")
        self.start(setup=setup)

        # tc-32
        self.login.enter_username_field_text(ReadConfig.get_user_name())
        self.logger.info("Set username field to '******'")

        # tc-33
        assert self.login.get_username_field_text_value() == ReadConfig.get_user_name(), \
            "Username field text is not displayed correctly"
        self.logger.info("Username field text is correctly displayed. Text: '******'")

        # tc-34
        self.login.enter_password_field_text(ReadConfig.get_user_password())
        self.logger.info("Set password field to '******'")

        # tc-35
        assert self.login.get_password_field_text_value() == ReadConfig.get_user_password(), "Password field text is " \
                                                                                             "not displayed correctly "
        self.logger.info("Password field text is correctly displayed. Text: '******'")

        # tc-36 -action
        self.login.click_login_button()
        self.logger.info("Login button is clicked")

        # tc-37
        assert self.home.get_dashboard_header_text() == "Dashboard", "Dashboard header text is not displayed correctly"
        self.logger.info("Dashboard header text is correctly displayed. Text: 'Homepage'")

        # tc-38
        assert self.home.is_profile_section_displayed() is True, "Profile section is not displayed"
        self.logger.info("Profile section is displayed, value: True")

        # tc-39
        assert self.home.is_profile_pic_displayed() is True, "Profile pic is not displayed"
        self.logger.info("Profile pic is displayed, value: True")

        # tc-40
        assert self.home.is_profile_name_displayed() is True, "Profile name is not displayed"
        self.logger.info("Profile name is displayed, value: True")

        # tc-41
        self.home.click_profile_section()
        self.logger.info("Profile section is clicked")

        # tc-42
        assert self.home.is_profile_menu_displayed() is True, "Profile menu is not displayed"
        self.logger.info("Profile menu is displayed, value: True")

        # tc-43
        assert self.home.get_menu_about_text() == "About", "Menu about text is not displayed correctly"
        self.logger.info("Menu about text is correctly displayed. Text: 'About'")

        # tc-44
        assert self.home.get_menu_support_text() == "Support", "Menu support text is not displayed correctly"
        self.logger.info("Menu support text is correctly displayed. Text: 'Support'")

        # tc-45
        assert self.home.get_menu_change_password_text() == "Change Password", "Menu change password text is not " \
                                                                               "displayed correctly"
        self.logger.info("Menu change password text is correctly displayed. Text: 'Change Password'")

        # tc-46
        assert self.home.get_menu_logout_text() == "Logout", "Menu logout text is not displayed correctly"
        self.logger.info("Menu logout text is correctly displayed. Text: 'Logout'")

        # tc-47 -action
        self.home.click_menu_logout()
        self.logger.info("Menu logout is clicked")

        # tc-48
        assert self.login.get_login_header_text() == "Login", "Login header text is not displayed correctly"
        self.logger.info("Login header text is displayed correctly. Text: 'Login'")
