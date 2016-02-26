# MODULES
from __future__ import print_function
import sqlite3
import csv
import os
import glob     # glob module finds all pathnames matching a specified pattern according to rules used by Unix shell
import sys

# get DB name
db = sys.argv[1]

conn = sqlite3.connect(db)
conn.text_factory = str     # allows utf-8 data to be stored

c = conn.cursor()

# traverse the directory and process each csv file
for csvfile in glob.glob(os.path.join(sys.argv[2], "*.csv")):
    # remove the path and extension and use what's left as a table name
    tablename = os.path.splitext(os.path.basename(csvfile))[0]

    with open(csvfile, 'r') as f:
        reader = csv.reader(f)

        header = True
        for row in reader:
            if header:
                # gather column names from the first row of the csv
                header = False

                sql = "DROP TABLE IF EXISTS %s" % tablename
                c.execute(sql)

                # Create a table for each csv file
                sql = "CREATE TABLE %s (%s)" % (tablename, ", ".join([ '"%s"' % column for column in row]))
                c.execute(sql)

                insertsql = "INSERT INTO %s VALUES (%s)" % (tablename, ", ".join([ "?" for column in row]))

            else:
                c.execute(insertsql, row)

    conn.commit()

c.close()
conn.close()
