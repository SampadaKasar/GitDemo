numbers = [10,20,30,40,50]
for number in numbers:
    if number>25:
        print(number)

data = {
    "user": {
        "name": "John",
        "age": 25
    }
}

# Print John
print(data["user"]["name"])

#example-3
import requests
headers = {"Authorization": "Bearer Token "}
response = requests.get("https://jsonplaceholder.typicode.com/posts/1" , headers=headers,)
print(response.status_code)
json_response = response.json()

#example 4 - Mini project
# Mini Project (Best Confidence Test)
#
# Build this without watching the course:
#
# Call a public API:
#
# https://jsonplaceholder.typicode.com/users
# Get the JSON response.
# Print:
# User name
# Email
# City
# Save the response to users.json.
# Read users.json back and print the first user's name.
#
# If you can complete this in 20–30 minutes on your own, you're ready to proceed.
#
# Even Better: API Automation Challenge
#
# Write a script that:
#
# 1. Sends GET request
# 2. Checks status code = 200
# 3. Extracts JSON data
# 4. Validates a field
# 5. Saves response to file
# 6. Handles exceptions
import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])
    print("-" * 30)

# Save to file
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)   #converts a Python object into JSON format and writes it directly to a file.
#makes the JSON nicely formatted with 4 spaces of indentation.
# Read back
with open("users.json", "r") as file:
    data = json.load(file)

print("First User:", data[0]["name"])
#test
# 1. A
# 2. 1,2,3,4
# 3. print(user["name"])
# 4. Below is the solution
def find_square(number):
    return number*number
print(find_square(5))
# 5. List - mutable and stores values list uses = [] and tuples uses = () and Dict - key value pairs
#Section - B
# 6.
data = {
    "employee": {
        "name": "Rahul",
        "salary": 50000,
        "city": "Delhi"
    }
}
for record in data:
    print(data["employee"]["name"])
# 7.
    print(data["employee"]["city"])
# 8. Javascript Object Notation
# 9 . GET
# 10. Success
# 11. Not Found
# 12.
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)
# 13.
response = requests.get(url)

# Complete this
data = response.json()
# 14.
assert response.status_code == 200

# 15. Basically API is application programming interface, and it allows two applications to communicate by exchanging requests and responses like frontend-API-Database
# 16. GET-Retrieve the data and POST-create the data and put for update the data and delete for delete the data
# 17. Headers carry metadata about the request, such as Authorization tokens, Content-Type, Accept, User-Agent, etc.
# 18. OAuth - primarlily Authorization framework that allows application to access resources on behalf of user without sharing user's password, it commonly uses access token
# 19. exception handling - to take care of failures so that code should run succesfully , whatever the test is we write in try block and handles the exception in except block
# 20.
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
assert response.status_code == 200
json_response = response.json()
print(json_response)
#exception handling -
try:
    division = 10/0
except ZeroDivisionError:
    print("can not divide by zero")