from flask import Flask
import mysql.connector
from mysql.connector.cursor import MySQLCursor
import os

app = Flask(__name__)

DB_Host = os.environ.get('DB_Host') or "localhost"
DB_Database = os.environ.get('DB_Database') or "mysql"
DB_User = os.environ.get('DB_User') or "root"
DB_Password = os.environ.get('DB_Password') or "root_password"


@app.route('/')
def users():
    db = mysql.connector.connect(host=DB_Host, database=DB_Database, user=DB_User, password=DB_Password, auth_plugin='mysql_native_password')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM nflteams.team_colors")

    rv = cursor.fetchall()
    return str(rv)

    cursor.close()
    db.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
