import os
import sys  

scripts_path = ""
if os.uname().sysname.find("Win") > -1:
    sys.path.insert(0, os.getcwd() + "\\FlaskLiveCam_WebApp")
    scripts_path = os.getcwd() + "\\FlaskLiveCam_WebApp\\scripts"
    sys.path.insert(0, scripts_path )
else:
    sys.path.insert(0, os.getcwd() + "/FlaskLiveCam_WebApp")
    sys.path.insert(0, os.getcwd())
    scripts_path = os.getcwd() + "/FlaskLiveCam_WebApp/scripts"
    sys.path.insert(0, scripts_path)

from flask import Flask

app = Flask(__name__)
# Uses __init__.py file for app configuration
app.config.from_object('config')

from FlaskLiveCam_WebApp import views
