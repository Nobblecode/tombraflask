import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'helina',
    user = 'root',
    password = ''
)



mycursor = mydb.cursor(dictionary=True)


mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Person(
        ID INT NOT NULL AUTO_INCREMENT,
        first_name VARCHAR(255),
        second_name VARCHAR(255),
        gender VARCHAR(255),
        tradition VARCHAR(255),
        location VARCHAR(255),
        nationalid VARCHAR(255),
        PRIMARY KEY(ID)
        
    )
    """
)
