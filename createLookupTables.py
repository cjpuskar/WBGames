# MODULES
import sqlite3

# Create the database
connection = sqlite3.connect('CCSF_DB')
cursor = connection.cursor()

# Create OrgGroup Table
cursor.execute("DROP TABLE IF EXISTS OrgGroup")
cursor.execute("CREATE TABLE OrgGroup ( OrgGroupID PRIMARY KEY, OrgGroup, FOREIGN KEY ) ")
connection.commit()

# Insert Values into OrgGroup Table
cursor.execute("INSERT INTO OrgGroup (OrgGroupID, OrgGroup) VALUES (1, 'Public Protection'),(2, 'Public Works, Transportation & Commerce'), (3, 'Human Welfare & Neighborhood Development'),(4, 'Community Health'),(5, 'Culture & Recreation'),(6, 'General Administration & Finance'),(7, 'General City Responsibilities')")
connection.commit()

# Create Dept Table
cursor.execute("DROP TABLE IF EXISTS Dept")
cursor.execute("CREATE TABLE Dept( DeptID PRIMARY KEY, Dept) ")
connection.commit()

# Insert Values into Dept Table
cursor.execute("INSERT INTO Dept (DeptID, Dept) VALUES ('AAM', 'Asian Art Museum'),('ADM', 'General Services Agency - City Admin'),('ADP', 'Adult Probation'),('AGE', 'Human Services'),('AGW', 'General Services Agency - City Admin'),('AIR', 'Airport Commission'),('ANC', 'General Services Agency - City Admin'),('ART', 'Arts Commission'),('ASR', 'Assessor/Recorder'),('BOS', 'Board of Supervisors'),('CAO', 'General Services Agency - City Admin'),('CAT', 'City Attorney'),('CCD', 'Community College District'),('CFC', 'Children and Families Commission'),('CFM', 'General Services Agency - City Admin'),('CHF', 'Children, Youth & Their Families'),('CII', 'Community Investment & Infrastructure'),('CME', 'General Services Agency - City Admin'),('CON', 'Controller'),('CPC', 'City Planning'),('CRT', 'Superior Court'),('CSC', 'Civil Service Commission'),('CSS', 'Child Support Services'),('CTA', 'County Transportation Authority'),('CWP', 'PUC Wastewater Enterprise'),('DAT', 'District Attorney'),('DBI', 'Department of Building Inspection'),('DOE', 'General Services Agency - Technology'),('DPH', 'Public Health'),('DPT', 'Municipal Transportation Agency'),('DPW', 'General Services Agency - Public Works'),('DSS', 'Human Services'),('ECD', 'Department of Emergency Management'),('ECN', 'Economic and Workforce Development'),('ENV', 'Environment'),('ETH', 'Ethics Commission'),('FAM', 'Fine Arts Museum'),('FIR', 'Fire Department'),('GEN', 'General City Responsibility'),('HCH', 'Public Health'),('HCN', 'Public Health'),('HGH', 'Public Health'),('HHP', 'PUC Hetch Hetchy'),('HMH', 'Public Health'),('HPH', 'Public Health'),('HRC', 'Human Rights Commission'),('HRD', 'Human Resources'),('HSS', 'Health Service System'),('JUV', 'Juvenile Probation'),('LHP', 'PUC Hetch Hetchy'),('LIB', 'Public Library'),('LLB', 'Law Library'),('MCT', 'Superior Court'),('MTA', 'Municipal Transportation Agency'),('MYR', 'Mayor'),('OCA', 'General Services Agency - City Admin'),('PAB', 'Board of Appeals'),('PAG', 'General Services Agency - City Admin'),('PDR', 'Public Defender'),('POL', 'Police'),('PRT', 'Port'),('PTC', 'Municipal Transportation Agency'),('PUC', 'PUC Public Utilities Commission'),('PUR', 'General Services Agency - City Admin'),('RCD', 'General Services Agency - City Admin'),('REC', 'Recreation and Park Commission'),('REG', 'Elections'),('RES', 'General Services Agency - City Admin'),('RET', 'Retirement System'),('RNT', 'Rent Arbitration Board'),('SCI', 'Academy of Sciences'),('SHF', 'Sheriff'),('TIS', 'General Services Agency - Technology'),('TJP', 'Transbay Joint Powers Authority'),('TTX', 'Treasurer/Tax Collector'),('TXC', 'Municipal Transportation Agency'),('UNA', 'General Fund Unallocated'),('USD', 'County Education Office'),('WAR', 'War Memorial'),('WOM', 'Department of the Status of Women'),('WTR', 'PUC Water Department')")
connection.commit()

# Close DB connection
connection.close()
