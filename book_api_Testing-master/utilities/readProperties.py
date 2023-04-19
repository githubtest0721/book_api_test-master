import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfig():
    @staticmethod
    def getBaseURL():
        baseUrl = config.get('common info', 'baseURL')
        return baseUrl

    @staticmethod
    def getUrlStatus():
        status = config.get('common info', 'status')
        return status

    @staticmethod
    def getAuth():
        auth = config.get('common info', 'auth')
        return auth
