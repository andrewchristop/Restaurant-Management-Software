from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector.errors import _SQLSTATE_CLASS_EXCEPTION
def reservationInsert(x1, x2, x3, x4):
    cnx =  mysql.connector.connect(host='localhost',
                                         database='dorsia',
                                         user='root',
                                         password='')
    cmd = cnx.cursor()

    add_res = ("INSERT INTO reservation "
               "(name, contact, date, time) "
               "VALUES (%s, %s, %s, %s)")

    data_res = (x1, x2, x3, x4)
    cmd.execute(add_res,data_res)

    cnx.commit()
    cmd.close()
    cnx.close()

def reservationView():
    session = mysql.connector.connect(host='localhost',
                                         database='dorsia',
                                         user='root',
                                         password='')
    
    view_session = ("SELECT * FROM reservation")
    cdn = session.cursor()
    cdn.execute(view_session)

    records = cdn.fetchall()
    for row in records:
        print()
        print("Reservation ID:", row[0],)
        print("Customer Name:", row[1])
        print("Customer Contact:", row[2])
        print("Reservation Date:", row[3])
        print("Reservation Time:", row[4], "\n")

    cdn.close()
    session.close()

def tableAssign(y1,y2):
    currentconnection = mysql.connector.connect(host='localhost',
                                         database='dorsia',
                                         user='root',
                                         password='')
    
    assign = currentconnection.cursor()
    add_tables = ("INSERT INTO tables "
               "(name, table_number) "
               "VALUES (%s, %s)")
    
    tables_append = (y1,y2)
    assign.execute(add_tables,tables_append)

    currentconnection.commit()
    assign.close()
    currentconnection.close()

def tablesView():
    session = mysql.connector.connect(host='localhost',
                                         database='dorsia',
                                         user='root',
                                         password='')
    
    view_session = ("SELECT * FROM tables")
    cdn = session.cursor()
    cdn.execute(view_session)

    records = cdn.fetchall()
    for row in records:
        print()
        print("Table ID:", row[0],)
        print("Customer Name:", row[1])
        print("Table Number:", row[2])
        print("Orders:", row[3], "\n")

    cdn.close()
    session.close()

def insertOrders(z1,z2):
    session = mysql.connector.connect(host='localhost',
                                         database='dorsia',
                                         user='root',
                                         password='')
    
    mycursor = session.cursor()
    sql = (f"UPDATE tables SET orders = '{z1}' WHERE table_id = '{z2}'") 
    mycursor.execute(sql)

    session.commit()
    mycursor.close()
    session.close()

def createAccount(y1,y2):
    session = mysql.connector.connect(host='localhost',
                                         database='dorsia',
                                         user='root',
                                         password='')

    assign = session.cursor()
    add_acct = ("INSERT INTO users "
               "(username, password) "
               "VALUES (%s, %s)")
    
    data_acct = (y1,y2)
    assign.execute(add_acct, data_acct)

    session.commit()
    assign.close()
    session.close()

