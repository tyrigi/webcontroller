import time, logging, re

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from webcontroller.common.EventListener import EventListener

class Controller(object):


    capabilities = {
        'chrome': DesiredCapabilities.CHROME,
        'firefox': DesiredCapabilities.FIREFOX,
        'android': DesiredCapabilities.ANDROID
    }

    for browser_option in capabilities:
        capabilities[browser_option]['pageLoadStrategy'] = "none"

    def __init__(self, browser, url):
        logger = logging.getLogger("Controller.__init__")
        if 'chrome' in browser.lower():
            logger.info("Using a local Chrome instance")
            self.browser = EventFiringWebDriver(
                webdriver.Chrome(
                    desired_capabilities=self.capabilities['chrome']
                ),
                EventListener(self)
            )
        if 'firefox' in browser.lower():
            logger.info("Using a local Firefox instance")
            self.browser = EventFiringWebDriver(
                webdriver.Firefox(
                    capabilities=self.capabilities['firefox']
                ),
                EventListener(self)
            )
        if 'android' in browser.lower():
            logger.info("Using a locally connected Android Device")
            self.browser = EventFiringWebDriver(
                webdriver.Remote(
                    'http://localhost:9515',
                    desired_capabilities=self.capabilities['android']
                ),
                EventListener(self)
            )
        domain_info = re.search(
            '(^[a-z]*)\:\/\/([A-Za-z0-9]*)\.([A-Za-z0-9]*)\.([A-Za-z0-9]*)', 
            url
        )
        site_type = domain_info.group(1)
        site_prefix = domain_info.group(2)
        site_name = domain_info.group(3)
        site_postfix = domain_info.group(4)

    def page_parse(self):
        