from selenium.webdriver.common.by import By


class Home:
    dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
    profile_section = (By.XPATH, "//*[@class='oxd-userdropdown-tab']")
    profile_pic = (By.XPATH, "//*[@class='oxd-userdropdown-tab']//img[@alt='profile picture']")
    profile_name = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    profile_menu = (By.XPATH, "//*[@class='oxd-dropdown-menu']")
    menu_about = (By.XPATH, "//a[text()='About']")
    menu_support = (By.XPATH, "//a[text()='Support']")
    menu_change_password = (By.XPATH, "//a[text()='Change Password']")
    menu_logout = (By.XPATH, "//a[text()='Logout']")

    # ========== Dashboard Cards ==========
    time_at_work = (By.XPATH, "//p[text()='Time at Work']")
    my_actions = (By.XPATH, "//p[text()='My Actions']")
    quick_launch = (By.XPATH, "//p[text()='Quick Launch']")
    buzz_latest_posts = (By.XPATH, "//p[text()='Buzz Latest Posts']")
    employees_on_leave_today = (By.XPATH, "//p[text()='Employees on Leave Today']")
    employees_distribution_by_sub_unit = (By.XPATH, "//p[text()='Employee Distribution by Sub Unit']")
    employees_distribution_by_location = (By.XPATH, "//p[text()='Employee Distribution by Location']")
