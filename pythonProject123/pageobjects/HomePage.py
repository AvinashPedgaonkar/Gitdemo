from selenium.webdriver.common.by import By

from pageobjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR,"div[class='form-group'] input[name='name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    checkbox = (By.CSS_SELECTOR, "label[for='exampleCheck1']")
    gendersel = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    profession = (By.ID, "inlineRadio2")
    dob = (By.CSS_SELECTOR, "input[name='bday']")
    submit = (By.CSS_SELECTOR, "input[value='Submit']")
    alert =(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    #self.driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1")
    #self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    def shopItems(self):

        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def clickcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selectgender(self):
        return self.driver.find_element(*HomePage.gendersel)

    def getprofession(self):
        return self.driver.find_element(*HomePage.profession)

    def getdob(self):
        return self.driver.find_element(*HomePage.dob)

    def clicksubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getalert(self):
        return self.driver.find_element(*HomePage.alert)



