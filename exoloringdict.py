#Dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

myDict = {
    "Name": "Wasim Patel",
    "Course": "Bsc.IT",
    "Roll no": 39,
    "Class": "SY.IT",
    "favSubject": "DBMS"
}
print(myDict)

#Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets:

x = myDict["Name"]
print(x)

#Change Values
#You can change the value of a specific item by referring to its key name:

myDict["Class"] = "TY.IT"
print(myDict)

#Removing Items
#The pop() method removes the item with the specified key name:

myDict.pop("favSubject")
print(myDict)

#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.

myFamily = {
    "child1":{
        "name": "Usman",
        "year": "2030"
    },
    "child2":{
            "name": "Arslan",
            "year": "2030"
        },
    "child3":{
            "name": "Haya",
            "year": "2031"
        }
}