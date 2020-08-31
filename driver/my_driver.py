

from appium import webdriver
from utils.my_utils import highlight_element_appium
class My_Driver():
    @classmethod
    def my_xueqiu_driver(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "LMX4C17A04007025"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        return cls.driver