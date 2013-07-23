import os
os.environ['DIAG_CONFIG_MODULE'] = 'config.production'

from consolecraze import app

app.run(debug=True, host='0.0.0.0', port=5000)
