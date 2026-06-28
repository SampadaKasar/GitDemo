import mysql.connector
#Practice-1
connection = mysql.connector.connect(host="localhost" , database="apidevelop" , user="root" , password="root")
cursor = connection.cursor()
query = "select * from CustomerInfo;" #just example
cursor.execute(query)
all_rows = cursor.fetchall()
#Q1  - SELECT * FROM books;
#Q2 - SELECT BookName , author FROM books;
#Q3 SELECT * FROM books where BOOKNAME = "Selenium";
#Q4 SELECT * FROM books where author = "Rahul Shetty";
#Q5 SELECT * FROM books where aisle > 50;
#Q6 SELECT COUNT(*) FROM books
#Q9 query = UPDATE books SET author = %s where BOOKNAME = %S
# results = ('Mahendra Singh Dhoni' , 'DhoniStory') # as it is tuple
#Q10 DELETE FROM books where BOOKNAME = "Jmeter";
#Q11 all_rows = cursor.fetchall()
#Q12
for row in all_rows:
    print(row[0])
#Q13
def get_book_by_name(book_name):
    query = "SELECT * FROM books WHERE BookName = %S"
    cursor.execute(query, (book_name,))
    return cursor.fetchone()
print(get_book_by_name("Devops"))

#Q14
query = "SELECT * FROM books WHERE BookName = %s"
data = ("selenium", )
cursor.execute(query, data)
row = cursor.fetchone()
#Q15
query = "SELECT * FROM books WHERE BookName=%s"
cursor.execute(query, ("DhoniStory",))
row = cursor.fetchone()
print(row)
#Q16 How do you validate API response with database?



#Q18 After api calls, we can assert response.statuscode again we can print response.text or else can assert success msg text
#Q19 Cursor is use to streamline the connection to talk to the database tables basically  to executes SQL Commands using execute() method, fetch results etc
#Q20  fetchone() - fetch single row and fetchall() - fetch all rows
#Q21 use %s placeholders  to avoid hardcoding of values basically to parameterize SQL
#Q22  closing db connections is mandatory to avoid resource leak issues and performance issues
#Q23 to save changes permanently in DB commit is used after update
