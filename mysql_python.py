import mysql.connector

# ЗАВДАННЯ:
# 1. Створити нову базу даних 'my_first_db'.
# 2. Створити в цій базі даних таблицi:
#       'student' з полями: 'id' (INT) i 'name' (VARCHAR(255));
#       'employee' з полями: 'id' (INT_AUTO_INCREMENT PRIMARY KEY) ,
#       'name' (VARCHAR(255)) i 'salary' (INT(6))
# 3. Змінити у таблиці 'student' поле 'id' на PRIMARY KEY.
# 4. Додати до таблиці 'student' такі дані: (01, 'John').
# 5. Додати до таблиці 'employee' такі дані:  (01, 'John', 1000).


# Створюю коннектор.
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Oleksiisql1985',
    database='my_first_db'
)


# 1. Створюю базу даних 'my_first_db'.
mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE my_first_db')


# 2. Створюю таблицю 'student' з полями: 'id' (INT) i 'name' (VARCHAR(255)).
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE student (id INT, name VARCHAR(255))')


# 2. Створюю таблицю 'employee' з полями:'id' (INT_AUTO_INCREMENT PRIMARY KEY),
# 'name' (VARCHAR(255)) i 'salary' (INT(6))
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, '
                 'name VARCHAR(255), salary INT(6))')


# 3. Змінюю у таблиці 'student' поле 'id' на PRIMARY KEY.
mycursor = mydb.cursor()
mycursor.execute('ALTER TABLE student DROP id, '
                 'ADD id INT AUTO_INCREMENT PRIMARY KEY')


# 4. Додаю до таблиці 'student' такі дані: (01, 'John').
mycursor = mydb.cursor()
sql = 'INSERT INTO student (id, name) VALUES (%s, %s)'
val = (1, 'John')
mycursor.execute(sql, val)


# 5. Додаю до таблиці 'employee' такі дані: (01, 'John', 1000).
mycursor = mydb.cursor()
sql = 'INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)'
val = (1, 'John', 1000)
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, 'record inserted.')
