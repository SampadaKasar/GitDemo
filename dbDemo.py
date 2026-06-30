import mysql.connector
from mysql.connector import cursor
from utilities.configurations import *
# conn = mysql.connector.connect(host="localhost" , database="apidevelop" , user="root" , password="root")
conn = getConnection()
print(conn.is_connected())
cursor=conn.cursor()             #method to streamline connection to talk to the database table ,basically object to execute SQL queries and fetch the results
cursor.execute("select * from CustomerInfo;")
# first_Row=cursor.fetchone()
# print(first_Row)   # in SQL Database results are returned in form of tuples
# print(first_Row[2])
# all_rows = cursor.fetchall()   #now it will fetch records from second row
# #simply if we want to use fetchall method don't use fetchone method
# print(all_rows)  #list of tuples
# print(all_rows[2][1])

rows = cursor.fetchall()
print(type(rows))
sum=0
for row in rows:
    sum=sum+row[2]
print(sum)
assert sum == 340
query = "update customerInfo set Location = %s where CourseName = %s"   # this is how we parameterize SQL
# %s = one query will come and replace the respective values here. query should be generic and not hardcoded

#as output is always in tuple format then
data = ("Indonesia" , "Appium")
cursor.execute(query, data)
conn.commit()# to save changes permanently
conn.close() # Resource leakage / performance issues if not closed

#Notes: Q: Why create DB connection? ( conn = mysql.connector.connect() )== To allow Python scripts to execute SQL queries on the database.
#Cursor is used to: execute SQL queries, fetch results
#Q: Difference between connection and cursor? === 1) Connection = connects to DB 2) Cursor = runs SQL commands
#Important: After INSERT/UPDATE/DELETE use: conn.commit() Because without commit changes may not persist in DB
#fetchone() - Returns one row & fetchall() - Returns all rows
#Must-Know SQL for API Automation
#SELECT * FROM books;
#SELECT * FROM users WHERE isbn="cricket";
#insert into books VALUES ('Destiny', 'cricket' , 7 , 'MSD');
#UPDATE books SET BOOKNAME = "DhoniStory where isbn = "cricket";
#DELETE FROM books WHERE isbn = "cricket";
#SELECT COUNT(*) FROM books;
#SELECT * FROM books ORDER BY aisle ASC; -- Ascending
#SELECT * FROM books ORDER BY aisle DESC;  -- Descending:
#select max(aisle) FROM books;
#Q1: Why database validation in API testing? - To verify backend data consistency after API operations
#Q2: Which Python library connects to MySQL? - Examples: mysql-connector-python & pymysql
#Q3: Why utility file for DB? - Avoid duplicate code.
#Q4: What if query fails? - Use exception handling
try:
    cursor.execute(query)
except Exception as e:
    print(e)

#need to do practice more on python UI automation










