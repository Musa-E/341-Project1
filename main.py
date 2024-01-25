#
# header comment! Overview, name, etc.
#

import sqlite3
import string
# import matplotlib.pyplot as plt


################################################################## 
#
# search_Station
#
# Search for the given station name in the database
#
def search_Station(dbConn, searchStation):
    dbCursor = dbConn.cursor()

    # print("\nSearching for " + searchStation + " in database...\n")
    
    # Search for the stations and order them alphabetically
    dbCursor.execute("SELECT Station_Name, Station_ID FROM Stations WHERE Stations.Station_Name LIKE ? ORDER BY Stations.Station_Name ASC;", (searchStation,))

    # Get the result
    rows = dbCursor.fetchall()

    # Check if any results are returned
    if rows:
        # If there are matches
        for row in rows:
            found_station = row[0]
            station_ID = row[1]
            print(station_ID, ": " + found_station)

        # print("\nNumber of matching stations: ", len(rows))
        # You can save the results to a variable or return them as needed
        return [row[0] for row in rows]
    else:
        # If no match is found, handle it
        # print("Station not found in the database.")
        return None


################################################################## 
#
# partial_Name_Search
#
# Search for the given partial station name in the database
# Output station names in ascending order. If no stations are 
# found, print a message indicating that no stations were found.
# 
def partial_Name_Search(dbConn):

    # Get input from user
    query = input("Enter partial station name (wildcards _ and %): ")

    # Call search_Station() function
    result = search_Station(dbConn, query)

    if result == None:
        print("**No stations found...")

    print() # Formatting

    # End partial_Name_Search()


##################################################################  
#
# print_stats
#
# General Statistics:
 # of stations: 147
 # of stops: 302
 # of ride entries: 1,070,894
 # date range: 2001-01-01 - 2021-07-31
 # Total ridership: 3,377,404,512
# Given a connection to the CTA database, executes various
# SQL queries to retrieve and output basic stats.
#
def print_stats(dbConn):
    dbCursor = dbConn.cursor()
    
    print("General stats:")
    
    dbCursor.execute("Select count(*) From Stations;")
    row = dbCursor.fetchone();
    print("  # of stations:", f"{row[0]:,}")
    
    dbCursor.execute("Select count(*) From Stops;")
    row = dbCursor.fetchone();
    print("  # of stops:", f"{row[0]:,}")

    dbCursor.execute("Select count(*) From Ridership;")
    row = dbCursor.fetchone();
    print("  # of ride entries:", f"{row[0]:,}")

    dbCursor.execute("SELECT DATE(MIN(Ride_Date)) AS min_date, DATE(MAX(Ride_Date)) AS max_date FROM Ridership;")
    row = dbCursor.fetchone();

    # Check if a result is returned; prevented some file issues
    if row:
        min_date = row[0]
        max_date = row[1]

        print("  date range:", min_date, "-", max_date);
        # print(" ", min_date)
        # print(" - ", max_date)
        # return min_date, max_date
    else:
        print("No dates found in the database.")
        return None

    dbCursor.execute("SELECT SUM(Num_Riders) AS RiderCount FROM Ridership;")
    row = dbCursor.fetchone();
    print("  Total ridership:", f"{row[0]:,}")


##################################################################  
#
# commandDriver
#
# This handles calling the relevant functions/processes based on the input
# from the user.
#
def commandDriver(userChoice, dbConn):
    
    # If the input is 1-9, execute the relevant processes
    if userChoice == '1':
        partial_Name_Search(dbConn)

    elif userChoice == '2':
        print("Chose command 2 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif userChoice == '3':
        print("Chose command 3 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif userChoice == '4':
        print("Chose command 4 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif userChoice == '5':
        print("Chose command 5 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif userChoice == '6':
        print("Chose command 6 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif userChoice == '7':
        print("Chose command 7 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif userChoice == '8':
        print("Chose command 8 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif userChoice == '9':
        print("Chose command 9 - Not Yet Implemented.\nExiting...\n")
        exit(0)
    
    # If the user wants to exit
    elif userChoice == 'x':
        print("\nExiting...")
        exit(0)
    
    # Enable to accept capital X as an exit command
    # elif userChoice == 'X':
    #     print("\nExiting...")
    #     exit(0)

    # A valid command must be entered to continue the program
    else:
        print("**Error, unknown command, try again...")
        userChoice = input("\nPlease enter a command (1-9, x to exit): ")
        commandDriver(userChoice, dbConn)

    # End commandDriver()


##################################################################  
#
# main
#
def main():

    print('** Welcome to CTA L analysis app **');
    print();

    dbConn = sqlite3.connect('CTA2_L_daily_ridership.db');

    print_stats(dbConn);

    # print("\nSelect a station name to search for:")

    userChoice = input("Please enter a command (1-9, x to exit): ")
    commandDriver(userChoice, dbConn)

    # Keep looping for user input until they want to exit
    while (userChoice != 'x'):

        # Enable to accept a capital X as an exit command
        # if (userChoice == 'X'):
        #     break
    
        userChoice = input("Please enter a command (1-9, x to exit): ")
        commandDriver(userChoice, dbConn)


    
        # CHECK LECTURE SLIDES (from 1/23/2024)
        #

#
# done
#

main()