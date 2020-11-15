from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.secret_key = 'biopark_key'
api = Api(app)

app.run(port = 5000, debug = True)
