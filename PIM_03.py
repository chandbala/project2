from selenium.webdriver.common.by import By


class EmployeePageElements:

    def __init__(self, driver):
        self.driver = driver
        self.pim_element_xpath = "//span[text()= 'PIM']"
        self.add_employee_button_xpath = "//button[normalize-space() = 'Add']"
        self.firstname_textbox_xpath = "//input[@name ='firstName']"
        self.lastname_textbox_xpath = "//input[@name ='lastName']"
        self.upload_image_xpath = "//button[contains(@class,'employee-image-action')]"
        self.toggle_login_detail_xpath = "//div[@class ='oxd-switch-wrapper']"
        self.newuser_xpath = "//label[contains(text(), 'Username')]/parent::div/following-sibling::div/input"
        self.newpassword_xpath = "//input[@type ='password']"
        self.confirm_password_xpath = "//label[contains(text(), 'Confirm Password')]/parent::div/following-sibling::div/input"
        self.empsave_button_xpath = "//button[@type='submit']"
        self.employee_list_xpath = "//a[contains(text(),'Employee List')]"

    def pim_click(self):
        self.driver.find_element(By.XPATH, self.pim_element_xpath).click()

    def click_add_button(self):
        self.driver.find_element(By.XPATH, self.add_employee_button_xpath).click()

    def add_employee(self, addfirstname, addlastname):
        self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).send_keys(addfirstname)
        self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).send_keys(addlastname)

    def toggle_logindetail(self):
        self.driver.find_element(By.XPATH, self.toggle_login_detail_xpath).click()

    def click_newuser_textbox(self, newusername, newpassword, confirmpassword):
        self.driver.find_element(By.XPATH, self.newuser_xpath).send_keys(newusername)
        self.driver.find_element(By.XPATH, self.newpassword_xpath).send_keys(newpassword)
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(confirmpassword)

    def emp_save_button_click(self):
        self.driver.find_element(By.XPATH, self.empsave_button_xpath).click()
