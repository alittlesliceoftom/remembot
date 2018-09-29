import configparser
import os


def get_config(section='database'):
    config = configparser.ConfigParser()
    # print(os.path.dirname(__file__) + 'config.ini')
    # config.read(os.path.join(os.path.dirname(__file__) , 'config.ini') )
    config.read('config.ini')
    if section in config.sections():
        return config[section]
    else:
        raise Exception('Config for {} does not exist.'.format(section))