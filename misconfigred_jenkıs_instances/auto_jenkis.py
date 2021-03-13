from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from  selenium.webdriver.firefox.options import Options
import re

options = Options()
options.headless = False
username = ""
password = ""
jenkins_list = open('jenkins_list.txt', 'r').readlines()
for jenkins in jenkins_list:
    jenkins = jenkins.rstrip('\n')
    print('Checking -' + jenkins)
    driver = webdriver.FirefoxDriver(options=options)
    driver.set_page_load_timeout(20)
    try:
        driver.get(jenkins)
    except:
        print('Page load timeout')
    driver.implicitly_wait(20)
    try:
        element = driver.find_element_by_id('login_field')
        element.send_keys(username)
        element = driver.find_element_by_id('password')
        element.send_keys(password)
        element = driver.find_element_by_name('commit')
        element.click()
        element = driver.find_element_by_id('js-oauth-authorize-btn')
        element.click()
    except:
        pass
    if re.findall(r'Manage\sJenkins',driver.page_source):
        print(jenkins + '= jenkins Misconfigured')
    driver.quit()

