from flask import Flask, request, jsonify,make_response
import db

app = Flask(__name__)


def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/')
def hello_world():
	db_conn = db.get_database_connection()

	with db_conn.cursor() as cursor:
		print("db connected")
	return 'Hello, World!'

@app.route('/api/sql_injections/union_based/detect_columns', methods=["POST","OPTIONS"])
def detect_columns():
	if request.method == "OPTIONS":
		return _build_cors_prelight_response()
	elif request.method == "POST":
		item_name = request.form.get("name")
		db_conn = db.get_database_connection()
		with db_conn.cursor() as cursor:
			sql = "SELECT * FROM products WHERE name = " + item_name + ";"
			cursor.execute(sql)
			res = cursor.fetchall()
			result = {}
			result["response"] = res
		return _corsify_actual_response(jsonify(result))