import mysql.connector
import re

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'adminadmin',
    database = 'vocab'
)
cursor = conn.cursor()
cursor.excute('SHOW DATABASES')

found = False
for db in cursor:
    pattern = "[(,')]"
    db_string = re.sub(pattern,"", str(db))

    if(db_string == 'vocab'):
        found = True
        print ('database vocab exists')
if (not found):
    cursor.excute('CREATE DATABASE vocab')

sql = 'DROP DATABASE IF EXISTS vocab_table'
cursor.excute(sql)

sql = 'CREATE TABLE vocab_table(word VARCHAR(255), definition VARCHAR(255))'
cursor.excute(sql)

fh = open('Vocabulary_list.csv', 'r')
wd_set = fh.readlines()
# print(wd_set)
#  remove the header
wd_set.pop(0)
# task 2 prepare the json list
vocab_list = []

for rawstring in wd_set:
    word, definition = rawstring.split(',', 1)
    # remove newline from string
    definition = definition.rstrip()
    vocab_list.append({word, definition})
    sql = 'INSERT INTO vocab_table(word, definition) VALUES(%s, %s)'
    values = (word, definition)
    cursor.excute(sql, values)

    conn.commit()
    print( 'Inserted' + str(cursor.rowcount) + 'row into vocab_table')

sql = 'SELECT * from vocab_table WHERE word = %s'

value = ('boisterous',)
cursor.excute(sql, value)

result = cursor.fetchall()

for row in result:
    print(row)

sql = 'UPDATE vocab_table SET definition %s WHERE word = %s'
value = ('spirited; lively', 'boisterous')
cursor.excute(sql, value)

conn.commit()
print('Modified row count:', cursor.rowcount)
sql = 'SELECT * FROM vocab_table WHERE word = %s'
value = ('boisterous')
cursor.excute(sql, value)
result = cursor.fetchall()

for row in result:
    print((row))

#print(vocab_list)