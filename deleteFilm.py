from connect import *

def delete_film():
    try:
        #?saves the ID for passing to sql for deletion of film.
        filmID = input('Enter the film ID you want to delete: ')
        #?Get film title for print use later
        dbCursor.execute(f'SELECT title FROM tblFilms where filmID = {filmID}')
        selectedFilmTitle = dbCursor.fetchone()
        #?Get film row for Deletion
        dbCursor.execute(f'SELECT * FROM tblFilms where filmID = {filmID}')
        row = dbCursor.fetchone()

        #? Checks row exists
        if row == None:
            print(f'No film with the filmID of {filmID} exists in the table!')
        #?Performs Deletion
        else:
            dbCursor.execute(f'DELETE FROM tblFilms WHERE filmID = ?', (filmID,)) #delete statement
            dbCon.commit() #commits change to table
            print(f'{selectedFilmTitle[0]} removed from the database.') #confirmation message

    #!ERRORS
    except sql.OperationalError as oe:
        print(f'Operational Error: {oe}')
    except sql.Error as e:
        print(f'Error: {e}')
    except sql.ProgrammingError as pe:
        print(f'Programming Error: {pe}')


if __name__ == '__main__':
    delete_film()