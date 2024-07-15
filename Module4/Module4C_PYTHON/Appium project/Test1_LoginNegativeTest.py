import time
import unittest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


class LoginNegativeTest( unittest.TestCase ):

    @classmethod
    def setUp(cls):
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator',
            'deviceName': 'Android',
            'app': 'C:\\Users\\oreoluwa.hammed\\Documents\\TESTIFY\\TestifyAPK\\Android-MyDemoAppRN.1.1.0.build-226.apk',
            'appPackage': 'com.saucelabs.mydemoapp.rn',
            'appActivity': '.MainActivity',
            'noSign': True
        }

        url = 'http://127.0.0.1:4723/wd/hub'

        cls.driver = webdriver.Remote( url, options=AppiumOptions().load_capabilities( cap ) )
        time.sleep( 5 )

    def testcase_1(admin):
        hamburger_icon = admin.driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='open menu' )
        hamburger_icon.click()
        login_button1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                             value='//android.view.ViewGroup[@content-desc="menu item log in"]' )
        login_button1.click()
        time.sleep( 4 )
        sername_field1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Username input field"]' )
        username_field1.send_keys( "Zainab" )
        time.sleep( 2 )
        password_field1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Password input field"]' )
        password_field1.send_keys( "Test123$" )
        time.sleep( 2 )
        loginPage_button1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                 value='//android.view.ViewGroup[@content-desc="Login button"]' )
        loginPage_button1.click()
        time.sleep( 2 )
        invalid_credentials_msg1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                        value='//android.view.ViewGroup[@content-desc="generic-error-message"]/android.widget.TextView' )
        get_Attribute1 = invalid_credentials_msg1.get_attribute( "text" )
        print( "Invalid username and invalid password:", get_Attribute1 )
        time.sleep( 2 )
        username_field1.clear()
        password_field1.clear()
        time.sleep( 5 )

        # second negative login testcase
        # Login with invalid username and valid password
   
        username_field1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Username input field"]' )
        username_field1.send_keys( "Zainab" )
        password_field1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Password input field"]' )
        password_field1.send_keys( "10203040" )
        time.sleep( 3 )
        loginPage_button1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                 value='//android.view.ViewGroup[@content-desc="Login button"]' )
        loginPage_button1.click()
        invalid_credentials_msg1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                        value='//android.view.ViewGroup[@content-desc="generic-error-message"]/android.widget.TextView' )
        get_Attribute1 = invalid_credentials_msg1.get_attribute( "text" )
        print( "Invalid username", get_Attribute1 )
        time.sleep( 3 )
        username_field1.clear()
        password_field1.clear()
        time.sleep( 2 )
       
        # third negative login test case
        # Login with valid username and invalid password
        time.sleep( 2 )

        username_field1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Username input field"]' )
        username_field1.send_keys( "bob@example.com" )
        password_field1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Password input field"]' )
        password_field1.send_keys( "++3456%+" )
        time.sleep( 3 )
        loginPage_button1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                 value='//android.view.ViewGroup[@content-desc="Login button"]' )
        loginPage_button1.click()
        invalid_credentials_msg1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                        value='//android.view.ViewGroup[@content-desc="generic-error-message"]/android.widget.TextView' )
        get_Attribute1 = invalid_credentials_msg1.get_attribute( "text" )
        print( "valid username and invalid password:", get_Attribute1 )
        time.sleep( 3 )
        username_field1.clear()
        password_field1.clear()
        time.sleep( 5 )


        # fourth negative login test case
        # Login with empty username and valid password
 
        username_field1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Username input field"]' )
        username_field1.send_keys( "" )
        password_field1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Password input field"]' )
        password_field1.send_keys( "10203040" )
        time.sleep( 3 )
        loginPage_button1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                 value='//android.view.ViewGroup[@content-desc="Login button"]' )
        loginPage_button1.click()
        time.sleep( 3 )
        invalid_credentials_msg1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Username is required"]' )
        get_Attribute1 = invalid_credentials_msg1.get_attribute( "text" )
        print( "Empty Username:", get_Attribute1 )
        print( invalid_credentials_msg1.is_displayed() )
        time.sleep( 3 )
        password_field1.clear()
        time.sleep( 5 )

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()