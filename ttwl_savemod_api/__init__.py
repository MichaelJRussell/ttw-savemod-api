import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    global app
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SAVE_DIR=os.environ.get('TTWL_SAVE_DIR'),
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register blueprints
    from .views import hello, ttwl_info_bp
    app.register_blueprint(hello)
    app.register_blueprint(ttwl_info_bp)

    return app
