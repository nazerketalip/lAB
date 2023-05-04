import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='NNNaigul77'
)

current = config.cursor()
# добавляем значения в таблицу
id = 1
name = 'Nazerke'
number = '87781078121'

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()