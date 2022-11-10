from jira import JIRA
from flask import Flask, request, make_response

import environ

import json


app = Flask(__name__)

env = environ.Env(
    DEBUG=(bool, False),
)


@app.route('/api/v1/jira-helper/jira-event', methods=['POST'])
def print_response():
    if request.method == 'POST':
        data = request.data
        json_data = json.loads(data)
        print(json.dumps(json_data, indent=4))
        return "OK"


if __name__ == '__main__':
    app.run(debug=env("DEBUG"), host='0.0.0.0', port=8080)
