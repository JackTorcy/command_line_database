from connect import *

dbCursor.execute('ALTER TABLE tblFilms RENAME COLUMN yearReleased TO ReleaseYear ')
dbCon.commit()