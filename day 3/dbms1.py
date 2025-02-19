import pymysql
def connect_db():
    try:
        connection=pymysql.connect(host='localhost',port=3306,user='root',password='Ar.Saini@200',database='Aryan',charset='utf8')
        print("DB connected")
        return connection
    except:
        print("DB connection failed")
def disconnect_db(connection):
    try:
        connection.close()
        print("DB disconnected")
    except:
        print("Error while disconneting")
connection=connect_db()
if connection:
    disconnect_db(connection)