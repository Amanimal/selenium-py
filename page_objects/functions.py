import os
from pathlib import Path

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait


# https://ivantay2003.medium.com/selenium-cheat-sheet-in-python-87221ee06c83
class Functions:
    """The BasePage class holds all common functionality  across the website.
    Also provides a nice wrapper when dealing selenium functions that may
    not be easy to understand.
    """

    def __init__(self, driver):
        """This function is called everytime a new object of the base class is created"""
        self.driver = driver

    def backspace_key(self, by_locator: By, times: int, time_out_in_seconds=10):
        """Performs clear on web element whose locator is passed to it"""
        for _ in range(times):
            WebDriverWait(self.driver, time_out_in_seconds).until(
                EC.visibility_of_element_located(by_locator)).send_keys(Keys.BACKSPACE)

    def clear(self, by_locator, time_out_in_seconds=10):
        """Performs clear on web element whose locator is passed to it"""
        WebDriverWait(self.driver, time_out_in_seconds).until(EC.visibility_of_element_located(by_locator)).clear()

    def click(self, by_locator, time_out_in_seconds=10):
        """Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, time_out_in_seconds).until(EC.element_to_be_clickable(by_locator)).click()

    @staticmethod
    def check_file_download(filename):
        path = Path.home()
        return os.path.exists(path / 'Downloads' / filename)

    def enter_text(self, by_locator: By, text: str, time_out_in_seconds=10):
        """Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        WebDriverWait(self.driver, time_out_in_seconds).until(EC.visibility_of_element_located(by_locator)) \
            .send_keys(text)

    def get_aria_expanded(self, by_locator: By, time_out_in_seconds=10) -> str:
        """Take in the locator and it's attribute"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).get_attribute("aria-expanded")

    def get_aria_label(self, by_locator, time_out_in_seconds=10):
        """get aria-label on web element (icons) whose locator is passed to it"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).get_attribute("aria-label")

    def get_bg_color(self, by_locator: By, time_out_in_seconds=10) -> str:
        """Returns the hex decimal value of the background color"""
        element = WebDriverWait(self.driver, time_out_in_seconds).until(EC.visibility_of_element_located(by_locator))
        return Color.from_string(element.value_of_css_property("background-color")).hex

    def get_border_bottom_color(self, by_locator: By, time_out_in_seconds=10) -> str:
        """Take in the locator and it's attribute"""
        return Color.from_string(WebDriverWait(self.driver, time_out_in_seconds) \
                                 .until(EC.visibility_of_element_located(by_locator)) \
                                 .value_of_css_property("border-bottom-color")).hex

    def get_css_property(self, by_locator: By, attribute: str, time_out_in_seconds=10) -> str:
        """Take in the locator and it's attribute"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).value_of_css_property(attribute)

    def get_color(self, by_locator: By, time_out_in_seconds=10) -> str:
        """Returns the hex decimal value of the color"""
        element = WebDriverWait(self.driver, time_out_in_seconds).until(EC.visibility_of_element_located(by_locator))
        return Color.from_string(element.value_of_css_property("color")).hex

    def get_img_alt(self, by_locator: By, time_out_in_seconds=10) -> str:
        """Take in the locator and it's attribute"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).get_attribute("alt")

    def get_inner_text(self, by_locator, time_out_in_seconds=10) -> str:
        """Take in the by_locator and returns the elements text"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).get_attribute("innerText")

    def get_placeholder(self, by_locator, time_out_in_seconds=10):
        """get placeholder on web element whose locator is passed to it"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).get_attribute("placeholder")

    def get_style(self, by_locator, time_out_in_seconds=10):
        """get data-testid on web element (icons) whose locator is passed to it"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).get_attribute("style")

    def get_test_id(self, by_locator, time_out_in_seconds=10):
        """get data-testid on web element (icons) whose locator is passed to it"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).get_attribute("data-testid")

    def get_text(self, by_locator, time_out_in_seconds=10) -> str:
        """Take in the by_locator and returns the elements text"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).text

    def get_text_align(self, by_locator: By, time_out_in_seconds=10) -> str:
        """Returns the text-align value of the element"""
        return WebDriverWait(self.driver, time_out_in_seconds) \
            .until(EC.visibility_of_element_located(by_locator)) \
            .value_of_css_property("text-align")

    def get_text_decoration_line(self, by_locator: By, time_out_in_seconds=10) -> str:
        """Take in the locator and it's attribute"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).value_of_css_property('text-decoration-line')

    def get_text_value(self, by_locator, time_out_in_seconds=10):
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).get_attribute("value")

    def get_title(self, title: str) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_tooltip(self, by_locator: By, time_out_in_seconds=10) -> str:
        """Take in the locator and it's attribute"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).get_attribute("mattooltip")

    def hover(self, by_locator, time_out_in_seconds=10):
        action = ActionChains(self.driver)
        element = WebDriverWait(self.driver, time_out_in_seconds).until(EC.visibility_of_element_located(by_locator))
        action.move_to_element(element).perform()

    def horizontal_scroll_right(self, by_locator, time_out_in_seconds=0):
        while not self.is_displayed(by_locator, time_out_in_seconds=time_out_in_seconds):
            action = ActionChains(self.driver)
            # send keys
            action.send_keys(Keys.ARROW_RIGHT)
            # perform the operation
            action.perform()

    def horizontal_scroll_left(self, by_locator, time_out_in_seconds=0):
        while not self.is_displayed(by_locator, time_out_in_seconds=time_out_in_seconds):
            action = ActionChains(self.driver)
            action.send_keys(Keys.ARROW_LEFT)
            action.perform()

    def is_clickable(self, by_locator, time_out_in_seconds=10) -> bool:
        """Performs is_selected on web element whose locator is passed to it"""
        try:
            WebDriverWait(self.driver, time_out_in_seconds).until(EC.element_to_be_clickable(by_locator))
            return True
        except TimeoutException:
            return False

    def is_displayed(self, by_locator, time_out_in_seconds=10) -> bool:
        """Performs is _displayed on web element whose locator is passed to it"""
        try:
            return WebDriverWait(self.driver, time_out_in_seconds).until(
                EC.visibility_of_element_located(by_locator)).is_displayed()
        except TimeoutException:
            return False

    def is_enabled(self, by_locator, time_out_in_seconds=10) -> bool:
        """Performs is_enabled on web element whose locator is passed to it"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).is_enabled()

    def is_selected(self, by_locator, time_out_in_seconds=10) -> bool:
        """Performs is_selected on web element whose locator is passed to it"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).is_selected()

    def scroll_down(self, by_locator, time_out_in_seconds=0):
        while not self.is_displayed(by_locator, time_out_in_seconds=time_out_in_seconds):
            action = ActionChains(self.driver)
            action.send_keys(Keys.ARROW_DOWN)
            action.perform()
            