from crypt import methods
from app.database import query_data, store_data

from flask import render_template, redirect, url_for, jsonify, request
from app import app


@app.route('/index')
def index():
    return "Hello, World"


@app.route('/todos', methods=['GET', 'POST'])
def todos():
    
    if request.method == "GET":
        sql = "SELECT * FROM todo"
        q_data = query_data(sql, ())
        return jsonify(q_data)

    elif request.method == "POST":
        r_data = request.get_json()
        sql = "INSERT INTO todo (item) VALUES(%s)"
        params = (r_data["item"],)
        store_data(sql, params)
        return jsonify({"status": "success"})
    
    return jsonify({"status": "failed"})


@app.route('/todos/<id>', methods=['PUT', 'PATCH'])
def updateTodo(id):
    if request.method == "PUT":
        sql = "UPDATE todo SET item=%s WHERE id=%s"
        # get the request data
        r_data = request.get_json()
        params = (r_data["item"], id, )
        store_data(sql, params)

        return jsonify({"status": "success"})

