# Change working directory so relative paths (and template lookup) work again
import os
os.chdir(os.path.dirname(__file__))

# ... build or import your bottle application here ...
from bottle import route, default_app, view, request, post


@route('/')
@view('index')
def index():
    return dict(submit=False)


@post('/')
@view('index')
def do_index():
    email = request.forms.get('email')
    return dict(submit=True, email=email)

# Do NOT use bottle.run() with mod_wsgi
application = default_app()
