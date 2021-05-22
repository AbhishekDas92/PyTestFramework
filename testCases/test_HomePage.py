import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmisson(self, getData):
        log = self.test_getLogger()

        homePage = HomePage(self.driver)

        homePage.getName().send_keys(getData["FirstName"])
        log.info("First Name is "+getData["FirstName"])
        homePage.getEmail().send_keys(getData["Email"])
        homePage.getCheckBox().click()

        sel = Select(homePage.getGender())
        sel.select_by_visible_text(getData["gender"])

        homePage.Submit().click()

        message = homePage.getAlertMessage().text

        # Assert - It always expect condition as true
        assert 'success' in message  # substring in String
        self.driver.refresh()

    #Create a ficture which will fetch data from TestData Folder using Fixture and use here
    @pytest.fixture(params=HomePageData.getTestData("TestCase1"))
    def getData(self, request):
        return request.param
