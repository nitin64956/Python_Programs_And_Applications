import json
from difflib import get_close_matches

data  = json.load(open("data.json"))

def translate(val):
    val = val.lower()
    if val in data:
        return data[val]

    elif val.title() in data:
        return data[val.title()]

    elif val.upper() in data:
        return data[val.upper()]    

    elif len(get_close_matches(val,data.keys())) > 0:    
        yn =  input("Did You Mean %s ? Enter 'Y' if yes or 'N' if no: " % get_close_matches(val,data.keys())[0])
        if yn == "Y": 
            return data[get_close_matches(val,data.keys())[0]]
        elif yn =="N":
            return "The word doesn't Exist, Please double check it"
        else:
            return "We didin't understand your Entry"

    else:
        return "The word doesn't Exist, Please double check it"    

word = input("Enter Your Word To Search: ")

output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)        

