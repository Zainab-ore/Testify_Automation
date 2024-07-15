import time
import unittest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class AppProductPage( unittest.TestCase ):

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

    def test_case_1_assert_product_page(admin):

        expected_title = "Products"
        actual_title = "Products"

        if actual_title == expected_title:
            print( "Test Passed:", actual_title )
            assert actual_title == expected_title
        else:
            print( "Test Failed" )
            assert False, "Test Case Failed"
        time.sleep( 5 )

        #testcase_2_sort
        sort_button = admin.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="sort button"]' )
        sort_button.click()
        time.sleep( 3 )
        price_asc_button = admin.driver.find_element( by=AppiumBy.XPATH,
                                                     value='//android.view.ViewGroup[@content-desc="priceAsc"]' )
        price_asc_button.click()
        print("Products successfully sorted in Ascending Order by price")
        time.sleep( 5 )

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()