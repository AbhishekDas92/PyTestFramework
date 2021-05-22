import time
import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.test_getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        self.driver.implicitly_wait(5)

        ##Choose All Products and Parent-Child Tag Movement Concept Application
        checkoutPage = CheckoutPage(self.driver)
        log.info("Getting all the Cart Titles")
        Products = checkoutPage.getproductItems()
        ProductName = checkoutPage.getProductName()
        ProductButton = checkoutPage.getProductButton()

        i = -1
        for product in ProductName:
            i = i+1
            ProdName = product.text
            log.info(ProdName)
            if ProdName == "Blackberry":
                ProductButton[i].click()
                break

        # Proceed to Checkout
        firstCheckOut = checkoutPage.getCheckoutPageConfirm()
        firstCheckOut.click()

        finalCheckOut = checkoutPage.getFinalCheckoutConfirm()
        finalCheckOut.click()

        ##Confirm Page - Auto Suggestive Dropdown List

        confirmPage = ConfirmPage(self.driver)
        log.info("Entering Country Name as Ind")
        sendCountry = confirmPage.getCountry()
        sendCountry.send_keys("Ind")

        #Explicit wait - Common in Base Class
        self.verifyLinkPresenceWait("India")

        confirmPage.getSelectedCountry().click()
        confirmPage.getClickCheckBox().click()
        confirmPage.getPurchaseButton().click()

        assert self.driver.find_element_by_xpath("//input[@id='checkbox2']").is_selected()

        ##Validate Text
        print(self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)

        Sucess_Text = "Success! Thank you! Your order will be delivered in next few weeks :-)."
        log.info("Test received from Apllication is: "+Sucess_Text)
        assert "Success! Thank you" in Sucess_Text

