import pymysql
import config
from flask import g

def get_database_connection(cursorclass=pymysql.cursors.DictCursor):

    if 'db_connection' not in g:
        DATABASE = config.DATABASE
        
        g.db_connection = pymysql.connect(host=DATABASE["HOST"],
                            user=DATABASE["USER"],
                            password=DATABASE["PASSWORD"],
                            db=DATABASE["NAME"],
                            charset='utf8mb4',
                            cursorclass=cursorclass)
    return g.db_connection