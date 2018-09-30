import configparser
import os


def get_config(section='database'):
    config = configparser.ConfigParser()
    if os.getcwd() == r'C:\projects\remembot\tests':
        os.chdir('..') ##@todo setup directories better so nasty hack not needed.

    config.read('config.ini')

    # print(config.values())
    if section in config.sections():
        return config[section]
    else:
        raise Exception('Config for {} does not exist.'.format(section))