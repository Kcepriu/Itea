from flask import Flask, request, Response, jsonify
from models import User
import json

app = Flask(__name__)


@app.route('/users', methods=['GET', 'POST'])

def get_user():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        print(request.json)
        serr = json.dumps(serr)


        user = User.objects.create(**request.json)
        return jsonify({'id': str(user.id),
                 'login': user.login})





app.run(debug=True)