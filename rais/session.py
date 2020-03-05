__author__ = 'v.denisov'
from rais.client_reguest import ClientReguest as cr
from rais.parameter_initialization import ParameterInitialization as pi
#from rais.config_host import ConfigHost as config

class SessionHelper:

    def __init__(self):
        pass

    def logout(self):
        pass

    @classmethod
    def login(self, username, password, profiles_cookie, language):
        response = cr.get(url=pi.get_url_host()+'/get_rsid')
        for cookie in response.cookies:
            if cookie.name in 'rsid':
                cookie_domain=cookie.domain
                break
        cookies_jar = response.cookies
        cookies_jar.set('profile', profiles_cookie, domain=cookie_domain)
        pi.set_cookies(cookies_jar)

        data = {
            "login": username,
            "pass" : password,
            "lang" : language
        }
        response_login = cr.post(url=pi.get_url_host() + '/interface/orange/user/login', data=data)
        print('response_login=', response_login.json())



