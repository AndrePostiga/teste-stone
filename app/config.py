# pip installed
import os

#APP configuration
#UPLOAD_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/uploads')'
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + '/uploads'

#DB configuration
MYSQL_HOST = "us-cdbr-iron-east-05.cleardb.net"
MYSQL_USER = "bd011b993abccb"
MYSQL_PASSWORD = "2bd4da8b"
MYSQL_DB = "heroku_f2b0b326ed67e14"
MYSQL_PORT = 3306


