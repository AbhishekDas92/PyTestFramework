from selenium.webdriver.common.by import By


class ConfirmPage:
    
    def __init__(self, driver):
        self.driver = driver

    searchCountry = (By.XPATH, "//input[@type='text']")
    selectCountry = (By.LINK_TEXT, "India")
    clickCheckBox = (By.XPATH, "//label[@for='checkbox2']")
    clickPurchaseButton = (By.XPATH, "//input[@type='submit']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.searchCountry)

    def getSelectedCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def getClickCheckBox(self):
        return self.driver.find_element(*ConfirmPage.clickCheckBox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.clickPurchaseButton)
