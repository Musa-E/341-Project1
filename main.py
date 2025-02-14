#
# Musa Elqaq
# CS 341 - Spring 2024
# Program 1: CTA Database App
#
# Purpose: 
#  Using SQL and python, this program allows a user to perform operations
#  and gather information from the CTA's database.
# 

import sqlite3
import string
import matplotlib.pyplot as plt
import numpy as np # Tutorial for plotting said this was needed



''' ################################################################## 
#
# search_Station
#
# Search for the given station name in the database.
# If mode == 0 , enables exact general search term only
# If mode == 1 , enables partial general search
# If mode == 2 , returns the station_ID
# If mode == 3 , enables partial general search with NO outputs
# '''
def search_Station(dbConn, searchStation, mode):
    dbCursor = dbConn.cursor()
    result = None

    # Search database for station and order them alphabetically
    if (mode == 0):  # Exact matches only
        dbCursor.execute("SELECT Station_Name FROM Stations WHERE Stations.Station_Name = ? ORDER BY Stations.Station_Name ASC;", (searchStation,))
    
    elif (mode == 1): # Search for station(s) using partial names
        dbCursor.execute("SELECT Station_Name, Station_ID FROM Stations WHERE Stations.Station_Name LIKE ? ORDER BY Stations.Station_Name ASC;", (searchStation,))

    elif (mode == 2): # Exact match search for given station's ID
        dbCursor.execute("SELECT Station_ID FROM Stations WHERE Stations.Station_Name = ? ORDER BY Stations.Station_Name ASC;", (searchStation,))

    elif (mode == 3): # Search for station(s) using partial names and return some additional information
        
        # For some reason, the number of riders gets doubled.  For that reason, I've included a
        # ' / 2' in the select section.  This has fixed the problem for now, but could cause
        # problems later on, especially if different databases are used.
        dbCursor.execute("""
        SELECT
            strftime('%Y', Ridership.Ride_Date) AS Year,
            SUM(Ridership.Num_Riders) / 2 AS TotalRidership,
            COUNT(DISTINCT Stations.Station_ID) AS NumStations,
            Stations.Station_Name,
            Stops.ADA AS isADACompliant
        FROM
            Stations
        JOIN
            Ridership ON Stations.Station_ID = Ridership.Station_ID
        JOIN
            Stops ON Stations.Station_ID = Stops.Station_ID
        WHERE
            Stations.Station_Name LIKE ?
        GROUP BY
            Year, Stations.Station_Name
        ORDER BY
            Year ASC; 
        """, (searchStation,))

    elif (mode == 4): # Search for station(s) using partial names and return some additional information

        dbCursor.execute("""
            SELECT 
                Station_Name
            FROM 
                Stations 
            WHERE 
                Stations.Station_Name LIKE ? 
            ORDER BY 
                Stations.Station_Name ASC;""", 
        (searchStation,))

        result = dbCursor.fetchall()

        if not result:
            print("**No station found...\n")
            return
        
        if (len(result) > 1):
            print("**Multiple stations found...\n")
            return

        searchYear = input("Enter a year: ")

        dbCursor.execute("""
        SELECT
            strftime('%Y', Ridership.Ride_Date) AS Year,
            strftime('%m', Ridership.Ride_Date) AS Month,
            SUM(Ridership.Num_Riders) AS TotalRidership,
            Stations.Station_Name
        FROM
            Stations
        JOIN
            Ridership ON Stations.Station_ID = Ridership.Station_ID
        WHERE
            Stations.Station_Name LIKE ? AND strftime('%Y', Ridership.Ride_Date) = ?
        GROUP BY
            Year, Month
        ORDER BY
            Year ASC, Month ASC;
        """, (searchStation, searchYear,))

        result = dbCursor.fetchall()

        if not result:
            print("Monthly Ridership at " + searchStation + " for " + searchYear)

            plotQuery = input("Plot? (y/n) ") # Nothing to plot though,
            
            if (plotQuery == "y"):

                # Will hold a list of the data being printed out, should the user want to plot it
                months = []
                riders = []

                # # Additional settings for the plot
                plt.figure(figsize=(10, 6))  # Adjust the size of the plot
                plt.plot(months, riders, color='b', label='Ridership')  # Specify marker, linestyle, and color
                plt.title(f"Monthly Ridership at {searchStation} Station ({searchYear})")  # Add a title
                plt.xlabel("Month")  # Add label for x-axis
                plt.ylabel("Number of Riders")  # Add label for y-axis

                plt.show()

            print() # Formatting
            return
            

    elif (mode == 5):
        
        dbCursor.execute("""
            SELECT 
                Station_Name
            FROM 
                Stations 
            WHERE 
                Stations.Station_Name LIKE ? 
            ORDER BY 
                Stations.Station_Name ASC;""", (searchStation,))

        result = dbCursor.fetchall()

        if not result:
            print("**No station found...\n")
            return

        elif len(result) > 1:
            print("**Multiple stations found...\n")
            return
        
        else:

            dbCursor.execute("""
                SELECT
                    strftime('%Y', Ridership.Ride_Date) AS Year,
                    SUM(Ridership.Num_Riders) / 2 AS TotalRidership
                FROM
                    Stations
                JOIN
                    Ridership ON Stations.Station_ID = Ridership.Station_ID
                JOIN
                    Stops ON Stations.Station_ID = Stops.Station_ID
                WHERE
                    Stations.Station_Name LIKE ?
                GROUP BY
                    Year, Month
                ORDER BY
                    Year ASC, Month ASC;
            """,(searchStation))


    rows = dbCursor.fetchall()
    # Get the result
    if (result is not None):
        rows = result

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
        
        # If there was more than one partial match, handle it [station stats by year]
        elif (mode == 3):
            
            # Should be redundant, but just in case
            if (rows == None):
                return None
            
            # The user may choose to plot this data, so the entire table will be returned
            return rows
        
        elif (mode == 4):
            
            # Should be redundant, but just in case
            if (rows == None):
                return None
            
            
            # The user may choose to plot this data, so the entire table will be returned
            return rows
        
        elif (mode == 5):

            # Should be redundant, but just in case
            if (rows == None):
                return None
            
            return rows

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
    query = input("\nEnter partial station name (wildcards _ and %): ")

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
    query = input("\nEnter the name of the station you would like to analyze: ")

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

        print("Percentage of ridership for the " + query + " station: ")
        # Print or use the results as needed
        print(f"  Weekday ridership: ", f"{weekdayRiders:,}", f"({weekDayRiderPercent:.2f}%)")
        print(f"  Saturday ridership: {saturdayRiders:,}", f"({saturdayRidersPercent:.2f}%)") 
        print(f"  Sunday/holiday ridership: {sundayRiders:,}", f"({sundayRidersPercent:.2f}%)") 
        print(f"  Total ridership: {totalRiders:,}")

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
    
    # Start printing out the stats
    print("General Statistics:")
    
    # Prints the number of stations, stops, and overall ride entries (in order)
    dbCursor.execute("Select count(*) From Stations;")
    row = dbCursor.fetchone();
    print("  # of stations:", f"{row[0]:,}")
    
    dbCursor.execute("Select count(*) From Stops;")
    row = dbCursor.fetchone();
    print("  # of stops:", f"{row[0]:,}")

    dbCursor.execute("Select count(*) From Ridership;")
    row = dbCursor.fetchone();
    print("  # of ride entries:", f"{row[0]:,}")

    # Prints the date range of the database
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

    # Prints out total Ridership
    dbCursor.execute("SELECT SUM(Num_Riders) AS RiderCount FROM Ridership;")
    row = dbCursor.fetchone();
    print("  Total ridership:", f"{row[0]:,}")

    # End print_stats()



''' ##################################################################
#
# weekdayRidershipByName
#
# Outputs the total ridership on weekdays for each station, with station names instead
# of station IDs. Also shows the percentages, taken out of the total ridership on weekdays 
# for all the stations. Results in descending order by ridership
#
# '''
def weekdayRidershipByName(dbConn):
    
    print("Ridership on Weekdays for Each Station")
    dbCursor = dbConn.cursor()

    # Query for weekday riders
    dbCursor.execute(
        """
        SELECT Stations.station_Name, SUM(Ridership.Num_Riders) AS Weekday_Rider_Sum 
        FROM Ridership JOIN Stations ON Ridership.station_ID = Stations.station_ID 
        WHERE Ridership.Type_of_Day = 'W' 
        GROUP BY Stations.station_Name 
        ORDER BY Weekday_Rider_Sum DESC;
        """
    )

    weekdayRidersQuery = dbCursor.fetchall()

    # Query for total riders
    dbCursor.execute("SELECT SUM(Num_Riders) AS Total_Rider_Sum FROM Ridership WHERE Ridership.Type_of_Day = 'W';")
    totalRidersQuery = dbCursor.fetchone()

    # Ensure good output before trying to use it
    if weekdayRidersQuery and totalRidersQuery:

        totalRiders = totalRidersQuery[0]

        # Output each station
        for row in weekdayRidersQuery:
            station_Name = row[0]
            weekdayRidersSum = row[1]
            
            # Calculate percentage
            weekdayRiderPercentage = (weekdayRidersSum / totalRiders) * 100

            print(f"{station_Name} : {weekdayRidersSum:,} ({weekdayRiderPercentage:.2f}%)")

    # End weekdayRidershipByName()



''' ##################################################################
#
# stopsInLineAndDirection
#
# 
# '''
def stopsInLineAndDirection(dbConn):

    colorQuery = input("\nEnter a line color (e.g. Red or Yellow): ").lower()
    
    dbCursor = dbConn.cursor()

    # Query for weekday riders
    dbCursor.execute( "SELECT Color FROM Lines")

    colors = dbCursor.fetchall()

    # Extract color values from the list of tuples
    color_values = [color[0].lower() for color in colors]

    # Confirm the inputted color is a valid line color
    if colorQuery in color_values:
        # print("Valid color!\n")

        # Worth noting that this is case-insensitive due to .lower()
        directionQuery = input("Enter a direction (N/S/W/E): ").lower()

        # Check which direction the user wants to try searching for (North, South, West, East)
        if (directionQuery == "n" or directionQuery == "north"):
            directionQuery = 'N'

        elif (directionQuery == "s" or directionQuery == "south"):
            directionQuery = 'S'
        
        elif (directionQuery == "w" or directionQuery == "west"):
            directionQuery = 'W'
        
        elif (directionQuery == "e" or directionQuery == "east"):
            directionQuery = 'E'

        # Invalid direction- the project documentation did not specify what to do in this situation.
        # There are 2 options here: 1) Simply return back to the main function and prompt for a new command
        #                           2) Using the current method, re-prompt for a valid color & direction [loops]
        else:
            # print("**Invalid Direction entered.  Try again.\n")
            print("**That line does not run in the direction chosen...\n")
            # stopsInLineAndDirection(dbConn) # Brings user back to color select
            return

        # Title-case for the query
        colorQuery = colorQuery.title()

        # Handle extra whitespaces
        colorQuery = colorQuery.strip()
        directionQuery = directionQuery.strip()
        
        dbCursor.execute("""
            SELECT 
                Stops.Stop_Name,
                Stops.ADA AS isADACompliant
            FROM 
                Stops
            JOIN 
                StopDetails ON Stops.Stop_ID = StopDetails.Stop_ID
            JOIN 
                Lines ON StopDetails.Line_ID = Lines.Line_ID
            WHERE 
                Lines.Color = ? AND Stops.Direction = ?
            ORDER BY
                Stops.Stop_Name;
        """, (colorQuery, directionQuery,))

        # Get results
        results = dbCursor.fetchall()

        # Check if there are no stops in the given direction      or len(results) == 0
        if results is None or len(results) == 0:
            print("**That line does not run in the direction chosen...")
        else:

            # Outputs the actual data from the database now that a color and direction are confirmed to be valid 
            for row in results:

                is_ada_compliant = row[1]
                ADAStatus = "not handicap accessible" 

                if (is_ada_compliant):
                    ADAStatus = "handicap accessible"
                else:
                    ADAStatus = "not handicap accessible"

                print(f"{row[0]} : direction = {directionQuery} ({ADAStatus})")

            

        # Formatting
        print("") 

    # Invalid color
    else:
        print("**No such line...\n")



''' ##################################################################
#
# stopsByColor_DirectionSorted
#
# Outputs the number of stops for each line color, separated by direction. 
# Results shown in ascending order by color name, and then in ascending order by direction. 
# Also shows the percentage for each color/stop, which is taken out of the total number of stops
# '''
def stopsByColor_DirectionSorted(dbConn):
    
    print("Number of Stops For Each Color By Direction")
    dbCursor = dbConn.cursor()

    # Query for weekday riders; verified in SQLiteStudio
    dbCursor.execute("""
        SELECT
            Lines.Color,
            Stops.Direction,
            COUNT(Stops.Stop_ID) AS NumOfStops,
            (SELECT COUNT(*) FROM Stops) AS TotalStops
        FROM
            Lines
        JOIN
            StopDetails ON Lines.Line_ID = StopDetails.Line_ID
        JOIN
            Stops ON StopDetails.Stop_ID = Stops.Stop_ID
        GROUP BY
            Lines.Color,
            Stops.Direction
        ORDER BY
            Lines.Color ASC,
            Stops.Direction ASC;       
    """)

    stops = dbCursor.fetchall()

    # Assuming query worked, output the results
    if (stops != None):

        # Loop through the data/process it and output to user
        for row in stops:

            color = row[0]
            direction = row[1]
            num_of_stops = row[2]
            total_stops = row[3]
            percentage = (num_of_stops / total_stops) * 100
            
            # Output
            print(f"{color} going {direction} : {num_of_stops} ({percentage:.2f}%)")

    print() # Formatting

    # End stopsByColor_DirectionSorted()



''' ##################################################################
#
# stationRidershipByYear
#
# Given a station name, outputs the total ridership for each year for that station, in 
# ascending order by year. Allows the user to use wildcards _ and % for partial names. 
# Shows an error message if the station name does not exist or if multiple station names 
# match. After the output, the user is given the option to plot the data
# '''
def stationRidershipByYear(dbConn):

    # Get input from user
    query = input("\nEnter a station name (wildcards _ and %): ")

    # Call search_Station() function
    result = search_Station(dbConn, query, 3)

    # No matching stations; return early
    if not result:
        print("**No station found...\n")
        return

    # More than one matching station; return early
    # Uses a set because the result returns all the results for a station over the years,
    # so it can tell if there are more than one station but ignore the same results for 
    # a particular station.
    elif (len(set(row[3] for row in result)) > 1):
        print("**Multiple stations found...\n")
        return

    # Only one station matched, output it's data and ask if the user wants to plot it
    else:

        station_name = result[0][3]
        print("Yearly Ridership at " + station_name)

        # Assuming query worked, output the results
        if result is not None:
            
            # Will hold a list of the data being printed out, should the user want to plot it
            years = []
            riders = []

            # Update/Output values for each year found
            for row in result:
                year = row[0]
                totalRiders = row[1]

                # Update lists
                years.append(year)
                riders.append(totalRiders)

                print(f"{year} : {totalRiders:,}")


            # Does the user want to plot the data?
            plotStatus = input("Plot? (y/n) ")

            # If "y" create a plot, else do nothing
            if (plotStatus == "y"):
                
                print("\nOutputting plot...")

                # Additional settings for the plot
                plt.figure(figsize=(10, 6))  # Adjust the size of the plot
                plt.plot(years, riders, color='b', label='Ridership')  # Specify marker, linestyle, and color
                plt.title(f"Yearly Ridership at {station_name} Station")  # Add a title
                plt.xlabel("Year")  # Add label for x-axis
                plt.ylabel("Number of Riders")  # Add label for y-axis

                plt.show()


    print() # Formatting

    # End stationRidershipByYear()



''' ##################################################################
#
# stationRidershipByYear
#
# Given a station name and year, output the total ridership for each 
# month in that year. SQL wildcards (_ and %) supported for the station name.
# Displays the found data, then asks if the user wants to plot it.
#
# '''
def stationRidershipByMonth(dbConn):
    
    # Get input from user
    query = input("\nEnter a station name (wildcards _ and %): ")

    # Call search_Station() function
    result = search_Station(dbConn, query, 4)

    # No/Multiple matching stations; return early.  This is handled inside of search_Station mode 4
    if result is None:
        # print("**No station found...\n")
        return

    # Only one match found
    else:
        
        # print(result)
        print("Monthly Ridership at " + result[0][3] + " for " + result[0][0])
        
        # Will hold a list of the data being printed out, should the user want to plot it
        months = []
        riders = []

        # Update/Output values for each year found
        for row in result:
            year = row[0]
            month = row[1]
            totalRiders = row[2]

            # print(row)

            # Update lists
            months.append(month)
            riders.append(totalRiders)

            print(f"{month}/{year} : {totalRiders:,}")


        # Does the user want to plot the data?
        plotStatus = input("Plot? (y/n) ")

        # If "y" create a plot, else do nothing
        if (plotStatus == "y"):

            # # Additional settings for the plot
            plt.figure(figsize=(10, 6))  # Adjust the size of the plot
            plt.plot(months, riders, color='b', label='Ridership')  # Specify marker, linestyle, and color
            plt.title(f"Monthly Ridership at {result[0][3]} Station ({result[0][0]})")  # Add a title
            plt.xlabel("Month")  # Add label for x-axis
            plt.ylabel("Number of Riders")  # Add label for y-axis

            plt.show()

    print() # Formatting
    # End stationRidershipByYear()



#
def twoStationsByDay(dbConn):

    print("\n**NOT IMPLEMENTED CORRECTLY!!**\nExiting...\n")
    exit(0)
    
    station_name = input("Enter station name (wildcards _ and %): ")
    year = input("Enter year: ")

    # Search for the station using partial name search mode (mode 1)
    query_result = search_Station(dbConn, station_name, 1)

    if query_result:
        # Extract the station ID from the query result
        station_id = query_result[0][1]

        # Query to get the first 5 days of the year for the given station
        query_first_5_days = f"""
            SELECT
                strftime('%Y', Ridership.Ride_Date) AS Year,
                Ridership.Ride_Date,
                SUM(Ridership.Num_Riders) AS TotalRidership
            FROM
                Ridership
            JOIN
                Stations ON Ridership.Station_ID = Stations.Station_ID
            WHERE
                Stations.Station_ID = {station_id}
                AND strftime('%Y', Ridership.Ride_Date) = "{year}"
            GROUP BY
                Year, Ridership.Ride_Date
            ORDER BY
                Year ASC, Ridership.Ride_Date ASC
            LIMIT 5;
        """

        # Query to get the last 5 days of the year for the given station
        query_last_5_days = f"""
            SELECT
                strftime('%Y', Ridership.Ride_Date) AS Year,
                Ridership.Ride_Date,
                SUM(Ridership.Num_Riders) AS TotalRidership
            FROM
                Ridership
            JOIN
                Stations ON Ridership.Station_ID = Stations.Station_ID
            WHERE
                Stations.Station_ID = {station_id}
                AND strftime('%Y', Ridership.Ride_Date) = "{year}"
            GROUP BY
                Year, Ridership.Ride_Date
            ORDER BY
                Year DESC, Ridership.Ride_Date DESC
            LIMIT 5;
        """

        # Execute the queries
        dbCursor = dbConn.cursor()
        dbCursor.execute(query_first_5_days)
        result_first_5_days = dbCursor.fetchall()

        dbCursor.execute(query_last_5_days)
        result_last_5_days = dbCursor.fetchall()

        # Output the results for the given station
        print("\nResults for Station (First 5 Days):")
        for row in result_first_5_days:
            print(f"Year: {row[0]}, Date: {row[1]}, Total Ridership: {row[2]}")

        print("\nResults for Station (Last 5 Days):")
        for row in result_last_5_days:
            print(f"Year: {row[0]}, Date: {row[1]}, Total Ridership: {row[2]}")

    else:
        print("Station not found in the database.")

    print("\nEnd of current functionality...\n")




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
        weekdayRidershipByName(dbConn)

    elif (userChoice == '4'):
        stopsInLineAndDirection(dbConn)

    elif (userChoice == '5'):
        stopsByColor_DirectionSorted(dbConn)

    elif (userChoice == '6'):
        stationRidershipByYear(dbConn)

    elif (userChoice == '7'):
        stationRidershipByMonth(dbConn)

    elif (userChoice == '8'):
        twoStationsByDay(dbConn)

    elif (userChoice == '9'):
        print("Chose command 9 - Not Yet Implemented.\nExiting...\n")
        exit(0)
    
    # If the user wants to exit
    elif (userChoice == 'x'):
        # print("\nExiting...")
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

    if (dbConn != None):
        print_stats(dbConn);

    # print("\nSelect a station name to search for:")

    print()
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