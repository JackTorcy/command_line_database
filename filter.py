from connect import *
from main import *
''' #! DELETE THIS SECTION AFTER WORKING SEARCH SECTION
#?PLAN FOR SEARCH.PY to be done 04/03/24
#---------------------------------------------------------------------------------------------------------------------------------------------
#*-Option 5 of menu runs 'more search options' - 'search.py' this page - KEEP THIS                                                           -
# -search.py displays 1.search by genre 2.search by yearRelease 3.search by rating 4.Back to menu (main.py)                                  -
# -Get user input                                                                                                                            -
# -userInput saved - match Case statement, else being invalid input, close program                                                           -
# -based on input, field value will be set to either genre, yearRelease or rating. - 4 will run main.py to take you back                     -
# -when select statement is called, fill in column with 'field' it will select the correct column and display that and order by 'field' too  -
# -Should work. I hope                                                                                                                       -
#! ADD MESSAGE AFTER UPDATE/ADD/DELETE TO SAY '{record inserted into table successfully}'
#---------------------------------------------------------------------------------------------------------------------------------------------
'''
def filter_films():
    #?Display menu while True
    filterProgram = True #variable assignemnt
    while filterProgram: 
        #?display menu
        with open('C:/Users/jack/OneDrive/Documents/Just IT/[Week 11] Project Week - PythonSql/command_line_database/filter.txt') as filterTxt:
            readFilter = filterTxt.read()
            print(readFilter)
        try:
            #?Assigning user choice to menu option
            filterChoice = int(input('Enter a filter option: ')) #user choice
            match filterChoice:
                #?Fields
                case 1: 
                    field = 'ReleaseYear'
                case 2: 
                    field = 'Rating'
                case 3: 
                    field = 'Genre'
                #?Other options
                case 4:
                    #?return to menu
                    filterProgram = False #loop stop
                    print('Returning to Main Menu') #keep user informed
                    input('Press Enter to Continue: \n') #waits for key input until returning
                    mainMenu() #return to menu
                    break #important to stop this for running once main menu is exited
                case 5:
                    #?exit program entirely
                    print('Exiting Program...')
                    filterProgram = False #loop stop
                    break
                case _:
                    #?invalid option
                    print('Chosen number does not exist as an option!')
                    field = None
            
            #?checks if a field was selected in match statement
            if field is not None:
                print(f'Selected {field}') #displays user option
                #?Gather values
                value = input(f'Enter a {field} value: ')
                dbCursor.execute(f'SELECT * FROM tblFilms WHERE {field} = ? ORDER BY {field}, filmID', (value,)) 
                filteredFilms = dbCursor.fetchall()
                
                #?check for results
                if filteredFilms:
                    #?Formatting output into a table in console
                    print('*'*97)
                    print(f' |----------------------------------Films by {field}, {value}---------------------------------|\n')
                    print(' |-FilmID-|----------------Title---------------|-ReleaseYear-|-Rating-|-Duration-|----Genre----|')
                    print('*'*97)
                    #?iterate through gathered films
                    for film in filteredFilms:
                        #?prints each film value (title, year, genre etc)
                        print(f'*| {film[0]:6} | {film[1]:34} | {film[2]:11} | {film[3]:6} | {film[4]:8} | {film[5]:11} |*')
                    print('*'*97)
                #?no results
                else:
                    print('No films under that filter exist!')
            input('Press Enter to Continue: \n')#wait for user input before continue
        #!ERRORS
        except sql.OperationalError as oe:
            print(f'Operational Error: {oe}')
        except sql.Error as e:
            print(f'Error: {e}')
        except sql.ProgrammingError as pe:
            print(f'Programming Error: {pe}')

if __name__ == '__main__':
    filter_films()