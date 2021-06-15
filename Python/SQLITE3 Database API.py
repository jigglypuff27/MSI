#SQLITE3 Database API

import sqlite3

def main():
    print('Connecting')
    db=sqlite3.connect('db-api.db')         #creates a db file
    cur=db.cursor()                         #creating a cursor to connect and execute programs
    cur.execute('DROP TABLE IF EXISTS test')        #execute is used to execute sql command
    cur.execute("""CREATE TABLE test(
        id INTEGER PRIMARY KEY,
        string TEXT,
        number INTEGER )"""
    )
    cur.execute("""INSERT INTO test values(1,'hello','57')""")
    cur.execute("""INSERT INTO test (string,number) values ('yeee',29)""")
    db.commit()          #commit
    for row in cur.execute('SELECT * FROM test'):    
        print(row)
    db.close()           #close

main()        