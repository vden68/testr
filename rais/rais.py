__author__ = 'v.denisov'

from rais.parameter_initialization import ParameterInitialization as pi
from rais.session import SessionHelper as session

class Rais:

    def __init__(self):
        pass

    @classmethod
    def initialization(self, url_host, prefix):
        pi.set_url_host(url_host=url_host)
        pi.set_prefix(prefix=prefix)

    @classmethod
    def get_parameters(self):
        parameters = {
            "url_host": pi.get_url_host(),
            "prefix": pi.get_prefix()
        }
        return parameters

    @classmethod
    def login(self, username, password, profiles_cookie, language):
        session.login(username=username, password=password, profiles_cookie=profiles_cookie, language=language)
