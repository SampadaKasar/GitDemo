import requests
from utilities.configurations import *
from utilities.resources import *

def after_scenario(context, scenario):
    if "library" in scenario.tags:
        context.url2 = get_config()['API']['endpoint'] + APIResources.deleteBook

        deleteBook_response = requests.post(
            context.url2,
            json={"ID": context.bookId},
            headers=context.headers
        )

        print(deleteBook_response.status_code)
        print(deleteBook_response.text)

        assert deleteBook_response.status_code == 200

        deletebook_json = deleteBook_response.json()
        print(deletebook_json["msg"])

        assert deletebook_json["msg"] == "book is successfully deleted"

# Another solution for github becasue book was getting deleted everytime and it gave error.
# def after_scenario(context, scenario):
#     if not hasattr(context, "bookId"):
#         return
#
#     context.url2 = get_config()['API']['endpoint'] + APIResources.deleteBook
#
#     deleteBook_response = requests.post(
#         context.url2,
#         json={"ID": context.bookId},
#         headers=context.headers,
#     )
#
#     print(deleteBook_response.status_code)
#     print(deleteBook_response.text)
#
#     assert deleteBook_response.status_code == 200
#     deletebook_json = deleteBook_response.json()
#     assert deletebook_json["msg"] == "book is successfully deleted"
