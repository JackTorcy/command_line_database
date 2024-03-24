from connect import *
#? Run to insert another 100 records into the table
def dump_data():
    #open folder/file...
    with open('C:/Users/jack/OneDrive/Documents/Just IT/[Week 11] Project Week - PythonSql/command_line_database/tblFilms.sql') as dumpfile:
        #read the contents saved  in the dumpfile varaible and pass it to the sqlInsertScript variable
        sqlInsertScript = dumpfile.read()

        #write the content found/stored in the sqlInsertScript to the table
        dbCursor.executescript(sqlInsertScript)
        

dump_data()