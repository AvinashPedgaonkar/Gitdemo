from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver=driver

    countryName = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    checkbox = (By.CSS_SELECTOR, "div[class*='checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "input[value='Purchase']")

    def entercountry(self):
        return self.driver.find_element(*ConfirmPage.countryName)
    #self.driver.find_element(By.LINK_TEXT, "India").click()
    def clickoncountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    #self.driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox-primary']").click()
    def clickCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
    #self.driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
    def clickPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

