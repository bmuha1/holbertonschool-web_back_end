#!/usr/bin/env python3
"""
SQLAlchemy model User
"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
app.url_map.strict_slashes = False
AUTH = Auth()


@app.route('/', methods=['GET'])
def hello():
    """ GET /
    Return:
      - welcome message
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'])
def register():
    """ POST /users
    JSON body:
      - email
      - password
    Return:
      - user created message if success
      - 400 if email already registered
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ POST /sessions
    JSON body:
      - email
      - password
    Return:
      - logged in message if success
      - 401 if login info is incorrect
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ DELETE /sessions
    JSON body:
      - session_id
    Return:
      - destroy session and redirect to GET /
      - 403 if user doesn't exist
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    try:
        AUTH.destroy_session(user.id)
        return redirect('/')
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
