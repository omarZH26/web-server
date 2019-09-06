from flask import Flask, render_template, jsonify
from bd import lista1, l
import json
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/v1/users")
def api_users():
    print(hex(id(lista1)))
    datos = lis
    return jsonify({ 'usuarios ': [dict(tupla) for tupla in datos]})

@app.route("/users/list")
def lista_users():
    print(hex(id(lis)))
    return render_template('users.html', datos=lista1)



if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4000, debug=True)