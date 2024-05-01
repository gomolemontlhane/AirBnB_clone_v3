#!/usr/bin/python3
from flask import Flask
from models import storage


def create_app():
    app = Flask(__name__)
    # ... other configuration

    # Import app_views here
    from api.v1.views import app_views

    # Register blueprint
    app.register_blueprint(app_views)

    # ... other app logic

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host=os.environ.get('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.environ.get('HBNB_API_PORT', 5000)),
            threaded=True)
