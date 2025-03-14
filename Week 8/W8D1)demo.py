#W8D1 - Introduction to Dictionaries

#Dictionaries in Python are a collection set similar to associative arrays in JavaScript but also look similar to JS object builds. Most importantly, they store data in key and value pairs. They keys are referred to as properties and the values can be any data type. 

#---IMPORTS-----------------------------------------------------

#---MAIN EXECUTING CODE-----------------------------------------

#start by creating a populated dictionary 
myCar = {
    #'key' : value, 
    "make": "Ford",
    "model": " Focus SE Hatchback",
    "year": 2014,
    "name": "Gwendoline",
    "color": "black",
    #keys cannot be repeated/NO DUPLICATES allowed
    #repeats will replace first value,see 'color' key below in print
    "color" : "red"
}

#display the entire dictionary -> 'myCar'
print(myCar)

#display just the 'make' and 'model' values of the dictionary 'myCar'

#dictionaryName["keyName"] --> accesses stored value
#"keyName" will always be a STRING index, created by developer
print(f"My car is a {myCar["make"]} {myCar["model"]}{myCar['color']}")


yourCar = {
    #key : value,
    "make": "Ford",
    "model": "F-150",
    "year": 2024,
    "name": "Gandalf",
    "color": "black",
    "friends" : ["Tyler","Tony","Steve"]
}

print (yourCar)
print(f"My car is a {yourCar["make"]} {yourCar["model"]}{yourCar['color']}")

#add some data to a dictionary once created
yourCar["plate"] = "12345"

#or use the .update({key:value}) method
yourCar.update({"wheels": "4"})

for key in yourCar:
    #for every key stored to the yourCar dictionary
    print(f"{key.upper():10}\t {yourCar[key]}")