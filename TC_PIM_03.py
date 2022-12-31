from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from GuviProject2.OrangeHRM.Pages.Precondition import LoginPage
from GuviProject2.OrangeHRM.Pages.PIM_03 import EmployeePageElements


class Pim01(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        driver = cls.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

    def test_new_user(self):
        driver = self.driver
        employee = EmployeePageElements(driver)
        employee.pim_click()
        employee.click_add_button()
        employee.add_employee('Test', 'User')
        employee.toggle_logindetail()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//label[contains(text(), 'Username')]/parent::div/following-sibling::div/input")))
        employee.click_newuser_textbox('Testuser', 'Admin*05', 'Admin*05')
        employee.emp_save_button_click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

