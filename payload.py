from utilities.configurations import *


def addPayload(isbn , aisle):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Sampada Kasar"
    }
    return body

def buildPayLoadFromDB(query):
    addBody={}
    tp = getQuery(query)   #this getQuery method will return a record which is in the form of tuple
    addBody['name'] = tp[0] # this is How we read specific column values - using indexes
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody