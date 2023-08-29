from flask import Flask
import os
import sys

from .utils.data_helpers.get_data import get_data
from .controllers import link_controller, quote_controller


def create_app(config=None):
    app = Flask(__name__)
    
    if config:
        app.config.from_object(config)
    
    #Werkzeug(tool) checks which process is running, so only gets data on main process.
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true' and '--fetch-data' in sys.argv:
        get_data()
        
    
    # Register blueprints, extensions, etc. here
    app.register_blueprint(link_controller.link_blueprint)
    app.register_blueprint(quote_controller.quote_blueprint)

    return app
