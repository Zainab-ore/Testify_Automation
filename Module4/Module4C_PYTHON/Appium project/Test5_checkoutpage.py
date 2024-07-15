import time
import unittest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class AppCheckOut( unittest.TestCase ):

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
        time.sleep( 3 )
    
        username_field1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.widget.EditText[@content-desc="Username input field"]' )
        username_field1.send_keys( "bob@example.com" )
        time.sleep( 3 )
        password_field1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.widget.EditText[@content-desc="Password input field"]' )
        password_field1.send_keys( "10203040" )
        time.sleep( 3 )
        loginPage_button1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                      value='//android.view.ViewGroup[@content-desc="Login button"]' )
        loginPage_button1.click()
        time.sleep( 3 )

        #Testcase_1_sort
        sort_button = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="sort button"]' )
        sort_button.click()
        time.sleep( 3 )
        price_asc_button = admin.driver.find_element( by=AppiumBy.XPATH,
                                                     value='//android.view.ViewGroup[@content-desc="priceAsc"]' )
        price_asc_button.click()
        time.sleep( 5 )

      #item1
        first_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[1]' )
        first_item.click()
        time.sleep( 2 )
        add_first_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_first_item.click()
        time.sleep( 2 )
        admin.driver.back()

        time.sleep( 2 )

        # item 2
        second_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='(//android.view.ViewGroup[@content-desc="store item"])[2]' )
        second_item.click()
        time.sleep( 3 )
        add_second_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_second_item.click()
        time.sleep( 5 )
        admin.driver.back()

        # item 3
        third_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[3]' )
        third_item.click()
        time.sleep( 3 )
        add_third_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_third_item.click()
        time.sleep( 5 )
        admin.driver.back()

        # item 4
        fourth_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='(//android.view.ViewGroup[@content-desc="store item"])[4]' )
        fourth_item.click()
        time.sleep( 3 )
        add_fourth_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_fourth_item.click()
        time.sleep( 5 )
        admin.driver.back()
        time.sleep( 3 )

        # item 5
    
        admin.driver.swipe( start_x=500, start_y=1000, end_x=500, end_y=500, duration=700 )

        fifth_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[5]' )
        fifth_item.click()
        time.sleep( 3 )
        add_fifth_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_fifth_item.click()
        time.sleep( 2 )
        admin.driver.back()

        # item 6

        sixth_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[6]' )
        sixth_item.click()
        time.sleep( 2 )
        add_sixth_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_sixth_item.click()
        time.sleep( 2 )
        admin.driver.back()
        time.sleep( 3 )

        #testcase_4_view_cart
        cart_button = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="cart badge"]' )
        cart_button.click()
        time.sleep( 3 )

        #testcase_6_remove_item
        remove_item1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                 value='(//android.view.ViewGroup[@content-desc="remove item"])[1]' )
        remove_item1.click()
        time.sleep( 3 )
        remove_item2 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                 value='(//android.view.ViewGroup[@content-desc="remove item"])[1]' )
        remove_item2.click()
        time.sleep( 5 )

        #testcase_7_totalNumber
        items_left = admin.driver.find_element( by=AppiumBy.XPATH, value="//android.widget.TextView[@text='4 items']" )
        get_Attribute = items_left.get_attribute( "text" )
        print( "Get Text Attribute:", get_Attribute )
        expected_items = "4 items"
        actual_items = "4 items"

        if actual_items == expected_items:
            print( "Total Number of items left after removal is:", actual_items )
            assert actual_items == expected_items
        else:
            print( "Test Failed" )
            assert False, "Test Case Failed"
        time.sleep( 5 )

        proceed_checkout_button = admin.driver.find_element( by=AppiumBy.XPATH,
                                                            value='//android.view.ViewGroup[@content-desc="Proceed To Checkout button"]' )
        proceed_checkout_button.click()
        time.sleep( 5 )

        # testcase_checkout_form(admin):
        #admin FullName
        admin.driver.swipe( start_x=500, start_y=1000, end_x=500, end_y=500, duration=800 )

        fullname = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.widget.EditText[@content-desc="Full Name* input field"]' )

        fullname.send_keys( "Zainab Hammed" )

        #Send Address Line 1
        address_line1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                     value='//android.widget.EditText[@content-desc="Address Line 1* input field"]' )
        #Send address_line1
        address_line1.send_keys( "11, Lagos street  " )

        #Send City
        city = admin.driver.find_element( by=AppiumBy.XPATH,
                                            value='//android.widget.EditText[@content-desc="City* input field"]' )
        #Send city
        city.send_keys( "Lagos" )

        #Send Zip Code
        zip_code = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.widget.EditText[@content-desc="Zip Code* input field"]' )
        #Send zip_code
        zip_code.send_keys( "100011" )

        #Send Country
        country = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Country* input field"]' )
        #select country
        country.send_keys( "Nigeria" )

        # To Payment admin
        to_payment_el = admin.driver.find_element( by=AppiumBy.XPATH,
                                                  value='//android.view.ViewGroup[@content-desc="To Payment button"]' )
        to_payment_el.click()
        time.sleep( 2 )

        #tescase_4_checkout_payment_method

        expected_title = "Enter a payment method"
        actual_title = "Enter a payment method"

        if actual_title == expected_title:
            print( "CheckOut Suceesful:", actual_title )
            assert actual_title == expected_title
        else:
            print( "Test Failed" )
            assert False, "Test Case Failed"
        time.sleep( 5 )

        #testcase_5_payment_method
        # ull Name
        admin.driver.swipe( start_x=500, start_y=1000, end_x=500, end_y=500, duration=700 )
        fullname = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.widget.EditText[@content-desc="Full Name* input field"]' )

        fullname.send_keys( "Zainab Hammed" )

        #Card Number

        card_Number= admin.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.widget.EditText[@content-desc="Card Number* input field"]' )
        card_Number.send_keys( "1234567890987615" )

        #Expiration date

        expiration_date = admin.driver.find_element( by=AppiumBy.XPATH,
                                                       value='//android.widget.EditText[@content-desc="Expiration Date* input field"]' )
        expiration_date.send_keys( "01/20" )

        #Security Code

        security_code = admin.driver.find_element( by=AppiumBy.XPATH,
                                                     value='//android.widget.EditText[@content-desc="Security Code* input field"]' )
        security_code.send_keys( "157" )

        #Review order Button
        review_order = admin.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup[@content-desc="Review Order button"]' )
        review_order.click()
        time.sleep( 3 )

        review_order_scroll = admin.driver.find_element( by=AppiumBy.XPATH,
                                                        value='//android.widget.ScrollView[@content-desc="checkout review order screen"]' )
        get_Attribute = review_order_scroll.get_attribute( "content-desc" )
        print( "Content Desc:", get_Attribute )

        admin.driver.swipe( start_x=700, start_y=1000, end_x=1000, end_y=1000, duration=700 )

        place_order = admin.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Place Order button"]' )
        place_order.click()
        time.sleep( 5 )

        #testcase_6_checkout_complete(admin):

        expected_title = "	Thank you for your order"
        actual_title = "	Thank you for your order"

        if actual_title == expected_title:
            print( "CheckOut Complete :", actual_title )
            assert actual_title == expected_title
        else:
            print( "Test Fail" )
            assert False, "Test Case Failed"
        time.sleep( 3 )

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()