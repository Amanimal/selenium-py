from locators.home_page import Home
from page_objects.functions import Functions


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.func = Functions(self.driver)
        self.home = Home()

    # get text dashboard header
    def get_dashboard_header_text(self):
        return self.func.get_inner_text(self.home.dashboard_header)

    # is displayed profile section
    def is_profile_section_displayed(self):
        return self.func.is_displayed(self.home.profile_section)

    # is displayed profile pic
    def is_profile_pic_displayed(self):
        return self.func.is_displayed(self.home.profile_pic)

    # is displayed profile name
    def is_profile_name_displayed(self):
        return self.func.is_displayed(self.home.profile_name)

    # click profile section
    def click_profile_section(self):
        self.func.click(self.home.profile_section)

    # is displayed profile menu
    def is_profile_menu_displayed(self):
        return self.func.is_displayed(self.home.profile_menu)

    # get text menu about
    def get_menu_about_text(self):
        return self.func.get_inner_text(self.home.menu_about)

    # get text menu support
    def get_menu_support_text(self):
        return self.func.get_inner_text(self.home.menu_support)

    # get text menu change password
    def get_menu_change_password_text(self):
        return self.func.get_inner_text(self.home.menu_change_password)

    # get text menu logout
    def get_menu_logout_text(self):
        return self.func.get_inner_text(self.home.menu_logout)

    # click menu about
    def click_menu_logout(self):
        self.func.click(self.home.menu_logout)

    # get text time at work
    def get_time_at_work_text(self):
        return self.func.get_inner_text(self.home.time_at_work)

    # get text my actions
    def get_my_actions_text(self):
        return self.func.get_inner_text(self.home.my_actions)

    # get text quick launch
    def get_quick_launch_text(self):
        return self.func.get_inner_text(self.home.quick_launch)

    # get text buzz latest posts
    def get_buzz_latest_posts_text(self):
        return self.func.get_inner_text(self.home.buzz_latest_posts)

    # get text employees on leave today
    def get_employees_on_leave_today_text(self):
        return self.func.get_inner_text(self.home.employees_on_leave_today)

    # get text employees distribution by sub unit
    def get_employees_distribution_by_sub_unit_text(self):
        return self.func.get_inner_text(self.home.employees_distribution_by_sub_unit)

    # get text employees distribution by location
    def get_employees_distribution_by_location_text(self):
        return self.func.get_inner_text(self.home.employees_distribution_by_location)
