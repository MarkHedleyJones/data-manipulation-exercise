# data-manipulation-exercise
Helping a friend with a Python based data manipulation task

>I am trying to wrangle data that I have saved into a csv from a web scraping script I wrote. The problem is that the pages that I scraped have inconsistent numbers of data points. For example, one page might have 'FULL NAME', 'BORN', 'DIED', 'WEIGHT', 'POSITION' (for a player who has passed away so no current age) and another page might have 'FULL NAME', 'BORN', 'AGE', 'WEIGHT', 'POSITION' (where a player is still alive so it can't have a date of death so it shows current age).
> 
>So for this example I would need an end csv that looks like the combined headers with blanks where the data isn't present:
>
>Row 1: 'FULL NAME', 'BORN', 'AGE', 'DIED', 'WEIGHT', 'POSITION'
>
>Row 2: 'John Smith', '22/03/1899', , '10/10/1990', 90, 'left'
>
>Row 3: 'Jimmy Key', '2/05/1990', 29, , 110, middle field' 
>
>I have attached a sample csv where the top row is the main header row in which I am trying to align the data with and I would like to loop over each set of rows (the data is in pairs, "header" and the corresponding data so I can keep tabs on what column holds what information.)
>
>The end result I am going for is a csv with a header row in top row and the data has aligned to the header row given its "sub header" position. 

The included script will open the sample csv file and process it according to the above requirements. It writes the output to players_processed.csv. Run this by either cloning or downloading this repository and running `python process.py`.
