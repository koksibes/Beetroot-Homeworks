import json
from json.decoder import JSONDecodeError


def contact_searcher(search_data):
    search_result = {}
    with open("phonebook.json") as fp:
        try:
            pb = json.load(fp)
            for i in pb:
                for j in pb[i]:
                    if search_data in pb[i][j].lower():
                        search_result.update({i: pb[i]})
            return search_result
        except JSONDecodeError:
            return "Phonebook is empty"


result = contact_searcher(input("Search "))
print(result)
