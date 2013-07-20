#!~/.virtualenvs/ccenv/bin/python
import os
os.environ['DIAG_CONFIG_MODULE'] = 'config.production'

import readline
from pprint import pprint

from flask import *
from consolecraze import *

os.environ['PYTHONINSPECT'] = 'True'
