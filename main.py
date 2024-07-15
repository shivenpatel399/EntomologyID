import os
import base64

SECRET_ENV = os.environ['SECRET_ENV']
exec(base64.b64decode(SECRET_ENV))