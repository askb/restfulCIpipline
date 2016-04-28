from bottle import route

@route('/<command>')
def ping(command=None):
 if command.lower() == "ping":
   return "pong!"
 else:
   return "Unknown command"

@route('/')
def main():
 return "Simple RESTfull API: curl -X GET $URL/ping"
EOF

[workstation]$ cat << EOF > project/restfullapi.wsgi
import sys

sys.path.insert(0, "/var/www/restfullapi")

import bottle
import restfullapi
application = bottle.default_app()

