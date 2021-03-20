import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y for Yes, or N for No: " % get_close_matches(word, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn =="n":
            return "Word not found. Please try again."
        else:
            return "Impermissible entry!"
    else:
        return("Word not found. Please try again.")

word = input("Enter word: ")

output = (definition(word))

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)