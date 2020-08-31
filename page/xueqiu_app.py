
from driver.my_driver import My_Driver
from page.main_page import MainPage


class Xueqiu_APP():
     @classmethod
     def start(cls):
         cls.driver = My_Driver.my_xueqiu_driver()
         cls.driver.implicitly_wait(10)
         return  MainPage(cls.driver)

     @classmethod
     def close(cls):
         cls.driver.quit()