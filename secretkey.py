# How to generate a secret key with Python
# via http://flask.pocoo.org/docs/quickstart/

import os
print(os.urandom(16))