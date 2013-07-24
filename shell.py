#!~/.virtualenvs/ccenv/bin/python
import sys
import os
config = sys.argv[1]
os.environ['DIAG_CONFIG_MODULE'] = 'config.{0}'.format(config)

import readline
from pprint import pprint

from flask import *
from consolecraze import *

os.environ['PYTHONINSPECT'] = 'True'

from consolecraze.database import init_db, drop_all, db_session
