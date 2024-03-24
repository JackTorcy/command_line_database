from connect import * #import connect for exceptions
import addFilm, deleteFilm, filter, readFilm, updateFilm #import all other programs to call their functions

def mainMenu():
    mainProgram = True #while running
    while mainProgram: #while running
        try:
            #?Prints the main menu
            with open('C:/Users/jack/OneDrive/Documents/Just IT/[Week 11] Project Week - PythonSql/command_line_database/mainMenu.txt') as mainMenuFile:
                mainMenuContents = mainMenuFile.read()
                print(mainMenuContents) 
            
            #?Navigation to other python scripts
            menuChoice = int(input('Select an option from the menu: ')) #user input menu choice
            match menuChoice:
                case 1: 
                    readFilm.read_films() #displays all films in database
                case 2:
                    addFilm.add_film() #adds new film
                case 3:
                    updateFilm.update_film() #updates existing film
                case 4: 
                    deleteFilm.delete_film() #deletes existing film
                case 5:
                    print('\n')
                    filter.filter_films() #runs filter options menu
                    filterProgram = False
                    break
                case 6:
                    print('Exiting Program...')
                    filterProgram = False
                    break
                case _:
                    print('Invalid Choice!')
        
            input('Press Enter to Continue: \n')
        
        except sql.OperationalError as oe:
            print(f'Operational Error: {oe}')
        except sql.Error as e:
            print(f'Error: {e}')
        except sql.ProgrammingError as pe:
            print(f'Programming Error: {pe}')

if __name__ == '__main__':
    mainMenu()
