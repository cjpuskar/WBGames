# WBGames

## Table of Contents

- [Coding Challenge Synopsis](#coding-challenge-synopsis)
- [Dependencies](#dependencies)
- [Instructions](#instructions)
- [Coding Exercises](#coding-exercises)
  - [Pulls Data Out of CSV](#pulls-data-out-of-csv)
  - [Convert Data from CSV to JSON](#convert-data-from-csv-to-json)
  - [Date Manipulation](#date-manipulation)
  - [Timeseries Data](#timeseries-data)
  - [Dataframes](#dataframes)
  - [Select Joins](#select-joins)
  - [Complex Select](#complex-select)

## Dependencies

* Data files were downloaded from https://data.sfgov.org/

* Jupyter Notebook
* sqlite3
* Python
* CSV Files
 - Graffiti_30_Days
 - Spending_And_Revenue.csv.zip (Original dataset I started w/, only here as a ref, DONT USE!)
 - Spend_And_Rev.csv

## Pull Data Out of CSV

  - For this challenge I created a script csv2sqlite.py which, when run from the command line will scan a given directory for csv files and load them into a database using the filename as the tablename.

  ```shell
  python csv2sqlite.py nameofdb directory
  ```

  ```shell
  python csv3sqlite.py CCSF_DB /Users/cpuskar/Projects/WBGames
  ```

  Where:
  - nameofdb =  sqlite3 database name, in this case CCSF_DB
  - directory = location of csv files. Since the CSV files are in the projects root folder type 'pwd' and paste that in as the directory



## Convert Data from CSV to JSON
  - For this challenge I created a script which converts a CSV file to a JSON file.

  - The csv-json.py script converts a csv file into a json file.
  - It takes 3 arguments:
     * -i: Name of the input file
     * -o: Name of the output file
     * -f: The format, can be either 'pretty' or 'dump'

     ```shell
     python csv-json.py -i Graffiti_30_Days.csv -o Graffiti_30_Days.json -f pretty
     ```
 - The outputted JSON file is Graffiti_30_Days.json

## Date Manipulation
## Timeseries Data
## Dataframes

  - For this challenge I needed a time series dataset. On the SF data portal I found a dataset called Graffiti_30_Days which lists all reported cases of graffiti in the past 30 days. I decided to use this to plot the number of cases reported per day.

  - I loaded the Graffiti_30_Days csv file into Jupyter Notebooks to display some examples of Date Manipulation, Timeseries Data, and Dataframes.

    * To open jupyter notebooks, at the command line type:

    ```shell
    jupyter notebooks
    ```

    * Open 'Grafetti_Time_Series_Analysis.ipynb'

## Select Joins
## Complex Select

- For this challenge I wanted to show query's with JOINs in them but I didnt have a normalized database / datasets. I noticed that the Spending_And_Revenue file had a lot of redundant data, containing both IDs and Description field names so I decided to create my own.
   * Example: DeptID: 1, Dept: Police

- I created 2 lookup tables for my database
    * OrgGroup
    * Dept

  I used the 'Spend_And_Rev_Working.ipynb' notebook to help me find unique values for these columns for use in CREATE TABLE statements.

 - I wanted to find the amount of money the City of SF spent on Police in 2015 so I ran 'complexJoin.sql' script to discover that the City spent over $519 million.

```sqlite3
SELECT S."Fiscal Year", S."Revenue or Spending", D.dept, sum(S.Amount)
FROM SAR as S
JOIN OrgGroup as O
ON S.OrgGroupID = O.OrgGroupID
JOIN Dept as D
ON S.DeptID = D.DeptID
WHERE S."Revenue or Spending" = "Spending" and O.OrgGroup = "Public Protection" and S."Fiscal Year" = "2015" and Dept = "Police"
```
