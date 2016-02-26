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

* CSV Files
 - Graffiti_30_Days
 - Spending_And_Revenue.csv.zip (make sure to unzip if you want to follow along)


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

  - I loaded the Graffiti_30_Days csv file into Jupyter Notebooks to display some examples of Date Manipulation, Timeseries Data, and Dataframes.

    * To open jupyter notebooks, at the command line type:

    ```shell
    jupyter notebooks
    ```

    * Open 'Grafetti_Time_Series_Analysis.ipynb'

## Select Joins
## Complex Select
