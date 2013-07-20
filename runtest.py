import os
import subprocess
os.environ['DIAG_CONFIG_MODULE'] = 'config.test'
subprocess.call(['nosetests', '--nocapture'])


#import nose
#nose.run()
