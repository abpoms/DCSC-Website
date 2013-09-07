# Change working directory so relative paths (and template lookup) work again
import os
os.chdir(os.path.dirname(__file__))

# ... build or import your bottle application here ...
from bottle import route, default_app, view, request, post
import bottle
import bottle_pgsql

plugin = bottle_pgsql.Plugin('dbname=web_user user=officer password=')
default_app().install(plugin)


@post('/')
def do_index(db):
    email = request.forms.get('email')
    #TODO: error handling for db call
    db.execute("INSERT INTO signup_emails VALUES (%s)", [email])
    return bottle.template('index', submit=True)


@route('/')
@view('index')
def index():
    return dict(submit=False)


# Do NOT use bottle.run() with mod_wsgi
application = default_app()
