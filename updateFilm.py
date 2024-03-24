from connect import *

def update_film():
    try:
        filmID = input('Enter the film ID you want to update: ')
        dbCursor.execute(f'SELECT * FROM tblFilms where filmID = {filmID}')
        row = dbCursor.fetchone()
        

        if row == None:
            print(f'No film with the filmID of {filmID} exists in the table!')
        else:
            field = input('Select field to update, (Title,ReleaseYear,Rating,Duration,Genre): ').title()
            validField = ['Title', 'Releaseyear', 'Rating', 'Duration', 'Genre']

            if field not in validField:
                print('Field does not exist!')
            else:
                match field:
                    case 'Title':
                        oldResult = row[1]
                    case 'Releaseyear':
                        oldResult = row[2]
                    case 'Rating':
                        oldResult = row[3]
                    case 'Duration':
                        oldResult = row[4]
                    case _:
                        oldResult = row[5]
                    
                updatedResult = input(f'Enter updated film {field} value: ')
            
            dbCursor.execute(f'UPDATE tblFilms SET {field} = ? WHERE filmID = {filmID}', (updatedResult,))
            dbCon.commit()  
            print(f'{row[1]} -- Successfully updated {field} from \'{oldResult}\' to \'{updatedResult}\'')
    
    except sql.OperationalError as oe:
        print(f'Operational Error: {oe}')
    except sql.Error as e:
        print(f'Error: {e}')
    except sql.ProgrammingError as pe:
        print(f'Programming Error: {pe}')

if __name__ == '__main__':
    update_film()