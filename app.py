from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from models import db, Entity


app = Flask(__name__)                   # App object

if app.config["ENV"] == "production":   # check relevant enviroment and load settings
    app.config.from_object("config.ProductionConfig")
    print("Production Env")
else:
    app.config.from_object("config.DevelopmentConfig")
    print("Development Env")

db.init_app(app)                      # initiate connection with the database
migrate = Migrate(app, db)            # migrate data, if needed

@app.route('/')
def hello_world():
    return "Hello, World!"
    
if __name__ == '__main__':            # run the server
    app.run(debug=True)