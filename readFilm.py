from connect import *

def read_films():
    try:
        #?Get all table rows
        dbCursor.execute('SELECT * FROM tblFilms')#selects all rows
        allFilms = dbCursor.fetchall() #gets all rows
        
        #?Check rows exist
        if allFilms:
            #Format readFile output
            print('*'*97)
            print(' |------------------------------------------All Films------------------------------------------|\n')
            print(' |-FilmID-|----------------Title---------------|-ReleaseYear-|-Rating-|-Duration-|----Genre----|')
            print('*'*97)
            for film in allFilms:
                print(f'*| {film[0]:6} | {film[1]:34} | {film[2]:11} | {film[3]:6} | {film[4]:8} | {film[5]:11} |*')
            print('*'*97)

        else:
        #?No Rows
            print('There is no content in the database!')
    
    except sql.OperationalError as oe:
        print(f'Operational Error: {oe}')
    except sql.Error as e:
        print(f'Error: {e}')
    except sql.ProgrammingError as pe:
        print(f'Programming Error: {pe}')


if __name__ == '__main__':
    read_films()