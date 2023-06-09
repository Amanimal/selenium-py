## About The Project
![Software][software-screenshot]
The project implements Selenium Python framework, using Page Object Model (POM) design pattern, in order to conduct UI and Functional (System) based testing
on any client owned test environment. 

Using this project, the QA team will be responsible for:

* Verifying UI/UX design of the web application
* Validating the functionality of the web application
* Reporting the results considered to be bugs and fixes

Additionally, this project will allow the team to test the 
web application on Chrome, Edge, Firefox and Safari browsers.


### Built With
The following frameworks/languages/libraries are used to bootstrap this project.

[![Selenium][Selenium]][Selenium-url] [![Python][Python]][Python-url] [![HTML][HTML]][HTML-url] [![CSS][CSS]][CSS-url]


## Getting Started

Here gives you instructions on setting up your project locally.

1. Clone the repository 
   ````
   git clone https://github.com/Amanimal/selenium-py.git
   ````
2. Create a virtual environment inside this project, using terminal
   ````
   python -m venv env
   ````
3. Activate the virtual environment, using terminal
   ````
   ./env/Scripts/activate
   ````
4. Install packages, using terminal
   ````
   pip install -r requirements.txt
   ````
5. Ensure the project contains the following directories/files. If not, create:
   
   a. ```\reports``` directory, where generated reports are stored for all 
   tests ran on different browsers <br/>
   b. ```\logs``` directory, containing ```automation.log``` file which logs each test


## Usage

Use the information below to learn how to run this project. 

### Option 1: Open any file inside ```test_cases``` directory
Lets take ```test_login_page.py``` as an example:

1. Run each test: By clicking run ```▶``` beside a function name
   ````
   def test_001_logo_and_title(self, setup):
      self.logger.info("************Test_001_Login_Page************")
      self.logger.info("************Verify Logo and Title************")
      self.driver = setup
      self.driver.get(self.base_url)
      self.login = LoginPage(self.driver)
      ...
   ````
2. Run a range of tests: By clicking run ```▶``` beside the class name
   ````
   class Test001LoginPage:
      base_url = ReadConfig.get_application_url()
      logger = LogGen.loggen()
      ...
   ````
   #### Note: Specify which browser to run each test or a range of tests:
   
   Open the ```conftest.py``` file on Windows,

   Chrome browser:
   ````
   ...
   if browser == 'chrome':
      # ------ Headless Chrome ------
      options = ChromeOptions()
      options.headless = True
      driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
      # ------ Chrome ------
      # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   ...
   ````
   Edge browser:
   ````
   ...
   elif browser == 'edge':
      # ------ Headless Edge ------
      options = EdgeOptions()
      options.headless = True
      driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
      # ------ Edge ------
      # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
   ...
   ````
   Firefox browser:
   ````
   ...
   elif browser == 'firefox':
      # ------ Headless Firefox ------
      options = FirefoxOptions()
      options.headless = True
      driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
      # ------ Firefox ------
      # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
   ...
   ````
   On macOS, Safari browser:
   ````
   ...
   elif browser == 'safari':
      # ------ Safari ------
      # to enable safari driver on the OS use the below command
      # `safaridriver --enable`
      # https://www.selenium.dev/documentation/webdriver/getting_started/open_browser/#desktop
      driver = webdriver.Safari()
   ...
   ````

### Option 2: Run the Test Suite

Using the ```TestSuit.py``` file,

On Windows:

1. Run all tests: By clicking run ```▶```
   ````
   if __name__ == '__main__':
      browsers = ["chrome", "edge", "firefox"]
      ...
   ````
On macOS:
1. Enable safari driver, using terminal
   ````
   safaridriver --enable
   ````
2. Run all tests: By clicking run ```▶```
   ````
   if __name__ == '__main__':
      browsers = ["chrome", "edge", "firefox", 'safari']
      ...
   ````
This will run all tests inside ```test_cases``` directory, on all browsers specified.

### Happy Testing!

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[software-screenshot]: images/software.png
[Selenium]: https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=green&labelColor=black&color=black
[Selenium-url]: https://www.selenium.dev/
[Python]: https://img.shields.io/badge/Python-4B8BBE?style=for-the-badge&logo=python&logoColor=yellow&labelColor=black&color=black
[Python-url]: https://www.python.org/
[CSS]: https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=blue&labelColor=black&color=black
[CSS-url]: https://www.w3.org/Style/CSS/Overview.en.html
[HTML]: https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=orange&labelColor=black&color=black
[HTML-url]: https://www.w3schools.com/html/