import DB
db = DB.DatabaseConnection()
#import Bibliothek
from faker import Faker
fake = Faker('de_DE')

#Start der Matrikelnummer
matrikelnummer = 5000

# Studierende erstellen
for _ in range(1000):
    matrikelnummer += 1
    name = fake.first_name()
    nachname = fake.last_name_female()
    birday = fake.date(pattern="%d-%m-%Y", end_datetime="-20y")

    data = (matrikelnummer, name+" "+nachname, birday)

    try:
        db.create_student(data)
    except Exception as e:
        pass




#Prüfungen und Noten erstellen
for __ in range(1,500,1):
    matrikelnummer = fake.random_int(min=5020, max=6000)

    note = fake.random_element(elements=('1.0', '1.3', '1.7', '2.0', '2.3', '2.7', '3.0', '3.3', '3.7', '4.0', '5.0'))

    prfnr = fake.random_element(elements=('1', '2', '3', '4', '6', '7', '8', '9', '10', '11', '12'))

    data = (float(note), int(prfnr), matrikelnummer)

    try:
        db.insert_note(data)
    except Exception as e:
        pass
