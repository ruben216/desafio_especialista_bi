import mysql.connector

con = mysql.connector.connect(
    user='root',
    host='172.17.0.2',
    port='3306',
    database='IBGE'
)

cursor = con.cursor()

cursor.execute('SELECT * FROM CNT')

CNT = cursor.fetchall()

for cnt in CNT:
    print(cnt)


