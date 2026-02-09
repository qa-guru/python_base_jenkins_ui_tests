import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class RegistrationPage:
    URL = "https://demoqa.com/automation-practice-form"

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    SUBJECTS = (By.ID, "subjectsInput")
    HOBBIES_SPORTS = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    SUBMIT_BUTTON = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open url /automation-practice-form")
    def open(self):
        self.driver.get(self.URL)
        wrapper = self.driver.find_element(By.CSS_SELECTOR, ".practice-form-wrapper")
        assert "Student Registration Form" in wrapper.text
        self.driver.execute_script("$('footer').remove()")
        self.driver.execute_script("$('#fixedban').remove()")

    @allure.step("Fill first name field with {first_name}")
    def fill_first_name(self, first_name):
        """Fill first name field"""
        element = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        element.clear()
        element.send_keys(first_name)

    @allure.step("Fill last name field with {last_name}")
    def fill_last_name(self, last_name):
        """Fill last name field"""
        element = self.driver.find_element(*self.LAST_NAME)
        element.clear()
        element.send_keys(last_name)

    @allure.step("Fill email field with {email}")
    def fill_email(self, email):
        """Fill email field"""
        element = self.driver.find_element(*self.EMAIL)
        element.clear()
        element.send_keys(email)