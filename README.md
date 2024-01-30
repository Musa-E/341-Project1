# Version 5.2B - Command 6 Data Completed

> This version currently supports the following functionality:
>
>    - Everything from version 2.1 - 4.2B[^2]  
>    - Currently working on **Command 6** plotting [see [changelog](#changelog)]  
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
>       -  *(Currently at: **25/50** points, excluding plots and style points)*
>
>    - Given a station name, outputs the total ridership for each year for that station, in 
>        ascending order by year. Allows the user to use wildcards _ and % for partial names. 
>        *(Shows an error message if the station name does not exist or if multiple station names 
>        match.)*
>
>    - Added ADA (accessibility) information to the output for command 4[^1].
>    

------

# Planned Functionality:

> The next version will focus on:
>
>   - Adding functionality for **command 6**'s plotting, specifically:  
>      ```
>        After the output, the user is given the option to plot the data. Make sure the axis labels 
>        and title of the figure are set appropriately. If the user responds with any input other than 
>        “y”, do not plot. 
>      ```
>
>
>     

------

# Progress

> Current progress:
>
> - [x] Gets the Colors
> - [x] Gets the Direction(s)
> - [x] Handles No Matches Found
> - [x] Handles Multiple Matches Found
> - [x] Handles One Match Found
> - [x] Outputs information in Asc. Order of Stop Names
> - [x] Outputs ADA Compliancy information
> - [x] Outputs the information correctly, according to the AutoGrader
> 
> - [ ] Handle Plotting from the user's input
>
> [see [changelog](#changelog)]

------

# Footnotes: 
> [^1]: This is not *explicitly* mentioned in the project document's description of **Command 4**.  
>       However, the sample output **DOES** contain ADA information, so it will be included.  
> 
> [^2]: Changed how I handle **Command 4**, when an invalid direction is entered  
>       Handling this was not mentioned in the project documentation: 2 options are listed in the code  
>       The AutoGrader offered a format/message to output when these conditions are met, so the code  
>       has been updated to reflect that.