from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from GuviProject2.OrangeHRM.Pages.Precondition import LoginPage
from GuviProject2.OrangeHRM.Pages.PIM_01 import MenuSearchElements
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

    # Validate the search textbox is displaying on the Admin Home page
    def test_search_box_display(self):
        driver = self.driver
        search = MenuSearchElements(driver)
        search_textbox = search.sidebar_search_displayed()
        if search_textbox.is_displayed():
            print("Search textbox is displaying on the Home page")
        else:
            print("Search textbox is not displaying on the Home page")

    # Validate the Menu options on the side pane are displaying on the Admin Page
    def test_menu_options(self):
        driver = self.driver
        menu_list = MenuSearchElements(driver)
        menu_list.menu_element_list()
        expected_menu_list = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Buzz']
        actual_menu_list = []
        for item in menu_list.menu_element_list():
            actual_menu_list.append(item.text)
        assert expected_menu_list == actual_menu_list
        print(actual_menu_list)
        print("Menu options are displaying on the Admin Page")

    def test_search_by_lowercase(self):
        driver = self.driver
        s = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        expected_menu_list1 = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Buzz']

        for item in expected_menu_list1:
            s.send_keys(item.lower())
            assert driver.find_element(By.XPATH, "//ul[@class ='oxd-main-menu']/li/a/span").text == item
            s.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        print("search menu in lower case")

    def test_search_by_uppercase(self):
        driver = self.driver
        s = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        expected_menu_list1 = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Buzz']

        for item in expected_menu_list1:
            s.send_keys(item.upper())
            assert driver.find_element(By.XPATH, "//ul[@class ='oxd-main-menu']/li/a/span").text == item
            s.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        print("search menu in upper case")

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
