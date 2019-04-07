from flask import Flask
from flask_restful import Api, Resource, reqparse

import json
import os
from flask import jsonify

app = Flask(__name__)
app.config["DEBUG"] = True
cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\user\\users.json', cur_path)

with open(new_path) as f:
  data = json.loads(f.read())

@app.route('/api', methods=['GET'])
def home():
    return '''<h1>User Management</h1>
<p>A prototype API for managing users.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/users/all', methods=['GET'])
def api_all():
    return jsonify(data)


app.run()