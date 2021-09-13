import mysql.connector
import config as conf

"""connected to database and created two tables"""
try:
    mydb = mysql.connector.connect(host=conf.mysql["host"],
                                   user=conf.mysql["user"], password=conf.mysql["password"],
                                   database=conf.mysql["database"])

    if mydb:
        print("successfully created")
    cur = mydb.cursor()

    query1 = "Create table Request_info(ID int AUTO_INCREMENT primary key, " \
             "First_Name varchar(30),middle_name varchar(30), Last_Name varchar(50)," \
             "dob date, gender char(30), nationality varchar(30), city varchar(30),state varchar(30)," \
             " pincode int, qualification varchar(40), salary int, " \
             "pan varchar(25), request_receive_time datetime default now())"
    query2 = "CREATE TABLE Response_Info(id int not null auto_increment primary key,request_id int," \
             "response varchar(20),reason varchar(500)," \
             "Foreign Key (request_id) References Request_Info(id))"

    cur.execute(query1)
    cur.execute(query2)
    mydb.commit()
except mysql.connector.Error as error:
    print("Something went wrong while processing: {}".format(error))


