# Change working directory so relative paths (and template lookup) work again
import os
os.chdir(os.path.dirname(__file__))

# ... build or import your bottle application here ...
from bottle import route, default_app, view, request, post
import bottle
import bottle_pgsql

app = bottle.Bottle()
plugin = bottle_pgsql.Plugin('dbname=web_user user=officer password=')
app.install(plugin)


@post('/')
@view('index')
def do_index(db):
    email = request.forms.get('email')
    db.execute("INSERT INTO signup_emails VALUES (%s)", (email))
    return dict(submit=True, email=email)


@route('/')
@view('index')
def index():
    return dict(submit=False, email="")


# Do NOT use bottle.run() with mod_wsgi
application = default_app()
