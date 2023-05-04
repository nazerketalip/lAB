import psycopg2
from config import data

db = psycopg2.connect(**data)
cursor = db.cursor()

sql = '''

        CREATE TABLE phonebook(
            number SERIAL PRIMARY KAY,
            username TEXT NOT NULL,
            telephone_number BIGINT NOT NULL,
            city TEXT NOT NULL
    )
'''
cursor.execute(sql)

cursor.close()
db.commit()
db.close()