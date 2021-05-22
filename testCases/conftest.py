import pytest
from selenium import webdriver

#Initialie run time varaible - for opting chrome or firefox or IE
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="H:\\Automation_Testing-Python\\Drivers\\chromedriver.exe")
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path="H:\\Automation_Testing-Python\\Drivers\\geckodriver.exe")
    else:
        print("Invalid Input")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver      #To return driver object to class object of fixture - call instance object using rquest instance
    yield
    driver.close()




