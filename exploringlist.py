#List are created like this-
IPLTEAMS = ["KKR", "SRH", "MI", "RCB", "CSK", "RR", "DC"]
print(IPLTEAMS)

#List Items
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

#Ordered
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.

#Changeable
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#Allow Duplicates
#Since lists are indexed, lists can have items with the same value:
list2 = ["apple", "banana", "watermelon", "apple", "banana", "Cherry"]
print(list2)

#List Length
#To determine how many items a list has, use the len() function:

list3 = ["apple", "banana", "watermelon"]
print(len(list3))

#List Items - Data Types
#List items can be of any data type:

listInt = [56, 49, 1, 7, 33, 55, 77]
listString = ["India", "Austrila", "England"]
listBoolean = [True, False, True]

#A list can contain different data types:

list4 = ["Wasim", "Bsc.IT", 39, "TY.IT", True]

#Access Items
#List items are indexed and you can access them by referring to the index number:

print(list4[0:3])

#Change Item Value

favPlayers = ["Manish Pandey", "Andre Russell", "Sunil Narine", "Cameron Green", "Karim Benzema"]
favPlayers[4]="Angrkish Raguvanshi"
print(favPlayers)

#insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#The insert() method inserts an item at the specified index:

favColors=["Purple", "Black", "White"]
favColors.insert(3, "Red")
print(favColors)

#Append Items
#To add an item to the end of the list, use the append() method:

favSports = ["Cricket", "MMA", "Football"]
favSports.append("BasketBall")
print(favSports)

#Extend List
#To append elements from another list to the current list, use the extend() method.

listA = ["Finn Allen", "Angkrish", "Cameron Green"]
listB = ["Tim Seiferit", "Sarthak Ranjan", "Rachin Ravindra"]
listA.extend(listB)
print(listA)
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

#Remove Specified Item
#The remove() method removes the specified item.
#If there are more than one item with the specified value, the remove() method removes the first occurrence.

abc = [23, 55, 77, 7, 5, 1]
abc.remove(7)
print(abc)

#Remove Specified Index
#The pop() method removes the specified index.
#If you do not specify the index, the pop() method removes the last item.
poptheIDX = ["Royal Enfield", "KTM", "YAHAMA", "Spelndor"]
poptheIDX.pop(1)
print(poptheIDX)

#Clear the List
#The clear() method empties the list.
#The list still remains, but it has no content.

clearList = ["Pogba", "Messi", "Jude", "Karim Benzema"]
clearList.clear()
print(clearList) 
