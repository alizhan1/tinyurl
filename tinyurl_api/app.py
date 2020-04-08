from flask import Flask
from flask import request
from flask import jsonify

import mysql.connector as mysql

app = Flask(__name__)

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "dbms"
)

cursor = db.cursor()
cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")



def minify(url):
    query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
    values = ("Hafeez", "hafeez")
    cursor.execute(query, values)
    db.commit()
    query = "SELECT * FROM users"
    cursor.execute(query)
    records = cursor.fetchall()


@app.route("/")
def index():
    return "Usage: http://<hostname>[:<prt>]/api/<url>"

@app.route("/api/<path:url>")
def api(url):
    qs = request.query_string.decode("utf-8")
    links = minify(url)
    return jsonify(links)

app.run(host="0.0.0.0")