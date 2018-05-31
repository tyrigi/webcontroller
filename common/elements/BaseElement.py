import logging, json
# from webcontroller.common.Type import ElementType

def _wrap_elements(result):
    if isinstance(result, list):
        return [_wrap_elements(item) for item in result]
    else:
        return 

class BaseElement(object):
    
    log_name = 'BaseElement'

    def __init__(self, element, controller):
        self._webdriver = controller._webdriver
        self._element = element
        self._controller = controller
        self.logger = logging.getLogger("Base_"+str(type(self).__name__))

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

    def click(self):
        """Clicks on the element."""
        
        self.logger.name = self.log_name+'.click'
        command_dict = {
            'script': 'arguments[0].click()',
            'args': [{'ELEMENT':self._element}]
        }
        self.logger.debug("Clicking element")
        self.execute(
            ('POST', '/execute'),
            command_dict
        )

    def get_attribute(self, attr):
        """Returns the value of the indicated attribute."""
        
        self.logger.name = self.log_name+".get_attribute"
        self.logger.debug("Getting element's "+attr+" attribute.")
        command_dict = {
            'script': 'return arguments[0].getAttribute(arguments[1])', 
            'args': [{'ELEMENT': self._element}, attr]
        }
        response = self.execute(
            ('POST', '/execute'),
            command_dict
        )
        return response['value']

    def execute(self, command, value):
        data = json.dumps(value)
        url = self._webdriver.command_executor._url+'/session/'+self._webdriver.session_id+command[1]
        communication_method = command[0]
        return self._webdriver.command_executor._request(communication_method, url, body=data)