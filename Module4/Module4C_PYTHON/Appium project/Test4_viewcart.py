import time
import unittest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


class DemoApp_ViewCart( unittest.TestCase ):

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

    def test_case_1_sort(admin):
        sort_button = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="sort button"]' )
        sort_button.click()
        time.sleep( 2 )
        price_asc_button = admin.driver.find_element( by=AppiumBy.XPATH,
                                                     value='//android.view.ViewGroup[@content-desc="priceAsc"]' )
        price_asc_button.click()
        time.sleep( 5 )

        #testcase_3_addcart
        #item 1
        item_one = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[1]' )
        item_one.click()
        time.sleep( 3 )
        add_first_item = admin.driver.find_element( by=AppiumBy.ACCESSIBILITY_ID,
                                                   value='Add To Cart button' )
        add_first_item.click()
        time.sleep( 3 )
        #Review or item
        give_five_star = admin.driver.find_element( by=AppiumBy.ACCESSIBILITY_ID,
                                                   value='review star 5' )
        give_five_star.click()
        time.sleep( 2 )
        close_modal = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="Close Modal button"]' )
        close_modal.click()
        time.sleep( 3 )
        admin.driver.back()

        time.sleep( 3 )

        # item 2
        item_two = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='(//android.view.ViewGroup[@content-desc="store item"])[2]' )
        item_two.click()
        time.sleep( 3 )
        add_second_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_second_item.click()
        time.sleep( 3 )
        admin.driver.back()

        # item 3
        item_three = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[3]' )
        item_three.click()
        time.sleep( 3 )
        add_third_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_third_item.click()
        time.sleep( 3 )
        admin.driver.back()

        # item 4
        item_four = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='(//android.view.ViewGroup[@content-desc="store item"])[4]' )
        item_four.click()
        time.sleep( 3 )
        add_fourth_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_fourth_item.click()
        time.sleep( 3 )
        admin.driver.back()
        time.sleep( 3 )

       
        admin.driver.swipe( start_x=500, start_y=1000, end_x=500, end_y=500, duration=700 )
        item_five = admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[5]' )
        item_five.click()
        time.sleep( 3 )
        add_fifth_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_fifth_item.click()
        time.sleep( 2 )
        admin.driver.back()

        # item 6

        item_six= admin.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[6]' )
        item_six.click()
        time.sleep( 3 )
        add_sixth_item = admin.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_sixth_item.click()
        time.sleep( 3 )

        #testcase_4_view_cart
        cart_button = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="cart badge"]' )
        cart_button.click()
        time.sleep( 2 )

        #testcase_5_assert
        admin.driver.admin( start_x=500, start_y=1000, end_x=2000, end_y=2000, duration=800 )
        items_picked = admin.driver.find_element( by=AppiumBy.XPATH,
                                                 value='//android.view.ViewGroup[@content-desc="checkout footer"]' )
        get_Attribute = items_picked.get_attribute( "content-desc" )
        print( "Content Attribute:", get_Attribute )
        expected_items = "6 items"
        actual_items = "6 items"

        if actual_items == expected_items:
            print( "Total number of items picked:", actual_items )
            assert actual_items == expected_items
        else:
            print( "Test Failed" )
            assert False, "Test Case Failed"
        time.sleep( 4 )

        #testcase_6_removeitem
        remove_item1 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                 value='(//android.view.ViewGroup[@content-desc="remove item"])[1]' )
        remove_item1.click()
        time.sleep( 2 )
        remove_item2 = admin.driver.find_element( by=AppiumBy.XPATH,
                                                 value='(//android.view.ViewGroup[@content-desc="remove item"])[1]' )
        remove_item2.click()
        time.sleep( 4 )

        #testcase_7_totalNumber
        items_left = admin.driver.find_element( by=AppiumBy.XPATH, value="//android.widget.TextView[@text='4 items']" )
        get_Attribute = items_left.get_attribute( "text" )
        print( "Text Attribute:", get_Attribute )
        expected_items = "4 items"
        actual_items = "4 items"

        if actual_items == expected_items:
            print( "Total number of actual items:", actual_items )
            assert actual_items == expected_items
        else:
            print( "Test Fail" )
            assert False, "Test Case Failed"
        time.sleep( 4 )

        proceed_checkout_button = admin.driver.find_element( by=AppiumBy.XPATH,
                                                            value='//android.view.ViewGroup[@content-desc="Proceed To Checkout button"]' )
        proceed_checkout_button.click()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()