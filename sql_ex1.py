import os
import sqlite3

#build path to db, datafile and open
cur_path = os.path.dirname(__file__)
db_filename = cur_path+'/sql-ex1.sqlite'
data_filename = cur_path+'/mbox.txt'
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

#create new db
cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('CREATE TABLE counts(org,count)')

data = open(data_filename, "r")
for line in data:
    if not line.startswith('From: '):
        continue #ignore lines that aren't a sent email
    else:
        #first split the line by space to get email
        splitline = line.split()
        email = splitline[1]
        #then split the email by @ to get org
        splitline = email.split('@')
        org = splitline[1]
        
        cursor.execute('SELECT * FROM Counts WHERE org = ?', (org,))
        row = cursor.fetchone()
        if row is None: #if first one
            cursor.execute('INSERT INTO Counts(org,count) VALUES(?,1)', (org,))
        else: #add 1 to count
            cursor.execute('UPDATE Counts SET count=count+1 WHERE org= ?', (org,))
conn.commit()

output_string = conn.execute('SELECT org,count FROM Counts ORDER BY count DESC')
for line in output_string:
    print( str(line[0]), str(line[1]) )

        
        

