# Version 7.1R - Command 7 Completed*

> This version currently supports the following functionality:
>
>    - Everything from version 2.1 - 6.1R[^2]  
>    - Finished working on **Command 7** [see [changelog](#changelog)] and this footnote[^3].
>    
>

------
# Changelog:  ##
> 
>    - Added some more comments to clarify what I was doing
>    
>
>    - Lots and lots of formatting, as the **AUTOGRADER** was released.
>       -  *(Currently at: **30/50** points, excluding plots and style points)*
>
>    - Given a station name and year, output the **total ridership[^3]** for each month in that year, in 
>        ascending order by year. Allows the user to use wildcards _ and % for partial names. 
>        *(Shows an error message if the station name does not exist or if multiple station names 
>        match.)*
> 
>    - Added plotting capabilities *(including labels/titles)*
>    

------

# Planned Functionality:

> The next version will focus on:
>
>   - Adding functionality for **command 8**, specifically:  
>      ```
>        Given two station names and year, output the total ridership for each day in that year. 
>        The user should be able to enter SQL wildcards (_ and %) for each station name. Since 
>        the full output would be quite long, you should only output the first 5 days and last 5 
>        days of data for each station. 
>
>        Also give the user the option to see a plot of the results. If the user responds with 
>        “y” your program should plot as shown below (with appropriate title, legend, and axis labels). 
>        If the user responds with any other input, do not plot. If no matching station names are found, 
>        or if multiple matching station names are found, display the corresponding error message. 
>        Note that if the user enters a year for which there is no data, no error message is necessary. 
>        The output and plot will be empty, which is sufficient.
>      ```
>
>   - Fix the issue of ridership being multiple times what it should be.  For **command 7**, the input
>     seems to be *doubled*, or even *quadrupled* for some reason.  A similar thing is occuring for
>     **command 6**.
>     

------

# Progress

> Current progress:
>
> - [x] Gets the station name and year
> - [x] Handles SQL wildcards in
> - [x] Handles no matches (if a year where this no data is given, no error message needed)
> - [x] Handles multiple matches (if a year where this no data is given, no error message needed)
> - [x] Outputs the total by month for the given year
> - [ ] Outputs the monthly totals[^3]
> - [ ] Outputs the information correctly, according to the AutoGrader
> 
> - [x] Handle Plotting from the user's input, using above data
>
> [see [changelog](#changelog)]

------

# Footnotes: 
>  
> [^1]: This is not *explicitly* mentioned in the project document's description of **Command 6**.  
>       The sample output **DOES NOT** contain ADA information, so it will not be included.  
>       *(Autograder output confirms this is not needed)*
> 
> [^2]: Changed how I handle **Command 4**, when an invalid direction is entered  
>       Handling this was not mentioned in the project documentation: 2 options are listed in the code  
>       The AutoGrader offered a format/message to output when these conditions are met, so the code  
>       has been updated to reflect that.
>
> [^3]: The number of riders seems to be multiple times what it should be.  For command 6 and 7,
>       sometimes it can go from being double what it should be, to quadruple.  Working to resolve this
>       issue, but for now, the core functionality is present.  Once this is fixed, everything should
>       be good to go.