import time, logging, re, json
import urlparse as parse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from webcontroller.common.EventListener import EventListener
from webcontroller.common.Type import NavState

class Controller(object):


    capabilities = {
        'chrome': DesiredCapabilities.CHROME,
        'firefox': DesiredCapabilities.FIREFOX,
        'android': DesiredCapabilities.ANDROID
    }

    log_name = 'Controller'

    for browser_option in capabilities:
        capabilities[browser_option]['pageLoadStrategy'] = "none"

    def __init__(self, browser, url):
        self.logger = logging.getLogger(self.log_name)
        if 'chrome' in browser.lower():
            self.logger.info("Using a local Chrome instance")
            self._webdriver = webdriver.Chrome(
                    desired_capabilities=self.capabilities['chrome']
                )
        if 'firefox' in browser.lower():
            self.logger.info("Using a local Firefox instance")
            self._webdriver = webdriver.Firefox(
                    capabilities=self.capabilities['firefox']
                )
        if 'android' in browser.lower():
            self.logger.info("Using a locally connected Android Device")
            self._webdriver = webdriver.Remote(
                    'http://localhost:9515',
                    desired_capabilities=self.capabilities['android']
                )
        self.domain_info = parse.urlparse(url)
        self._webdriver.get(url)

    def page_parse(self):
        pass

    # def load_wait(self, clicked_element):
    #     if self.nav_state == NavState.NO_NAV:
    #         return
        
    
    def find_element(self, locator):
        """Returns the ID of the element identified by the locator string."""

        self.logger.name = self.log_name+".find_element"
        self.logger.debug("Finding element "+locator)
        command_dict = {
            'using': 'xpath',
            'value': locator
        }
        response = self.execute(
            ('POST', '/element'),
            command_dict
        )
        return response['value']['ELEMENT']

    def find_elements(self, locator):
        """Returns a list of the ID's of the elements identified by the locator string."""

        self.logger.name = self.log_name+".find_elements"
        self.logger.debug("Finding elements "+locator)
        command_dict = {
            'using': 'xpath',
            'value': locator
        }
        response = self.execute(
            ('POST', '/elements'),
            command_dict
        )['value']
        return [id_num['ELEMENT'] for id_num in response if 'ELEMENT' in id_num]

    def execute(self, command, value):
        data = json.dumps(value)
        url = self._webdriver.command_executor._url+'/session/'+self._webdriver.session_id+command[1]
        communication_method = command[0]
        return self._webdriver.command_executor._request(communication_method, url, body=data)

    def close(self):
        self._webdriver.close()