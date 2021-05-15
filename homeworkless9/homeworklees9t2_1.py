import json
from json.decoder import JSONDecodeError
import pprint

def contact_searcher(search_data):
    search_result = []
    with open("homeworkless9\phonebook.json") as fp:
        try:
            pb = json.load(fp)
            for i in pb:
                for j in i.values():
                    if search_data in j:
                        search_result.append(i)
                        break
            return search_result
        except JSONDecodeError:
            return "Phonebook is empty"

result = contact_searcher(input("Search "))
pprint.pprint(result)
