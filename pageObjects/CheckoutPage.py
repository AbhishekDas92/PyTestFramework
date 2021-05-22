from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "//h4[@class='card-title']")
    productButton = (By.XPATH, "//div[@class='card-footer']")

    checkOutFirst = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    finalCheckOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getproductItems(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getProductName(self):
        return self.driver.find_elements(*CheckoutPage.productName)

    def getProductButton(self):
        return self.driver.find_elements(*CheckoutPage.productButton)

    def getCheckoutPageConfirm(self):
        return self.driver.find_element(*CheckoutPage.checkOutFirst)

    def getFinalCheckoutConfirm(self):
        return self.driver.find_element(*CheckoutPage.finalCheckOut)

