from flask import Flask, request
import pymysql
import json

app = Flask(__name__)

db_host = "capstonedb.ctusffklc5xg.ap-northeast-2.rds.amazonaws.com"
db_user = "admin"
db_password = "51525152"
db_name = "smartfarm"
db_port = 3306

def connect_to_db():
    return pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            port = db_port
            )

@app.route('/receive_data', methods=['POST'])
def receive_and_insert_data():
    try:
        data = request.json

        db_connection = connect_to_db()
        cursor = db_connection.cursor()

        query = "INSERT INTO basicdb (temp, humi, CO2) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['temp'], data['humi'], data['CO2']))

        db_connection.commit()
        db_connection.close()

        return 'Data received and inserted into RDS sucessfully.'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
