from configparser import ConfigParser


class ConfigFileParser:

    def __init__(self, filename=None):
        self.filename = filename
        self.cf = ConfigParser()
        self.cf.read(self.filename)

    def get_env(self, env_name):
        try:
            p = self.cf.get(env_name, 'port')
            h = self.cf.get(env_name, 'host')
            return h + ':' + p
        except Exception as e:
            return e

    def get_value(self, section, key):
        try:
            v = self.cf.get(section, key)
            return v
        except Exception as e:
            return e

    def get_all_values(self, section):
        list = []
        try:
            items = self.cf.items(section)
            for i in range(len(items)):
                list.append(items[i][1])
            return list
        except Exception as e:
            return e

if __name__ == '__main__':
    mail = ConfigFileParser(filename='D:\PycharmProjects\interfaceTest\conf\mail.cfg')
    # print(mail.get_value('mail_server', 'pwd'))
    print(mail.get_all_values('receiver'))
