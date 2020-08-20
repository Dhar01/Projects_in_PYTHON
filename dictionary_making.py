import json
from difflib import get_close_matches   # for smarting the program

""" This is a project from an udemy course """

data = json.load(open("data.json"))

def translation(word):
    # for various uppercase input
    word = word.lower()

    # for checking the availability
    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        """ For guessing the close correct word """
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        yn = yn.lower()

        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please check it again"
        else:
            return "We didn't understand your entry"

    else:
        return "The word doesn't exist. Please check it again!"

# initial part

word = input("Enter word: ")

output = translation(word)

# print output

if type(output) == list:        # for showing every meaning
    for item in output:
        print(item)
else:
    print(output)