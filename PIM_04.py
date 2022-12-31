from selenium.webdriver.common.by import By


class EmployeeListElements:
    def __init__(self, driver):
        self.driver = driver
        self.employee_tablist_xpath = "//div[@role ='tablist']/div/a"

    def employee_tab_list(self):
        a = self.driver.find_elements(By.XPATH, self.employee_tablist_xpath)
        return a
