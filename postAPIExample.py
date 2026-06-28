import json
import time
import configparser    #import this pkg and then from this pkg call the method and save it in one object
#configparser is a built-in Python module used to read configuration/settings files, usually .ini files.

import requests
import random
from payload import *
from utilities.configurations import *
from utilities.resources import *
from requests import auth
#addbook
url = get_config()['API']['endpoint'] + APIResources.addBook    #separated variable and string with + operator
headers = {'Content-Type': 'application/json'}
# isbn = "Dhoni" + str(random.randint(1000,9999))       #Prevent duplicate test data.
query = "select * from Books"
addBook_response = requests.post(url, json=buildPayLoadFromDB(query), headers=headers , )

print(addBook_response.status_code)
print(addBook_response.text)
addbook_json = addBook_response.json()
print(addbook_json)
bookId = addbook_json['ID']
print(bookId)

#deletebook
url2 = get_config()['API']['endpoint'] + APIResources.deleteBook
print("Delete URL:", url2)
print("Delete Payload:", {"ID": bookId})
deleteBook_response = requests.post(url2,
                                    json={"ID": bookId}, headers=headers,)
print(deleteBook_response.status_code)
print(deleteBook_response.text)
assert deleteBook_response.status_code == 200
deletebook_json = deleteBook_response.json()
print(deletebook_json["msg"])
#assert deletebook_json["msg"] == "book is successfully deleted"
#
# #authentication
# #GitHub's API simply doesn't accept passwords for authentication anymore. The PAT is the modern replacement for API access.
se=requests.session()    #method used to create one session
se.auth = auth=('SampadaKasar' , getPassword())
url = "https://api.github.com/user"

token = getPassword()      # Your GitHub Personal Access Token

headers = {
    "Authorization": f"Bearer {token}",            #GitHub no longer supports password-based authentication for REST APIs. A Personal Access Token (PAT) must be used instead.
    "Accept": "application/vnd.github+json"
}

github_response = requests.get(
    url,
    headers=headers
)

print(github_response.status_code)
print(github_response.text)

url2 = "https://api.github.com/user/repos"
response = se.get(url2)    #no need of authentication here again
#difference between se.get and request.get = in se.get no need of authentication again
print(response.status_code)