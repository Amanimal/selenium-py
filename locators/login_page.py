from selenium.webdriver.common.by import By


class Login:
    orange_hrm_image = (By.XPATH, "//img[@alt='company-branding']")
    login_header = (By.XPATH, "//h5[text()='Login']")
    credentials_section = (By.XPATH, "//*[@class='oxd-sheet oxd-sheet--rounded oxd-sheet--gutters "
                                     "oxd-sheet--gray-lighten-2 orangehrm-demo-credentials']")
    username_admin = (By.XPATH, "//p[text()='Username : Admin']")
    password_admin123 = (By.XPATH, "//p[text()='Password : admin123']")
    username_icon = (By.XPATH, "//i[@class='oxd-icon bi-person oxd-input-group__label-icon']")
    username_label = (By.XPATH, "//label[text()='Username']")
    username_field = (By.XPATH, "//input[@placeholder='Username']")
    password_icon = (By.XPATH, "//i[@class='oxd-icon bi-key oxd-input-group__label-icon']")
    password_label = (By.XPATH, "//label[text()='Password']")
    password_field = (By.XPATH, "//input[@placeholder='Password']")
    login_button = (By.XPATH, "//button[text()=' Login ']")
    forgot_your_password = (By.XPATH, "//p[text()='Forgot your password? ']")
    copyright_section = (By.XPATH, "//*[@class='orangehrm-copyright-wrapper']")
    linkedin_icon = (By.XPATH, "//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']")
    facebook_icon = (By.XPATH, "//a[@href='https://www.facebook.com/OrangeHRM/']")
    twitter_icon = (By.XPATH, "//a[@href='https://twitter.com/orangehrm?lang=en']")
    youtube_icon = (By.XPATH, "//a[@href='https://www.youtube.com/c/OrangeHRMInc']")
    invalid_credentials = (By.XPATH, "//p[text()='Invalid credentials']")
