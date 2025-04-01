import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData import HomePageData
from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):

        log = self.getLogger()


        homepage = HomePage(self.driver)

        log.info("this is homepage test")

        homepage.getname().send_keys(getData["name"])
        log.info("name loaded is" + getData["name"])
        homepage.getemail().send_keys(getData["email"])
        homepage.getpassword().send_keys(getData["password"])
        homepage.clickcheckbox().click()

        self.selectOptionByText(homepage.selectgender(),getData["gender"])


        log.info("data loaded proeprly")

        homepage.getprofession().click()
        homepage.getdob().send_keys("05/06/1996")
        homepage.clicksubmit().click()



        #self.driver.find_element(By.CSS_SELECTOR, "div[class='form-group'] input[name='name']").send_keys("Avinash")
        #self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("avi@gmail.com")
       # self.driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("Admin@123")
        #self.driver.find_element(By.CSS_SELECTOR, "label[for='exampleCheck1']").click()

        #gender = Select(self.driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
        #gender.select_by_visible_text("Male")

        #self.driver.find_element(By.ID, "inlineRadio2").click()
        #self.driver.find_element(By.CSS_SELECTOR, "input[name='bday']").send_keys("05/06/1996")
        #self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()

        alerttext =homepage.getalert().text

        assert ("Success" in alerttext)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.HomePageData.test_HomePage_data)
    def getData(self,request):
        return request.param







