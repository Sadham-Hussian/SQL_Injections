from flask import Flask, request
import db

app = Flask(__name__)

@app.route('/')
def hello_world():
	db_conn = db.get_database_connection()

	with db_conn.cursor() as cursor:
		print("db connected")
	return 'Hello, World!'