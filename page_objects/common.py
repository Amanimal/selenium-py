from locators.common import OrangeHRMNavbar
from locators.login_page import Login
from page_objects.functions import Functions
from utilities.readProperties import ReadConfig


class CommonPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.func = Functions(self.driver)
        self.navbar = OrangeHRMNavbar()
        self.login = Login()

    # # auto login
    def auto_login(self):
        self.func.enter_text(self.login.username_field, ReadConfig.get_user_name())
        self.func.enter_text(self.login.password_field, ReadConfig.get_user_password())
        self.func.click(self.login.login_button)

    # is displayed side navbar
    def is_side_navbar_displayed(self):
        return self.func.is_displayed(self.navbar.side_navbar)

    # is displayed navbar toggle
    def is_navbar_toggle_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_toggle)

    # is displayed navbar banner
    def is_navbar_banner_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_banner)

    # is displayed navbar search icon
    def is_navbar_search_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_search_icon)

    # is displayed navbar search field
    def is_navbar_search_field_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_search_field)

    # is displayed navbar admin icon
    def is_navbar_admin_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_admin_icon)

    # get text navbar admin
    def get_navbar_admin_text(self):
        return self.func.get_inner_text(self.navbar.navbar_admin)

    # is displayed navbar pim icon
    def is_navbar_pim_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_pim_icon)

    # get text navbar pim
    def get_navbar_pim_text(self):
        return self.func.get_inner_text(self.navbar.navbar_pim)

    # is displayed navbar leave icon
    def is_navbar_leave_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_leave_icon)

    # get text navbar leave
    def get_navbar_leave_text(self):
        return self.func.get_inner_text(self.navbar.navbar_leave)

    # is displayed navbar time icon
    def is_navbar_time_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_time_icon)

    # get text navbar time
    def get_navbar_time_text(self):
        return self.func.get_inner_text(self.navbar.navbar_time)

    # is displayed navbar recruitment icon
    def is_navbar_recruitment_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_recruitment_icon)

    # get text navbar recruitment
    def get_navbar_recruitment_text(self):
        return self.func.get_inner_text(self.navbar.navbar_recruitment)

    # is displayed navbar my info icon
    def is_navbar_my_info_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_my_info_icon)

    # get text navbar my info
    def get_navbar_my_info_text(self):
        return self.func.get_inner_text(self.navbar.navbar_my_info)

    # is displayed navbar performance icon
    def is_navbar_performance_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_performance_icon)

    # get text navbar performance
    def get_navbar_performance_text(self):
        return self.func.get_inner_text(self.navbar.navbar_performance)

    # is displayed navbar dashboard icon
    def is_navbar_dashboard_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_dashboard_icon)

    # get text navbar dashboard
    def get_navbar_dashboard_text(self):
        return self.func.get_inner_text(self.navbar.navbar_dashboard)

    # is displayed navbar directory icon
    def is_navbar_directory_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_directory_icon)

    # get text navbar directory
    def get_navbar_directory_text(self):
        return self.func.get_inner_text(self.navbar.navbar_directory)

    # is displayed navbar maintenance icon
    def is_navbar_maintenance_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_maintenance_icon)

    # get text navbar maintenance
    def get_navbar_maintenance_text(self):
        return self.func.get_inner_text(self.navbar.navbar_maintenance)

    # is displayed navbar buzz icon
    def is_navbar_buzz_icon_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_buzz_icon)

    # get text navbar buzz
    def get_navbar_buzz_text(self):
        return self.func.get_inner_text(self.navbar.navbar_buzz)

    # click navbar toggle
    def click_navbar_toggle(self):
        self.func.click(self.navbar.navbar_toggle)

    # is displayed navbar toggle
    def is_navbar_logo_displayed(self):
        return self.func.is_displayed(self.navbar.navbar_logo)
