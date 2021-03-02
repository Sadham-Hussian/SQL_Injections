import sqlite3
import config
from flask import g, Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_database_connection():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(config.DATABASE)
	return db

def close_database_connection(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
	with app.app_context():
		db = get_database_connection()
		with app.open_resource('database_scripts/schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

		with app.open_resource('database_scripts/data.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

# def get_database_connection(cursorclass=pymysql.cursors.DictCursor):

#     if 'db_connection' not in g:
#         DATABASE = config.DATABASE
        
#         g.db_connection = pymysql.connect(host=DATABASE["HOST"],
#                             user=DATABASE["USER"],
#                             password=DATABASE["PASSWORD"],
#                             db=DATABASE["NAME"],
#                             charset='utf8mb4',
#                             cursorclass=cursorclass)
#     return g.db_connection