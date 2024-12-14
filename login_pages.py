from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        self.username_textbox = (By.NAME, "username")
        self.password_textbox = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")
        
        self.dashboard = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Dashboard']")
        self.common_title = (By.XPATH, "//div[@class='oxd-topbar-header-title']")
        
        self.admin = (By.XPATH, "//li[1]//a[1]//span[1]")
        self.adminTitle = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        
        self.directory = (By.XPATH, "//span[normalize-space()='Directory']")
        self.pim = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
        self.leave = (By.XPATH, "//span[normalize-space()='Leave']")
        
    def open_page(self, url):
        self.driver.get(url)
        
    def enter_usrname(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)
        
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        
    def dashBoard_click(self):
        self.driver.find_element(*self.dashboard).click()

    def text_title(self):        
        title = self.driver.find_element(*self.common_title)
        return title.text
    
    def admin_click(self):
        self.driver.find_element(*self.admin).click()
        
    def admin_title(self):        
        title = self.driver.find_element(*self.adminTitle)
        return title.text
    
    def directory_click(self):
        self.driver.find_element(*self.directory).click()
        
    def pim_click(self):
        self.driver.find_element(*self.pim).click()

    def leave_click(self):
        self.driver.find_element(*self.leave).click()
  