# Change working directory so relative paths (and template lookup) work again
import os
#os.chdir(os.path.dirname(__file__))

activate_this = os.path.join('.env', 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

# ... build or import your bottle application here ...
import bottle
import bottle_pgsql
import formencode
import psycopg2
from formencode import validators
from bottle import route, default_app, view, request, post, static_file


plugin = bottle_pgsql.Plugin('dbname=web_user user=officer password=')
default_app().install(plugin)


@post('/')
def do_index(db):
    email = request.forms.get('email')
    #TODO: error handling for db call
    email_validator = validators.Email()
    if len(email_validator) == 0:
        return bottle.template(
            'index',
            submit=False,
            error_msg='Please enter an email.')
    try:
        email = email_validator.to_python(email)
    except formencode.Invalid, e:
        return bottle.template('index', submit=False, error_msg=e.msg)

    try:
        db.execute("INSERT INTO signup_emails VALUES (%s)", [email])
    except psycopg2.IntegrityError, e:
        return bottle.template(
            'index',
            submit=False,
            error_msg="Email already signed up.")
    except psycopg2.DatabaseError, e:
        return bottle.template(
            'index',
            submit=False,
            error_msg='Can not add email right now, try again later.')

    return bottle.template('index', submit=True, error_msg=None)


@route('/')
@view('index')
def index():
    return dict(submit=False, error_msg=None)

# for local debugging
#@route('/static/<filepath:path>')
#def server_static(filepath):
#    return static_file(filepath, root='static')

# Do NOT use bottle.run() with mod_wsgi
application = default_app()
