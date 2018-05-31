import logging
import socket
import string, base64

try:
    import http.client as httplib
    from urllib import request
    from urllib import parse
except ImportError:
    import httplib as httplib
    import urllib2 as request
    import urlparse as parse

class BrowserCommander(object):

    