import pymysql
def connect_db():
    try:
        connection=pymysql.Connect(host='localhost',port=3306,user='root',password='Ar.Saini@2004',database='Aryan',charset='utf8')
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
def create_Table():
    connection=connect_db()
    query="create table IF NOT EXISTS persons(id int primary key auto_increment,name varchar(32) not null,gender char(1) check(gender in ('m','M','f','F')),location varchar(64),dob date);"
    cursor=connection.cursor()
    cursor.execute(query)
    cursor.close()
    print("Table created")
    disconnect_db(connection)
def read_person_details():
    name = input('Enter person name: ')
    gender = input('Enter person gender: ')[0]
    location = input('Enter person location: ')
    dob = input('Enter person date of borth(yyyy/mm/dd): ')
    return (name, gender, location, dob)
def insert_values():
    person=read_person_details()
    query="insert into persons(name,gender,location,dob)values(%s,%s,%s,%s);"
    connection=connect_db()
    cursor=connection.cursor()
    cursor.execute(query,person)
    connection.commit()
    cursor.close()
    disconnect_db(connection)
create_Table()
insert_values()
