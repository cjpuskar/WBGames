# WBGames

## Table of Contents

- [Coding Challenge Synopsis](#coding-challenge-synopsis)
- [Dependencies](#dependencies)
- [Instructions](#instructions)
- [Coding Exercises](#coding-exercises)
  - [1. pulls data out of csv and/or json files](#1.pulls-data-out-of-csv-and/or-json-files)
  - [Convert Data from CSV to JSON](#convert-data-from-csv-to-json)
  - [Date Manipulation](#date-manipulation)
  - [Timeseries Data](#timeseries-data)
  - [Dataframes](#dataframes)
  - [6. select joins inner/left/right/full/cartesian](#select-joins-inner/left/right/full/cartesian)
  - [7. complex select (i.e. aggregate/group by, with pragma, recursive, etc)](#complex-select-(i.e.-aggregate/group-by,-with-pragma,-recursive,-etc))

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
## Date Manipulation
## Timeseries Data
## Dataframes

  - I loaded the Graffiti_30_Days csv file into Jupyter Notebooks to display some examples of Date Manipulation, Timeseries Data, and Dataframes.

    * To open jupyter notebooks, at the command line type:

    ```shell
    jupyter notebooks
    ```

    * and open 'Grafetti_Time_Series_Analysis.ipynb'
