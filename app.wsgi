#import sys
#sys.path.insert(0,'/var/www/html/int_ckrawala')

# activate_this='/root/.local/share/virtualenvs/internal_ckrawala-tVYL9fd1/bin/activate_this.py'

# with.open(activate_this)

#from flaskapp import app as application
#!/usr/bin/python 
import sys 
import logging 
logging.basicConfig(stream=sys.stderr) 
sys.path.insert(0,"/var/www/html/int_ckrawala") 
from FlaskApp import app as application 
application.secret_key = 'D1nk3s'
