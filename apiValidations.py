import requests

response = requests.get('http://216.10.245.166//Library/GetBook.php',
             params= {"AuthorName" : 'Rahul Shetty'},)   #mandatory to pass all params in dictionary format
print(response.text)
print(type(response.text))
json_response = response.json()
#response.json() saves time because it:
# Automatically parses JSON
# Converts data into Python objects
# Reduces manual parsing
# Makes automation scripts cleaner
print(type(json_response))
print(json_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
for actualbook in response.json():
    if actualbook['isbn'] == "RS792":
        print(actualbook)
        break             #Without break, loop continues and it may take lastbook as actualbook and assertion will fail

expectedbook = {
        "book_name": "Learn Appium Automation with Java 21",
        "isbn": "RS792",
        "aisle": "1111"
    }

assert actualbook == expectedbook
