import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.CheckoutPage import CheckoutPage
from pageobjects.ConfirmPage import ConfirmPage
from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
###################AVINASH GIT####################################


###################################################
##################################
#####################
        log= self.getLogger()

        homePage = HomePage(self.driver)
        log.info("now user is on checkoutpage")
        checkoutPage = homePage.shopItems()


        #checkoutPage = CheckoutPage(self.driver)
        cards = checkoutPage.getCardTitles()
        log.info(cards)

        for card in cards:
            resultname = card.find_element(By.CSS_SELECTOR, "div h4").text
            log.info(resultname)
            if resultname == "Blackberry":
                checkoutPage.getCardFooter(card).click()


        #card.find_element(By.CSS_SELECTOR, "button[class*='btn-info']").click()
        #card.find_element(By.CSS_SELECTOR, "button[class*='btn-info']").click()
        # Proceed to the checkout page by clicking checkout buttons
        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        checkoutPage.clickcheckoutbutton().click()

        #self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()

        confirmPage = checkoutPage.clickCheckoutBTN()


        # Enter "ind" in the country field to filter for "India"

        #self.driver.find_element(By.ID, "country").send_keys("ind")

        #confirmPage = ConfirmPage(self.driver)
        country = confirmPage.entercountry().send_keys("ind")

        log.info("entering country name")

        self.verifyLinkPresence("India")


        #self.driver.find_element(By.LINK_TEXT, "India").click()

        confirmPage.clickoncountry().click()

        # Accept terms & conditions checkbox
        #self.driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox-primary']").click()

        confirmPage.clickCheckbox().click()

        # Click the purchase button
        #self.driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()

        confirmPage.clickPurchaseButton().click()

        # Capture success message and verify
        success_text = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text

        log.info("text received on pop up is" + success_text)
        assert "Success! Tha321311232nk you!" in success_text





