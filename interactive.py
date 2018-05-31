import time
from selenium.webdriver.remote.command import Command
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.google.com')

base_element = browser.find_element_by_xpath('//a[@title="Google apps"]')
element = browser.execute(Command.FIND_ELEMENT, {'using':'xpath', 'value':'//div[@id="hptl"]/a'})['value']
print element
browser.execute(Command.EXECUTE_SCRIPT, {'script':'arguments[0].click()', 'args':[element]})

time.sleep(4)
#time.sleep(120)
browser.close()
