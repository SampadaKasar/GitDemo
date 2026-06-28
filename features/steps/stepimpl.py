import requests
from behave import *
from payload import *
from utilities.configurations import *
from utilities.resources import *

@given('the Book details which needs to be added to library')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + APIResources.addBook  # separated variable and string with + operator
    context.headers = {'Content-Type': 'application/json'}
    # isbn = "Dhoni" + str(random.randint(1000,9999))       #Prevent duplicate test data.
    #context.query = "select * from Books"
    #context.payload = buildPayLoadFromDB(context.query)
    context.payload = addPayload("sdfyg" , 4569)


@when('we execute the AddBook Post method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    addbook_json = context.response.json()
    print(addbook_json)
    print(context.response.status_code)
    print(context.response.text)
    context.bookId = addbook_json['ID']
    print(context.bookId)
    assert addbook_json["Msg"] == "successfully added"

@given('the Book details with {isbn} and {aisle}')
def step_impl(context , isbn , aisle):
    context.url = get_config()['API']['endpoint'] + APIResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payload = addPayload(isbn, aisle)


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()  # method used to create one session
    context.se.auth = auth = ('SampadaKasar', getPassword())

@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(APIResources.githubRepo)


@then('status code of response should be {statusCode:d}')  # :d it treats as integer as status code is 200
def step_impl(context , statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
