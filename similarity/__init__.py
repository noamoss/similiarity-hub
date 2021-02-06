from flask import Flask
from flask_migrate import Migrate
from similarity.models import db
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Check relevant environment and load settings.
    if app.config['ENV'] == 'production':
        app.config.from_object('config.ProductionConfig')
        print('Production Env')
    else:
        app.config.from_object('config.DevelopmentConfig')
        print('Development Env')

    # Initiate connection with the database.
    db.init_app(app)

    # Migrate data  (if needed).
    migrate = Migrate(app, db) # noqa

    return app


app = create_app()

# Importing after the `app` definition to avoid circular dependency.
# Ignoring "flake8" errors about it.
import similarity.views # noqa: E402,F401,E261


# run the server
if __name__ == '__main__':
    app.run(debug=True)
