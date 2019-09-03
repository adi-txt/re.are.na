import flask
from flask import request
from flask_graphql import GraphQLView
from flask_cors import CORS

from pkg.models import DB_SESSION
from pkg.schema import SCHEMA
from pkg.blocks import get_random_blocks
from pkg.db import add_test_data

APP = flask.Flask('__main__')
APP.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=SCHEMA,
        graphiql=True
    )
)

@APP.before_request
def create_app():
    if request.method == 'POST':
        add_test_data()
        get_random_blocks(3, 'adi')

@APP.route('/')
def my_index():
    return flask.render_template("index.html")

@APP.teardown_appcontext
def shutdown_session(exception=None):  # pylint:disable=unused-argument
    '''
    shut down database
    '''
    DB_SESSION.remove()

if __name__ == '__main__':
    CORS(APP, resources={r'/graphql': {'origins': '*'}})
    APP.run(debug=True, use_reloader=False)
