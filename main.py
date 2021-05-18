import time
from getpass import getpass
from datetime import datetime
from connector import*
from dbops import*
import mysql.connector


def viewReservations():
    print()
    print("======== Reservations List ========")
    reservationView()

def addReservation(inp1,inp2,inp3,inp4):
    reservationInsert(inp1, inp2, inp3, inp4)

def assignTable(inp1, inp2):
    tableAssign(inp1, inp2)

def viewTable():
    print()
    print("======= Occupied Tables ========")
    tablesView()

def addOrders(inp1, inp2):
    print()
    insertOrders(inp1,inp2)

def main():
    welcome_msg = """
     /$$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$ 
    | $$__  $$ /$$__  $$| $$__  $$ /$$__  $$|_  $$_/ /$$__  $$
    | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/  | $$  | $$  \ $$
    | $$  | $$| $$  | $$| $$$$$$$/|  $$$$$$   | $$  | $$$$$$$$
    | $$  | $$| $$  | $$| $$__  $$ \____  $$  | $$  | $$__  $$
    | $$  | $$| $$  | $$| $$  \ $$ /$$  \ $$  | $$  | $$  | $$
    | $$$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$/ /$$$$$$| $$  | $$
    |_______/  \______/ |__/  |__/ \______/ |______/|__/  |__/
    """
    
    
    print()
    local_time = time.asctime(time.localtime(time.time()))
    print("The current time is", local_time)
    print("\t \t \t Welcome to \t \t \t")
    print(welcome_msg)

    print()
    print("***Employee Login***")
    while True:
        print()
        username_input = input("Please enter your username: ")
        password_input = getpass("Please enter your password: ")

        check = mysql.connector.connect(host='localhost',
                                            database='dorsia',
                                            user='root',
                                            password='')

        find = check.cursor()
        find.execute(f"SELECT * from users WHERE username='{username_input}' AND password = '{password_input}'")

        if find.fetchall():
            print()
            print("Authorized!")
            user_input = 0
            while True:
                print()
                print("========= Command Actions =========")
                print("1. View today's reservations")
                print("2. View occupied tables/customer orders")
                print("3. Add Reservation")
                print("4. Assign customer tables")
                print("5. Add customer orders")
                print("6. Exit")
                print("===================================")
                print()
                user_input = int(input("Enter command: "))
                if user_input == 1:
                    viewReservations()
                elif user_input == 2:
                    print()
                    viewTable()
                elif user_input == 3:
                    print()
                    prompt1 = input("Please enter the name of the customer: ")
                    prompt2 = input("Please enter the customer's contact number/email: ")
                    prompt3 = input("Please enter the date the customer would like to book (YY/MM/DD): ")
                    prompt4 = input("Please enter the time the customer would like to book: ")
                    addReservation(prompt1, prompt2, prompt3, prompt4)
                    print("Reservation added!")
                elif user_input == 4:
                    print()
                    prompt1 = input("Enter customer name: ")
                    prompt2 = input("Enter table number to assign: ")
                    assignTable(prompt1,prompt2)
                    print("Table Assigned!")
                elif user_input == 5:
                    prompt1 = input("Enter the table ID (NOT number) to assign order: ")
                    prompt2 = input("Enter the customer's order: ")
                    addOrders(prompt2, prompt1)
                    print("Order Added!")
                elif user_input == 6:
                    print("You have successfully exited the program")
                    exit()
                else:
                    print("Please enter a valid input!")
        else:
            print("You have either entered the wrong credentials, or the input is empty!!")

main()