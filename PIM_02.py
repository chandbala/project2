from selenium.webdriver.common.by import By


class AdminPageElements:

    def __init__(self, driver):
        self.driver = driver
        self.admin_element_xpath = "//span[text()='Admin']"
        self.user_management_xpath = "//span[text()[normalize-space() = 'User Management']] "
        self.user_xpath = "//a[text() ='Users']"
        self.user_role_dropdown_xpath = "//label[@class = 'oxd-label' and text() = 'User Role']/../following-sibling::div/div/div/*/*"
        self.user_role_dropdown_list_xpath = "//div[@role='option']"
        self.status_dropdown_xpath = "//label[@class = 'oxd-label' and text() = 'Status']/../following-sibling::div/div/div/*/*"
        self.status_dropdown_list_xpath = "//div[@role='option']"

    def click_admin(self):
        self.driver.find_element(By.XPATH, self.admin_element_xpath).click()

    def click_user_management(self):
        self.driver.find_element(By.XPATH, self.user_management_xpath).click()

    def click_user(self):
        self.driver.find_element(By.XPATH, self.user_xpath).click()

    def click_user_role_dropdown(self):
        self.driver.find_element(By.XPATH, self.user_role_dropdown_xpath).click()
        user_role_list = self.driver.find_elements(By.XPATH, self.user_role_dropdown_list_xpath)
        return user_role_list

    def click_status_dropdown(self):
          self.driver.find_element(By.XPATH, self.status_dropdown_xpath).click()
          status_list = self.driver.find_elements(By.XPATH, self.status_dropdown_list_xpath)
          return status_list