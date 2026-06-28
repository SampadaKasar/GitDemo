import json
courses = '{"class": 9 , "subjects" : ["english" , "marathi"]}'
#The json.loads() method is used to convert a JSON string into a Python object
dict_Courses = json.loads(courses) #loads method for string argument
print(type(dict_Courses))
print(dict_Courses)
print(dict_Courses['class'])
print(dict_Courses['subjects'])
subject_list = dict_Courses['subjects']
print(subject_list[0])
#simple way
print(dict_Courses['subjects'][1])

with open("C:\\Users\\Admin\\Downloads\\complex_sample.json") as f:
    jsondata = json.load(f)   #load method for file object
    print(jsondata)
    print(type(jsondata))
    print(jsondata['organization']['name'])
    print(jsondata['users'][0]['username'])    #when list is there then its index bases so [0]
    print(jsondata['system']['features']['multiRegion'])   #when direct dictionary is there we can access directly
    print(jsondata['organization']['departments'][0]['manager']['name'])

    #loop concept when order is not fixed in the list how to get relevant data
    for user in jsondata['users']:
        if user['userId'] == 503:
            print(user['username'])
            assert user['username'] == "mukund"

with open("C:\\Users\\Admin\\Downloads\\complex_sample1.json") as f2:      #f2 is object
    jsondata1 = json.load(f2)
    assert jsondata == jsondata1 #it will give assertion error
    #print(jsondata == jsondata1) -------- will print either true or false in output
