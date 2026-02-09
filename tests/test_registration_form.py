import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.registration_page import RegistrationPage


@allure.title("Successful fill form")
def test_successful(setup_browser):
    registration_page = RegistrationPage(setup_browser)
    first_name = "Alex"
    last_name = "Egorov"

    with allure.step("Open registration form"):
        registration_page.open()

    with allure.step("Fill form"):
        registration_page.fill_first_name(first_name)
        registration_page.fill_last_name(last_name)
        registration_page.fill_email("alex@egorov.com")
        # TODO Move to pageobject
        # driver.find_element(By.CSS_SELECTOR, "#genterWrapper").find_element(
        #     By.XPATH, ".//*[text()='Other']"
        # ).click()
        # driver.find_element(By.CSS_SELECTOR, "#userNumber").send_keys("1231231230")
        # driver.find_element(By.CSS_SELECTOR, "#subjectsInput").send_keys("Maths")
        # driver.find_element(By.CSS_SELECTOR, "#subjectsInput").send_keys(Keys.ENTER)
        # sports_label = driver.find_element(By.CSS_SELECTOR, "#hobbiesWrapper").find_element(
        #     By.XPATH, ".//*[text()='Sports']"
        # )
        # driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sports_label)
        # sports_clickable = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[@id='hobbiesWrapper']//*[text()='Sports']"))
        # )
        # driver.execute_script("arguments[0].click();", sports_clickable)
        # driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("Some street 1")
        # driver.find_element(By.CSS_SELECTOR, "#state").click()
        # ncr = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[@id='stateCity-wrapper']//*[text()='NCR']"))
        # )
        # driver.execute_script("arguments[0].click();", ncr)
        # driver.find_element(By.CSS_SELECTOR, "#city").click()
        # delhi = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[@id='stateCity-wrapper']//*[text()='Delhi']"))
        # )
        # driver.execute_script("arguments[0].click();", delhi)
        # driver.find_element(By.CSS_SELECTOR, "#submit").click()

    # with allure.step("Check form results"):
    #     title = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, "#example-modal-sizes-title-lg"))
    #     )
    #     assert "Thanks for submitting the form" in title.text
