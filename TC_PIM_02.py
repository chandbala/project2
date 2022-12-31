from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from GuviProject2.OrangeHRM.Pages.Precondition import LoginPage
from GuviProject2.OrangeHRM.Pages.PIM_02 import AdminPageElements


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

    def test_admin_user_management(self):
        driver = self.driver
        admin_user_management = AdminPageElements(driver)
        admin_user_management.click_admin()
        admin_user_management.click_user_management()
        admin_user_management.click_user()
        user_role_list = admin_user_management.click_user_role_dropdown()
        expected_user_role_list = ["-- Select --", "Admin", "ESS"]
        actual_user_role_list = []
        for list_of_item in user_role_list:
            actual_user_role_list.append(list_of_item.text)
        assert expected_user_role_list == actual_user_role_list
        print("User role list:")
        print(actual_user_role_list)
        status_list = admin_user_management.click_status_dropdown()
        expected_status_list = ["-- Select --", "Enabled", "Disabled"]
        actual_status_list = []
        for list_of_item in status_list:
            actual_status_list.append(list_of_item.text)
        assert expected_status_list == actual_status_list
        print("Status list:")
        print(actual_status_list)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
