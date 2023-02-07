# Oscar Chiqui - Simple SQlite Application | Capstone Lab 5

"""
Start code with menu: https://gist.github.com/claraj/13a8b31b73b8cfec9c4e665cdc70d39e

I build the same program using Peewee 


"""

from peewee import *

db = SqliteDatabase('juggling_records.sqlite')

class Juggler(Model):

    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db
    
    def __str__(self):

        return f'ID: {self.id} | {self.name} | {self.country} | {self.catches}'

db.connect()
db.create_tables([Juggler])

Juggler.delete().execute()

janne_Mustonen = Juggler(name = 'Janne Mustonen', country = 'Finland', catches = 98)
janne_Mustonen.save()

ian_stewart = Juggler(name = 'Ian Stewart', country = 'Canada', catches = 94)
ian_stewart.save()

aaron_Gregg = Juggler(name = 'Aaron Gregg', country = 'Canada', catches = 88)
aaron_Gregg.save()

chad_taylor = Juggler(name = 'Chad Taylor', country = 'USA', catches = 78)
chad_taylor.save()



def main():

    while True:
        try:
            display_menu()
            choice = int(input('Enter choice:'))

            if choice == 1:
                add()
            elif choice == 2:
                search()
            elif choice == 3:
                update()
            elif choice == 4:
                delete()
            elif choice == 5:
                display_all_jugglers()
            elif choice == 6:
                print('Good bye')
                break
            else:
                print('\nNot a valid choice.\n')
        except ValueError as e:
            print('\nPlease enter a numeric choice')

def display_menu():
    print('1: Add new record')
    print('2: Search record')
    print('3: Update Record')
    print('4: Delete record')
    print('5: Display records on the table')
    print('6: Exit')

def add():
    add_name = input('Enter juggler name: ').title()
    add_country = input('Enter country:').upper()
    add_catches = int(input('Enter number of catches'))

    add_to_record = Juggler(name = add_name, country = add_country, catches = add_catches)
    add_to_record.save()

def search():
    search_name = input('Enter full name to search: ').title()
    search_record = Juggler.select().where(Juggler.name == search_name).execute()

    for record in search_record:
        print(f'Record found - {record}.')
        break
        
    else:
        print(f'No record found under name: {search_name}')

def update():
    update_by_name = input('Enter juggler name to update record:').title()
    update_catches = int(input('Enter number of new catches:'))

    rows_updated = Juggler.update(catches = update_catches).where(Juggler.name == update_by_name)
    if rows_updated == 0:
        print(f'No record was found under name: {update_by_name}.')

    else:
        print(f'Record under name {update_by_name} has been updated to {update_catches}.')


    