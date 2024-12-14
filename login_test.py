import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from login_pages import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    try: 
        yield driver
    finally:
        driver.quit()
    
def get_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    return driver

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #driver.maximize_window()
    
    try: 
        login_page.enter_usrname("admin")
        login_page.enter_password("admin12")
        login_page.click_login()
    
        invalid_cred = driver.find_element(By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.oxd-alert-content-text")

        expected_text = invalid_cred.text
        actual_text = "Invalid credentials"
        
        assert expected_text == actual_text, f"expected {expected_text}, but got {actual_text}"
        print("Login Test Case1-> passed: valid usrName & invalid password")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")
           
    try: 
        login_page.enter_usrname("admin1")
        login_page.enter_password("admin123")
        login_page.click_login()

        invalid_cred = driver.find_element(By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.oxd-alert-content-text")
        
        expected_text = invalid_cred.text
        actual_text = "Invalid credentials"
        
        assert expected_text == actual_text, f"expected {expected_text}, but got {actual_text}"
        print("Login Test Case2 -> passed: Invalid usrName & valid password")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")
           
    try: 
        login_page.enter_usrname("admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        expected_text = login_page.text_title() 
        actual_text = "Dashboard"
        
        assert expected_text == actual_text, f"expected {expected_text}, but got {actual_text}"
        print("Login Test Case3 -> passed: Valid usrName & password")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")

def test_All_Tabs(driver):
    login_page = LoginPage(driver)
    
    try: 
        login_page.dashBoard_click()
        expected_text = login_page.text_title()        
        actual_text = "Dashboard"
        
        assert expected_text == actual_text, f"expected {expected_text}, but got {actual_text}"
        print("All Tab Test Case1 -> passed: DashBoard Tab")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        
    try: 
        login_page.admin_click()
        expected_text = login_page.admin_title()        
        actual_text = "Admin"
        
        assert expected_text == actual_text, f"expected {expected_text}, but got {actual_text}"
        print("All Tab Test Case2 -> passed: Admin Tab")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")       
        
    try: 
        login_page.directory_click()
        expected_text = login_page.text_title()
        actual_text = "Directory"
        
        assert expected_text == actual_text, f"expected {expected_text}, but got {actual_text}"
        print("All Tab Test Case3 -> passed: Directory Tab")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        
    try: 
        login_page.pim_click()
        expected_text = login_page.text_title()
        actual_text = "PIM"
        
        assert expected_text == actual_text, f"expected {expected_text}, but got {actual_text}"
        print("All Tab Test Case4 -> passed: PIM Tab")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        
        
    try: 
        login_page.leave_click()
        expected_text = login_page.text_title()
        actual_text = "Leave"
        
        assert expected_text == actual_text, f"expected {expected_text}, but got {actual_text}"
        print("All Tab Test Case5 -> passed: Leave Tab")
        
    except AssertionError as e:
        print(f"Assertion failed: {e}")


if __name__ == "__main__":
    driver = get_driver()
    try:
        test_login(driver)
        test_All_Tabs(driver)
    finally:
        time.sleep(5)
        driver.quit()
