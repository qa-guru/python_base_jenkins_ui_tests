import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Successful fill form")
def test_successful(setup_browser):
    driver = setup_browser
    first_name = "Alex"
    last_name = "Egorov"

    with allure.step("Open registrations form"):
        driver.get("https://demoqa.com/automation-practice-form")
        wrapper = driver.find_element(By.CSS_SELECTOR, ".practice-form-wrapper")
        assert "Student Registration Form" in wrapper.text
        driver.execute_script("$('footer').remove()")
        driver.execute_script("$('#fixedban').remove()")
        # Remove any modal/overlay that might block clicks (e.g. ads, cookie banner)
        driver.execute_script("document.querySelectorAll('.modal.show, [role=dialog]').forEach(el => el.remove());")

    with allure.step("Fill form"):
        driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys(first_name)
        driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys(last_name)
        driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("alex@egorov.com")
        driver.find_element(By.CSS_SELECTOR, "#genterWrapper").find_element(
            By.XPATH, ".//*[text()='Other']"
        ).click()
        driver.find_element(By.CSS_SELECTOR, "#userNumber").send_keys("1231231230")
        driver.find_element(By.CSS_SELECTOR, "#subjectsInput").send_keys("Maths")
        driver.find_element(By.CSS_SELECTOR, "#subjectsInput").send_keys(Keys.ENTER)
        sports_label = driver.find_element(By.CSS_SELECTOR, "#hobbiesWrapper").find_element(
            By.XPATH, ".//*[text()='Sports']"
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sports_label)
        sports_clickable = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='hobbiesWrapper']//*[text()='Sports']"))
        )
        driver.execute_script("arguments[0].click();", sports_clickable)
        driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("Some street 1")
        driver.find_element(By.CSS_SELECTOR, "#state").click()
        ncr = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='stateCity-wrapper']//*[text()='NCR']"))
        )
        driver.execute_script("arguments[0].click();", ncr)
        driver.find_element(By.CSS_SELECTOR, "#city").click()
        delhi = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='stateCity-wrapper']//*[text()='Delhi']"))
        )
        driver.execute_script("arguments[0].click();", delhi)
        driver.find_element(By.CSS_SELECTOR, "#submit").click()

    with allure.step("Check form results"):
        title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#example-modal-sizes-title-lg"))
        )
        assert "Thanks for submitting the form" in title.text
