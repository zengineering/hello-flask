import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev_key",
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # load instance config if it exists (when not testing)
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load passed config (when testing)
        app.config.from_mapping(test_config)

    # make sure instance dir exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello():
        return "Hello, World!"

    from . import db
    db.init_app(app)

    return app
