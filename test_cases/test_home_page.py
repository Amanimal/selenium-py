from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.common import CommonPage
from utilities.custom_logger import LogGen
from utilities.readProperties import ReadConfig


class Test002HomePage:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    def start(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)
        self.common = CommonPage(self.driver)

    def test_001_dashboard_header(self, setup):
        self.logger.info("************Test_001_Dashboard_Header************")
        self.logger.info("************Validate Dashboard Header************")
        self.start(setup=setup)
        self.common.auto_login()

        # tc-1
        assert self.home.get_dashboard_header_text() == "Dashboard", "Dashboard header text is not displayed correctly"
        self.logger.info("Dashboard header text is correctly displayed. Text: 'Homepage'")

        # tc-2
        assert self.home.is_profile_section_displayed() is True, "Profile section is not displayed"
        self.logger.info("Profile section is displayed, value: True")

        # tc-3
        assert self.home.is_profile_pic_displayed() is True, "Profile pic is not displayed"
        self.logger.info("Profile pic is displayed, value: True")

        # tc-4
        assert self.home.is_profile_name_displayed() is True, "Profile name is not displayed"
        self.logger.info("Profile name is displayed, value: True")

    def test_002_side_navbar(self, setup):
        self.logger.info("************Test_002_Side_Navbar************")
        self.logger.info("************Validate Side_Navbar************")
        self.start(setup=setup)
        self.common.auto_login()

        # tc-5
        assert self.common.is_side_navbar_displayed() is True, "Side navbar is not displayed"
        self.logger.info("Side navbar is displayed, value: True")

        # tc-6
        assert self.common.is_navbar_toggle_displayed() is True, "Navbar toggle is not displayed"
        self.logger.info("Navbar toggle is displayed, value: True")

        # tc-7
        assert self.common.is_navbar_banner_displayed() is True, "Navbar banner is not displayed"
        self.logger.info("Navbar banner is displayed, value: True")

        # tc-8
        assert self.common.is_navbar_search_icon_displayed() is True, "Navbar search icon is not displayed"
        self.logger.info("Navbar search icon is displayed, value: True")

        # tc-9
        assert self.common.is_navbar_search_field_displayed() is True, "Navbar search field is not displayed"
        self.logger.info("Navbar search field is displayed, value: True")

        # tc-10
        assert self.common.is_navbar_admin_icon_displayed() is True, "Navbar admin icon is not displayed"
        self.logger.info("Navbar admin icon is displayed, value: True")

        # tc-11
        assert self.common.get_navbar_admin_text() == "Admin", "Navbar admin text is not displayed correctly"
        self.logger.info("Navbar admin text is correctly displayed. Text: 'Admin'")

        # tc-12
        assert self.common.is_navbar_pim_icon_displayed() is True, "Navbar pim icon is not displayed"
        self.logger.info("Navbar pim icon is displayed, value: True")

        # tc-13
        assert self.common.get_navbar_pim_text() == "PIM", "Navbar pim text is not displayed correctly"
        self.logger.info("Navbar pim text is correctly displayed. Text: 'PIM'")

        # tc-14
        assert self.common.is_navbar_leave_icon_displayed() is True, "Navbar leave icon is not displayed"
        self.logger.info("Navbar leave icon is displayed, value: True")

        # tc-15
        assert self.common.get_navbar_leave_text() == "Leave", "Navbar leave text is not displayed correctly"
        self.logger.info("Navbar leave text is correctly displayed. Text: 'Leave'")

        # tc-16
        assert self.common.is_navbar_time_icon_displayed() is True, "Navbar time icon is not displayed"
        self.logger.info("Navbar time icon is displayed, value: True")

        # tc-17
        assert self.common.get_navbar_time_text() == "Time", "Navbar time text is not displayed correctly"
        self.logger.info("Navbar time text is correctly displayed. Text: 'Time'")

        # tc-18
        assert self.common.is_navbar_recruitment_icon_displayed() is True, "Navbar recruitment icon is not displayed"
        self.logger.info("Navbar recruitment icon is displayed, value: True")

        # tc-19
        assert self.common.get_navbar_recruitment_text() == "Recruitment", "Navbar recruitment text is not displayed " \
                                                                           "correctly"
        self.logger.info("Navbar recruitment text is correctly displayed. Text: 'Recruitment'")

        # tc-20
        assert self.common.is_navbar_my_info_icon_displayed() is True, "Navbar my info icon is not displayed"
        self.logger.info("Navbar my info icon is displayed, value: True")

        # tc-21
        assert self.common.get_navbar_my_info_text() == "My Info", "Navbar my info text is not displayed correctly"
        self.logger.info("Navbar my info text is correctly displayed. Text: 'My Info'")

        # tc-22
        assert self.common.is_navbar_performance_icon_displayed() is True, "Navbar performance icon is not displayed"
        self.logger.info("Navbar performance icon is displayed, value: True")

        # tc-23
        assert self.common.get_navbar_performance_text() == "Performance", "Navbar performance text is not displayed " \
                                                                           "correctly"
        self.logger.info("Navbar performance text is correctly displayed. Text: 'Performance'")

        # tc-24
        assert self.common.is_navbar_dashboard_icon_displayed() is True, "Navbar dashboard icon is not displayed"
        self.logger.info("Navbar dashboard icon is displayed, value: True")

        # tc-25
        assert self.common.get_navbar_dashboard_text() == "Dashboard", "Navbar dashboard text is not displayed " \
                                                                       "correctly"
        self.logger.info("Navbar dashboard text is correctly displayed. Text: 'Dashboard'")

        # tc-26
        assert self.common.is_navbar_directory_icon_displayed() is True, "Navbar directory icon is not displayed"
        self.logger.info("Navbar directory icon is displayed, value: True")

        # tc-27
        assert self.common.get_navbar_directory_text() == "Directory", "Navbar directory text is not displayed " \
                                                                       "correctly"
        self.logger.info("Navbar directory text is correctly displayed. Text: 'Directory'")

        # tc-28
        assert self.common.is_navbar_maintenance_icon_displayed() is True, "Navbar maintenance icon is not displayed"
        self.logger.info("Navbar maintenance icon is displayed, value: True")

        # tc-29
        assert self.common.get_navbar_maintenance_text() == "Maintenance", "Navbar maintenance text is not displayed " \
                                                                           "correctly"
        self.logger.info("Navbar maintenance text is correctly displayed. Text: 'Maintenance'")

        # tc-30
        assert self.common.is_navbar_buzz_icon_displayed() is True, "Navbar buzz icon is not displayed"
        self.logger.info("Navbar buzz icon is displayed, value: True")

        # tc-31
        assert self.common.get_navbar_buzz_text() == "Buzz", "Navbar buzz text is not displayed correctly"
        self.logger.info("Navbar buzz text is correctly displayed. Text: 'Buzz'")

        # tc-32
        self.common.click_navbar_toggle()
        self.logger.info("Navbar toggle is clicked")

        # tc-33
        assert self.common.is_navbar_logo_displayed() is True, "Navbar logo is not displayed"
        self.logger.info("Navbar logo is displayed, value: True")

    def test_003_dashboard_page(self, setup):
        self.logger.info("************Test_003_Dashboard_Page************")
        self.logger.info("************Validate Dashboard Page************")
        self.start(setup=setup)
        self.common.auto_login()

        # tc-34
        assert self.home.get_time_at_work_text() == "Time at Work", "Time at work text is not displayed correctly"
        self.logger.info("Time at work text is correctly displayed. Text: 'Time at Work'")

        # tc-35
        assert self.home.get_my_actions_text() == "My Actions", "My actions text is not displayed correctly"
        self.logger.info("My actions text is correctly displayed. Text: 'My Actions'")

        # tc-36
        assert self.home.get_quick_launch_text() == "Quick Launch", "Quick launch text is not displayed correctly"
        self.logger.info("Quick launch text is correctly displayed. Text: 'Quick Launch'")

        # tc-37
        assert self.home.get_buzz_latest_posts_text() == "Buzz Latest Posts", "Buzz latest posts text is not " \
                                                                              "displayed correctly"
        self.logger.info("Buzz latest posts text is correctly displayed. Text: 'Buzz Latest Posts'")

        # tc-38
        assert self.home.get_employees_on_leave_today_text() == "Employees on Leave Today", \
            "Employees on leave today text is not displayed correctly"
        self.logger.info("Employees on leave today text is correctly displayed. Text: 'Employees on Leave Today'")

        # tc-39
        assert self.home.get_employees_distribution_by_sub_unit_text() == "Employee Distribution by Sub Unit", \
            "Employees distribution by sub unit text is not displayed correctly"
        self.logger.info("Employees distribution by sub unit text is correctly displayed. Text: 'Employee "
                         "Distribution by Sub Unit'")

        # tc-40
        assert self.home.get_employees_distribution_by_location_text() == "Employee Distribution by Location", \
            "Employees distribution by location text is not displayed correctly"
        self.logger.info("Employees distribution by location text is correctly displayed. Text: 'Employee "
                         "Distribution by Location'")

