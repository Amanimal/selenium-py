import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):  # This will get the value to set up method
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to set up method
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # ------ Headless Chrome ------
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        # ------ Chrome ------
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # ------ Headless Docker ------
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.headless = True
        # driver = webdriver.Remote(command_executor="127.0.0.1:4444", options=chrome_options)
    elif browser == 'edge':
        # ------ Headless Edge ------
        options = EdgeOptions()
        options.headless = True
        driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        # ------ Edge ------
        # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == 'firefox':
        # ------ Headless Firefox ------
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
        # ------ Firefox ------
        # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser == 'safari':
        # ------ Safari ------
        # to enable safari driver on the OS use the below command
        # `safaridriver --enable`
        # https://www.selenium.dev/documentation/webdriver/getting_started/open_browser/#desktop
        driver = webdriver.Safari()
    else:
        # ------ Headless Chrome ------
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        # ------ Chrome ------
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # set browser window size
    driver.set_window_size(1920, 1080)
    # maximize browser window
    driver.maximize_window()

    # return the driver object
    yield driver

    # close current browser window
    driver.close()
    # closes all the browser windows
    driver.quit()


# ######################pytest html report ###########################
# it hooks for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Selenium-Python-PageObjectModel'
    config._metadata['Software Name'] = 'OrangeHRM'
    config._metadata['Tester'] = 'QA'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)
    