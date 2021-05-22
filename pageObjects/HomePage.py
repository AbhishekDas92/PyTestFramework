from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    Name = (By.CSS_SELECTOR, "input[name='name']")
    Email = (By.CSS_SELECTOR, "input[name='email']")
    checkBox = (By.XPATH, "//input[@type='checkbox']")
    genderSelect = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    clickSubmit = (By.XPATH, "//input[@type='submit']")
    AlertMessage = (By.XPATH, "//*[contains(@class,'alert-success')]")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.Name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.Email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.genderSelect)

    def Submit(self):
        return self.driver.find_element(*HomePage.clickSubmit)

    def getAlertMessage(self):
        return self.driver.find_element(*HomePage.AlertMessage)




