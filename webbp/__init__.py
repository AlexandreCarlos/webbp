#! ../env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Alexandre Carlos'
__email__ = 'alexandre.carlos@gmail.com'
__version__ = '0.1'

from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from webbp.controllers.main import main
from webbp import assets
from webbp.models import db

from webbp.extensions import (
    cache,
    assets_env,
    debug_toolbar,
    login_manager
)


def create_app(object_name, env='dev'):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. webbp.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    # register our blueprints
    app.register_blueprint(main)

    return app
