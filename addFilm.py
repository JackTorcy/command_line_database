from connect import *

def add_film():
    try: 
        #?Gathers new movies info
        #Title, Year, Rating, Duration, Genre
        fTitle = input('Enter the film title: ')
        fYear = input('Enter the film\'s release year: ')
        fRating = input('Enter the film\'s rating: ')
        fDuration = input('Enter the film\'s duration: ')
        fGenre = input('Enter the film\'s genre: ')
        
        #?Add values to table
        dbCursor.execute('INSERT INTO tblFilms VALUES (NULL,?,?,?,?,?)', (fTitle, fYear, fRating, fDuration, fGenre)) #adds values
        dbCon.commit() # commit change
        #*Confirmation message
        print(f'Added {fTitle} to the database.')
    
    #!ERRORS
    except sql.OperationalError as oe:
        print(f'Operational Error: {oe}')
    except sql.Error as e:
        print(f'Error: {e}')
    except sql.ProgrammingError as pe:
        print(f'Programming Error: {pe}')


if __name__ == '__main__':
    add_film()