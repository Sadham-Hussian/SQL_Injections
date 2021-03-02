from flask import Flask, request, jsonify,make_response
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def hello_world():
	if request.method == "GET":
		db_conn = db.get_database_connection()
		return 'Hello, World!'

@app.route('/init_db', methods=["GET"])
def initialise_database():
	db.init_db()
	return 'Database initialised'

@app.route('/api/table/products', methods=["GET"])
def check_working():
	if request.method == "GET":
		cursor = db.get_database_connection().cursor()
		sql = "SELECT * FROM products;"
		cursor.execute(sql)
		res = cursor.fetchall()
		result = {}
		result["response"] = res
		
		return jsonify(result)

@app.route('/api/products/view_item', methods=["GET"])
def view_product():
	if request.method == "GET":
		item_name = request.args.get("item_name", None)
		db_conn = db.get_database_connection()
		sql = "SELECT * FROM products WHERE name = '" + item_name + "';" 
		cursor = db_conn.cursor()
		cursor.execute(sql)
		res = cursor.fetchall()
		db_conn.commit();
		result = {}
		result["response"] = res

		return jsonify(result)

@app.route('/api/sql_injections/products/view_item', methods=["GET"])
def view_product_sql_injections():
	if request.method == "GET":
		item_name = request.args.get("item_name", None)
		db_conn = db.get_database_connection()
		sql = "SELECT * FROM products WHERE name = '" + item_name + "';" 
		cursor = db_conn.cursor()
		cursor.executescript(sql)
		res = cursor.fetchall()
		db_conn.commit();
		result = {}
		result["response"] = res

		return jsonify(result)

@app.route('/api/users/view_user', methods=["GET"])
def view_user():
	if request.method == "GET":
		username = request.args.get("username", None)
		db_conn = db.get_database_connection()
		sql = "SELECT * FROM users WHERE username = '" + username + "';"
		cursor = db_conn.cursor()
		cursor.execute(sql)
		res = cursor.fetchall()
		db_conn.commit();
		result = {}
		result["response"] = res

		return jsonify(result)

@app.route('/api/sql_injections/users/view_user', methods=["GET"])
def view_user_sql_injections():
	if request.method == "GET":
		username = request.args.get("username", None)
		db_conn = db.get_database_connection()
		sql = "SELECT * FROM users WHERE username = '" + username + "';"
		cursor = db_conn.cursor()
		cursor.executescript(sql)
		res = cursor.fetchall()
		db_conn.commit();
		result = {}
		result["response"] = res

		return jsonify(result)

@app.route('/api/sql_injections/users/login', methods=["POST"])
def user_login():
	if request.method == "POST":
		username = request.form.get("username", None)
		password = request.form.get("password", None)
		cursor = db.get_database_connection().cursor()
		sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "';"
		cursor.execute(sql)
		res = cursor.fetchall()
		if res:
			return 'Authenticated'
		else:
			return 'Not Authenticated'

@app.route('/api/sql_injections/products/retreive', methods=["GET"])
def retreive_product():
	if request.method == "GET":
		item_name = request.args.get("item_name", None)
		cursor = db.get_database_connection().cursor()
		sql = "SELECT * FROM products WHERE name = '" + item_name + "';"
		cursor.execute(sql)
		res = cursor.fetchall()
		result = {}
		result["response"] = res

		return jsonify(result)