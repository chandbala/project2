from selenium.webdriver.common.by import By


class MenuSearchElements:

    def __init__(self, driver):
        self.driver = driver

        self.menu_search_xpath = "//input[@placeholder='Search']"
        self.menu_admin_xpath = "//span[contains(text(), ='Admin']"
        self.pim_element_xpath = "//span[text()= 'PIM']"
        self.dashboard_xpath = "//h6[text()= 'Dashboard']"
        self.leave_xpath = "//span[text()= 'Leave']"
        self.time_xpath = "//span[text()='Time']"
        self.recruitment_xpath = "//span[text()= 'Recruitment']"
        self.myinfo_xpath = "//span[text()= 'My Info']"
        self.directory_xpath = "//span[text()= 'Directory']"
        self.performance_xpath = "//span[text()= 'Performance']"
        self.maintenance_xpath = "//span[text()= 'Maintenance']"
        self.buzz_xpath = "//span[text()= 'Buzz']"
        self.menu_elements_xpath = "//ul[@class ='oxd-main-menu']/li/a/span"

    def sidebar_search_displayed(self):
        search_txtbox = self.driver.find_element(By.XPATH, self.menu_search_xpath)
        return search_txtbox

    def sidebar_search_textbox_click(self):
        search_textbox = self.driver.find_element(By.XPATH, self.menu_search_xpath)
        search_textbox.click()

    def menu_element_list(self):
        a = self.driver.find_elements(By.XPATH, self.menu_elements_xpath)
        return a

    def check_admin(self):
        self.driver.find_element(By.XPATH, self.menu_admin_xpath)
