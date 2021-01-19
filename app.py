from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from models import db, Entity

# App object
app = Flask(__name__)        

# check relevant enviroment and load settings
if app.config["ENV"] == "production":   
    app.config.from_object("config.ProductionConfig")
    print("Production Env")
else:
    app.config.from_object("config.DevelopmentConfig")
    print("Development Env")

# initiate connection with the database
db.init_app(app)                      
# migrate data, if needed
migrate = Migrate(app, db)            


@app.route('/')
def hello_world():
    return "Hello, World!"


if __name__ == '__main__':            # run the server
    app.run(debug=True)