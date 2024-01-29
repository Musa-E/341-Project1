# Version 5.1R - Command 5 Completed

> This version currently supports the following functionality:
>
>    - Everything from version 2.1 - 4.2B[^2]  
>    - Currently working on **Command 6** [see [changelog](#changelog)]  
>    
>

------
# Changelog:  ##
> 
>    - Added some more comments to clarify what I was doing
>    
>    - The user can now display the number of stops per color by direction
>
>    - Lots and lots of formatting, as the **AUTOGRADER** was released.
>       -  *(Currently at: **20/50** points, excluding plots and style points)*
>    

------

# Planned Functionality:

> The next version will focus on:
>
>   - Adding functionality for **command 6**, specifically:  
>      ```
>        Given a station name, output the total ridership for each year for that station, in 
>        ascending order by year. Allow the user to use wildcards _ and % for partial names. 
>        Show an error message if the station name does not exist or if multiple station names 
>        match.
>
>        After the output, the user is given the option to plot the data. Make sure the axis labels 
>        and title of the figure are set appropriately. If the user responds with any input other than 
>        “y”, do not plot.```
>
>   - Add ADA (accessibility) information to the output for command 4[^1].
>     

------

# Progress

> Current progress:
>
> - [x] Gets the Colors
> - [x] Gets the Direction(s)
> - [x] Calculate total stops for each stop of that color in the given direction
> - [x] Calculate the total percentage of the above total stops per color out of overall number of stops
>
> [see [changelog](#changelog)]

------

# Footnotes: 
> [^1]: This is not *explicitly* mentioned in the project document's description of **Command 4**.  
>       However, the sample output **DOES** contain ADA information.  I will ask for further clarification  
>       about this, but for now I'm leaving it _**without**_ the information until it's confirmed that I need it.  
> 
> [^2]: May need to change how I handle **Command 4**, when an invalid direction is entered  
>       Handling this was not mentioned in the project documentation: 2 options are listed in the code