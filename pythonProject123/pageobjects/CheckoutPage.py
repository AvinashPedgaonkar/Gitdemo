from selenium.webdriver.common.by import By

from pageobjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self,driver):
        self.driver=driver


    cardTitle = (By.CSS_SELECTOR, "div[class='card h-100']")

    cardFooter = (By.CSS_SELECTOR, "button[class*='btn-info']")

    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    checkoutBtn = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCardTitles(self):

        return self.driver.find_elements(*CheckoutPage.cardTitle)


    def getCardFooter(self, card):
        return card.find_element(*CheckoutPage.cardFooter)

    def clickcheckoutbutton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def clickCheckoutBTN(self):
       self.driver.find_element(*CheckoutPage.checkoutBtn).click()
       confirmPage = ConfirmPage(self.driver)
       return confirmPage