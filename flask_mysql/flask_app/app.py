
from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'myuser'
app.config['MYSQL_PASSWORD'] = 'mypass'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' 

mysql = MySQL(app)


@app.route('/')
def index():
    """
    Return database content in json format
    """
    cursor = mysql.connection.cursor()
    cursor.execute("Select * FROM people_table")
    rv = cursor.fetchall()
    return jsonify(rv)


@app.route('/health')
def db_health():
    """
    Check if database is connected
    """
    health_status = {'status': 'OK'}
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("Select * FROM people_table")
    except:
        health_status['status'] = 'database is not connected'

    return jsonify(health_status)


@app.errorhandler(404)
def page_not_found(e):
    return '404', 404



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)
