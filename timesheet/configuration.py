__author__ = 'vahid'

from pymlconf import ConfigManager
from os import path, mkdir
from appdirs import user_data_dir, user_config_dir

user_data_file = path.abspath(path.join(user_data_dir(), 'timesheet', 'timesheet.sqlite'))
user_config_file = path.abspath(path.join(user_config_dir(), 'timesheetrc'))

__builtin_config__ = """
db:
  uri: sqlite:///%(data_file)s
  echo: false
""" % dict(data_file=user_data_file)


def create_config_manager():

    data_dir = path.dirname(user_data_file)
    if not path.exists(data_dir):
        mkdir(data_dir)

    return ConfigManager(__builtin_config__)