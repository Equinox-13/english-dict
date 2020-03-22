import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def fetch_meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y if Yes, or N if No:"%(get_close_matches(word,data.keys(),cutoff=0.8)[0]))
        if yn == "Y":
            return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understood your input."
    else:
        return "The word doesn't exist. Please double check it."

word  = input("Enter a word:")
result = fetch_meaning(word)
if type(result) == list:
    for each in result:
        print(each)
else:
    print(result)

