import os
os.environ['DIAG_CONFIG_MODULE'] = 'config.test'
os.system('nosetests --nocapture')


#import nose
#nose.run()
