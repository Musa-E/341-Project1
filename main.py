#
# header comment! Overview, name, etc.
#

import sqlite3
import string
import matplotlib.pyplot as plt


''' ################################################################## 
#
# search_Station
#
# Search for the given station name in the database.
# If mode == 0 , enables exact general search term only
# If mode == 1 , enables partial general search
# If mode == 2 , returns the station_ID
# '''
def search_Station(dbConn, searchStation, mode):
    dbCursor = dbConn.cursor()

    # print("\nSearching for " + searchStation + " in database...\n")

    # Search database for station and order them alphabetically
    if (mode == 0):  # Exact matches only
        dbCursor.execute("SELECT Station_Name FROM Stations WHERE Stations.Station_Name = ? ORDER BY Stations.Station_Name ASC;", (searchStation,))
    
    elif (mode == 1): # Search for station(s) using partial names
        dbCursor.execute("SELECT Station_Name, Station_ID FROM Stations WHERE Stations.Station_Name LIKE ? ORDER BY Stations.Station_Name ASC;", (searchStation,))

    elif (mode == 2): # Exact matche search for given station's ID
        dbCursor.execute("SELECT Station_ID FROM Stations WHERE Stations.Station_Name = ? ORDER BY Stations.Station_Name ASC;", (searchStation,))

    # Get the result
    rows = dbCursor.fetchall()

    # Check if any results are returned
    if (rows):

        if (mode == 0):
            # If there are matches
            for row in rows:
                found_station = row[0]
                station_ID = row[1]
                print(station_ID, ": " + found_station)
            
            return [row[0] for row in rows]
        
        elif (mode == 1):
            # If there are matches
            for row in rows:
                found_station = row[0]
                station_ID = row[1]
                print(station_ID, ": " + found_station)
            
            return [row[0] for row in rows]

        # print("\nNumber of matching stations: ", len(rows))
        elif (mode == 2):
            
            for row in rows:
                station_ID = row[0]
                # print(station_ID, ": " + searchStation)

            return [row[0] for row in rows]
        
    else:
        # If no match is found, handle it
        # print("Station not found in the database.")
        return None
    
    # End search_Station()



''' ################################################################## 
#
# partial_Name_Search
#
# Search for the given partial station name in the database
# Output station names in ascending order. If no stations are 
# found, print a message indicating that no stations were found.
# '''
def partial_Name_Search(dbConn):

    # Get input from user
    query = input("Enter partial station name (wildcards _ and %): ")

    # Call search_Station() function
    result = search_Station(dbConn, query, 1)

    if (result == None):
        print("**No stations found...")

    print() # Formatting

    # End partial_Name_Search()


''' ################################################################## 
#
# station_Search_Percentages
#
# Search for the given *exact* station name in the database
# Output station names in ascending order. If no stations are 
# found, print a message indicating that no stations were found.
# Finds the percentage of riders on weekdays, on Saturdays, and on
# Sundays/holidays for that station. Percentage calculated out of 
# the total number of riders for that station. Displays both the 
# totals and the percentages.
# '''
def station_Search_Percentages(dbConn):
    
    # Get input from user
    query = input("Enter the name of the station you would like to analyze: ")

    # Call search_Station() function to find the station's ID
    stationID = search_Station(dbConn, query, 2)

    if (stationID == None):
        print("**No data found...\n")
        return None
    
    # Get the station ID from the list
    stationID = stationID[0]

    dbCursor = dbConn.cursor()

    # Query for weekday riders
    dbCursor.execute("SELECT SUM(Num_Riders) AS Weekday_Rider_Sum FROM Ridership WHERE Type_of_Day = 'W' AND station_ID = ?;", (stationID,))
    weekdayRidersQuery = dbCursor.fetchone()

    # Query for total riders
    dbCursor.execute("SELECT SUM(Num_Riders) AS Total_Rider_Sum FROM Ridership WHERE station_ID = ?;", (stationID,))
    totalRidersQuery = dbCursor.fetchone()

    # Query for sunday riders
    dbCursor.execute("SELECT SUM(Num_Riders) AS Saturday FROM Ridership WHERE Type_of_Day = 'A' AND station_ID = ?;", (stationID,))
    saturdayRidersQuery = dbCursor.fetchone()

    # Query for saturday riders
    dbCursor.execute("SELECT SUM(Num_Riders) AS Sunday_Rider_Sum FROM Ridership WHERE Type_of_Day = 'U' AND station_ID = ?;", (stationID,))    
    sundayRidersQuery = dbCursor.fetchone()

    # Check if any results are returned
    if weekdayRidersQuery and totalRidersQuery and sundayRidersQuery and saturdayRidersQuery:

        # Get the results from the queries
        weekdayRiders = weekdayRidersQuery[0]
        totalRiders = totalRidersQuery[0]
        sundayRiders = sundayRidersQuery[0]
        saturdayRiders = saturdayRidersQuery[0]

        # Calculate the percentage
        weekDayRiderPercent = (weekdayRiders/totalRiders) * 100
        sundayRidersPercent = (sundayRiders/totalRiders) * 100
        saturdayRidersPercent = (saturdayRiders/totalRiders) * 100

        # Print or use the results as needed
        print(f"Weekday Ridership: ", f"{weekdayRiders:,}", f"({weekDayRiderPercent:.2f}%)")
        print(f"Saturday ridership: {saturdayRiders:,}", f"({saturdayRidersPercent:.2f}%)") 
        print(f"Sunday/holiday ridership: {sundayRiders:,}", f"({sundayRidersPercent:.2f}%)") 
        print(f"Total Ridership: {totalRiders:,}")

    # Get the result
    rows = dbCursor.fetchone()
    
    print() # Formatting

    # End station_Search_Percentages()


''' ##################################################################  
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
# '''
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
    if (row):
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

    # End print_stats()



''' ##################################################################  
#
# commandDriver
#
# This handles calling the relevant functions/processes based on the input
# from the user.
# '''
def commandDriver(userChoice, dbConn):
    
    # If the input is 1-9, execute the relevant processes
    if (userChoice == '1'):
        partial_Name_Search(dbConn)

    elif (userChoice == '2'):
        station_Search_Percentages(dbConn)

    elif (userChoice == '3'):
        print("Chose command 3 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif (userChoice == '4'):
        print("Chose command 4 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif (userChoice == '5'):
        print("Chose command 5 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif (userChoice == '6'):
        print("Chose command 6 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif (userChoice == '7'):
        print("Chose command 7 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif (userChoice == '8'):
        print("Chose command 8 - Not Yet Implemented.\nExiting...\n")
        exit(0)

    elif (userChoice == '9'):
        print("Chose command 9 - Not Yet Implemented.\nExiting...\n")
        exit(0)
    
    # If the user wants to exit
    elif (userChoice == 'x'):
        print("\nExiting...")
        exit(0)
    
    # Enable to accept capital X as an exit command
    # elif (userChoice == 'X'):
    #     print("\nExiting...")
    #     exit(0)

    # A valid command must be entered to continue the program
    else:
        print("**Error, unknown command, try again...")
        userChoice = input("\nPlease enter a command (1-9, x to exit): ")
        commandDriver(userChoice, dbConn)

    # End commandDriver()


''' ##################################################################  
#
# main
# '''
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

    # End main()

#
# done
#

main()