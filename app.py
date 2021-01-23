from flask import Flask
from flask_migrate import Migrate
from models import db


# App object
app = Flask(__name__)


# check relevant environment and load settings
if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
    print('Production Env')
else:
    app.config.from_object('config.DevelopmentConfig')
    print('Development Env')


# initiate connection with the database
db.init_app(app)
# migrate data, if needed
migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# run the server
if __name__ == '__main__':
    app.run(debug=True)
