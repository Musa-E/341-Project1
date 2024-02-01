# Version 6.1R - Command 6 Completed

> This version currently supports the following functionality:
>
>    - Everything from version 2.1 - 5.2B[^2]  
>    - Finished working on **Command 6** plotting [see [changelog](#changelog)]  
>    
>

------
# Changelog:  ##
> 
>    - Added some more comments to clarify what I was doing
>    
>    - The user can now output the stops of the given line color and direction
>
>    - Lots and lots of formatting, as the **AUTOGRADER** was released.
>       -  *(Currently at: **30/50** points, excluding plots and style points)*
>
>    - Given a station name, outputs the total ridership for each year for that station, in 
>        ascending order by year. Allows the user to use wildcards _ and % for partial names. 
>        *(Shows an error message if the station name does not exist or if multiple station names 
>        match.)*
>
>    - Removed ADA (accessibility) information to the output for command 6[^1].
> 
>    - Added plotting capabilities *(including labels/titles)*
>    

------

# Planned Functionality:

> The next version will focus on:
>
>   - Adding functionality for **command 7**, specifically:  
>      ```
>        Given a station name and year, output the total ridership for each month in that year.
>      The user should be able to enter SQL wildcards (_ and %) for the station name.
> 
>      Once the station name and year have been entered, display the monthly totals. Then, 
>      give the user the option to see a plot of the results. If the user responds with “y” your 
>      program should plot as shown below (with appropriate title, legend, and axis labels). If 
>      the user responds with any other input, do not plot.
> 
>      If no matching station names are found, or if multiple matching station names are found, 
>      display the corresponding error message. Note that if the user enters a year for which 
>      there is no data, no error message is necessary. The output and plot will be empty, 
>      which is sufficient.
>      ```
>
>
>     

------

# Progress

> Current progress:
>
> - [ ] Gets the station name and year
> - [ ] Handles SQL wildcards in
> - [ ] Handles no matches (if a year where this no data is given, no error message needed)
> - [ ] Handles multiple matches (if a year where this no data is given, no error message needed)
> - [ ] Outputs the total by month for the given year
> - [ ] Outputs the monthly totals
> - [ ] Outputs the information correctly, according to the AutoGrader
> 
> - [ ] Handle Plotting from the user's input, using above data
>
> [see [changelog](#changelog)]

------

# Footnotes: 
> [^1]: This is not *explicitly* mentioned in the project document's description of **Command 6**.  
>       The sample output **DOES NOT** contain ADA information, so it will not be included.  
>       *(Autograder output confirms this is not needed)*
> 
> [^2]: Changed how I handle **Command 4**, when an invalid direction is entered  
>       Handling this was not mentioned in the project documentation: 2 options are listed in the code  
>       The AutoGrader offered a format/message to output when these conditions are met, so the code  
>       has been updated to reflect that.