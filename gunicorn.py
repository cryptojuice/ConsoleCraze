import os
os.environ['DIAG_CONFIG_MODULE'] = 'config.production'

import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = '0.0.0.0:80'
proc_name = 'cc_gunicorn'
pidfile = '/tmp/cc_gunicorn.pid'
logfile = '/tmp/cc_gunicorn.log'
worker_class = 'sync'
debug = True
daemon = True
