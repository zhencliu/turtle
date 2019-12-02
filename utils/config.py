import os
from configparser import ConfigParser


class Config(object):

    def __init__(self, conf):
        self.params = self.parse(conf)

    def parse(self, conf):
        cfg = ConfigParser()
        with open(conf) as fd:
            cfg.read_file(fd)
    
        cfg_dict = dict()
        for section in cfg.sections():
            cfg_dict[section] = dict()
            for item, value in cfg.items(section):
                if value is not None:
                    cfg_dict[section][item] = value
    
        return cfg_dict

    def setting(self, section):
        return self.params.get(section, dict())


if __name__ == '__main__':
    conf = Config('../arithmetic/conf.ini')
    print(conf.setting('screen'))
    print(conf.setting('control'))
    print(conf.setting('arithmetic'))
    
