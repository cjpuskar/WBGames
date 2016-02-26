'''
This script is used to create the SAR table and to copy all data from the Spend_And_Rev table
into the SAR table
'''

# MODULES
import sqlite3

# Create database
connection = sqlite3.connect('CCSF_DB')
cursor = connection.cursor()

# Create SAR tables
cursor.execute("DROP TABLE IF EXISTS SAR")
cursor.execute("CREATE TABLE SAR ( rowid, 'Fiscal Year' TEXT, 'Revenue or Spending' TEXT, OrgGroupID INT REFERENCES OrgGroup(OrgGroupID), DeptID REFERENCES Dept(DeptID), Amount REAL)")
connection.commit()

# Insert from Spend_And_Rev to SAR
cursor.execute("INSERT INTO SAR SELECT * FROM Spending_And_Revenue")
connection.commit()

# close Db connection
connection.close()
