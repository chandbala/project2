from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from GuviProject2.OrangeHRM.Pages.Precondition import LoginPage
from GuviProject2.OrangeHRM.Pages.PIM_03 import EmployeePageElements
from GuviProject2.OrangeHRM.Pages.PIM_04 import EmployeeListElements


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
        employee.add_employee('Tested', 'User')
        employee.toggle_logindetail()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//label[contains(text(), 'Username')]/parent::div/following-sibling::div/input")))
        employee.click_newuser_textbox('Testeduser', 'Admin*05', 'Admin*05')
        employee.emp_save_button_click()

    def test_tabs_employeelist(self):
        driver = self.driver
        tab_list = EmployeeListElements(driver)

        tab_list.employee_tab_list()
        expected_tab_list = ['Personal Details', 'Contact Details', 'Emergency Contacts', 'Dependents', 'Immigration',
                             'Job', 'Salary', 'Tax Exemptions', 'Report-to', 'Qualifications', 'Memberships']
        actual_tab_list = []
        for item in tab_list.employee_tab_list():
            actual_tab_list.append(item.text)
        assert expected_tab_list == actual_tab_list
        print(actual_tab_list)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

