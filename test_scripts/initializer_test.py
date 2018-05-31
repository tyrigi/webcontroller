import sys, time
sys.path.append('..')

from webcontroller.common.Controller import Controller 

browser = Controller('chrome', 'https://www.google.com')
print browser.domain_info
time.sleep(4)
browser.close()