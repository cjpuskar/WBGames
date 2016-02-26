# WBGames

## Table of Contents

- [Coding Challenge Synopsis](#coding-challenge-synopsis)
- [Dependencies](#dependencies)
- [Instructions](#instructions)
- [Coding Exercises](#coding-exercises)
  - [1. pulls data out of csv and/or json files](#1.pulls-data-out-of-csv-and/or-json-files)
  - [Convert Data from CSV to JSON](#convert-data-from-csv-to-json)
  - [3.puts dates into a database and manipulates them](#puts-dates-into-a-database-and-manipulates-them)
  - [4. date manipulation in general](#date-manipulation-in-general)
  - [5. timeseries data](#timeseries-data)
  - [6. select joins inner/left/right/full/cartesian](#select-joins-inner/left/right/full/cartesian)
  - [7. complex select (i.e. aggregate/group by, with pragma, recursive, etc)](#complex-select-(i.e.-aggregate/group-by,-with-pragma,-recursive,-etc))
  - [8. dataframes](#dataframes)
  - [9. pull data from DB and display time series/statistical data](#pull-data-from-DB-and-display-time-series/statistical-data)

## Dependencies
* Jupyter Notebook
* CSV Files
 - Graffiti_30_Days


## Convert Data from CSV to JSON

  - The csv-json.py script converts a csv file into a json file.
  - It takes 3 arguments:
     * -i: Name of the input file
     * -o: Name of the output file
     * -f: The format, can be either 'pretty' or 'dump'

     ```shell
     python csv-json.py -i Graffiti_30_Days.csv -o Graffiti_30_Days.json -f pretty
     ```
