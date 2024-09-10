from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def fill_form():
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome(executable_path='path_to_chromedriver')  # Replace with your ChromeDriver path
    driver.get('https://example.com/form')  # Replace with the actual form URL

    # Fill in the form fields
    driver.find_element_by_name("first_name").send_keys("John")
    driver.find_element_by_name("last_name").send_keys("Doe")
    driver.find_element_by_name("email").send_keys("johndoe@example.com")
    driver.find_element_by_name("phone").send_keys("1234567890")

    # Submit the form
    driver.find_element_by_xpath("//button[@type='submit']").click()

    # Wait for the confirmation page
    time.sleep(5)

    # Take a screenshot of the submitted form for reference
    driver.save_screenshot('screenshots/form_submission.png')

    driver.quit()

if __name__ == "__main__":
    fill_form()
