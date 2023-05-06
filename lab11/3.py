
import psycopg2
from psycopg2 import Error
import re
contacts = [
    (8, 'Aruzhan', '7777777777'),
    (9, 'Aruka', '7777777777'),
    (10, 'NAZ', '7777777777'),
    (11, 'Dayana', '7777777777'), # incorrect_values
]
incorrect_values = []
pattern = r'^8777[0-9]{7}$|^8747[0-9]{7}$|^8778[0-9]{7}$|^8700[0-9]{7}$|^8707[0-9]{7}$|^8708[0-9]{7}$|^8705[0-9]{7}$|^8775[0-9]{7}$'
for i in contacts:
    if re.search(pattern, i[2]) == None:
        contacts.remove(i)
        incorrect_values.append(i)
try:
    connection = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='NNNaigul77'
    )

    cursor = connection.cursor()
    cursor.executemany('CALL add_user(%s, %s, %s)', contacts)
    connection.commit()

except (Exception, Error) as error:
    print("ERROR", error)
finally:
    if connection:
        cursor.close()
        connection.close()
print(f'List of incorrect values is: {incorrect_values}')