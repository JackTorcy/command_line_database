import sqlite3 as sql #imports sqlite3 library

try:
    #?connects sql to python
    with sql.connect('C:/Users/jack/OneDrive/Documents/Just IT/[Week 11] Project Week - PythonSql/command_line_database/filmflix.db') as dbCon: 
    #?Cursor variable assignment for sqlite statements and data fetching
        dbCursor = dbCon.cursor()
#!ERRORS
except sql.OperationalError as oe:
        print(f'Operational Error: {oe}') #In case of error finding file