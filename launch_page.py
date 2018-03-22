'''
THIS IS THE CLASS FILE THAT DEFINES THE FUNCTIONS THAT THE MAIN SCRIPT WILL CALL
Author: Yadvinder Chauhan
Date: 10/11/2017
'''
##################################################################################

# First we import the webdriver module from the selenium package.
# Important: Selenium Libraries should first be configured/imported for it to work.
from selenium import webdriver
class launch_pg:
    driver = webdriver.Chrome("C:\Python36\chromedriver.exe")
    def openQa6(qa6_url):
        launch_pg.driver.set_page_load_timeout(30)
        launch_pg.driver.get(qa6_url)
        launch_pg.driver.maximize_window()
        launch_pg.driver.implicitly_wait(20)


    def click_subscribe(sub_link):
        elm = launch_pg.driver.find_element_by_link_text(sub_link)
        launch_pg.driver.implicitly_wait(5)
        elm.click()
        launch_pg.driver.implicitly_wait(20)
