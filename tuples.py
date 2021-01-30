#CREATE AN EMPTY TUPLE
thistuple = ("")
print(thistuple)

#CREATE TUPLE WITH HOMOGENEOUS ELEMENTS
thistupleHo = ("apple", "orange", "grape")
print(thistupleHo)

#CREATE TUPLE WITH HETEROGENEOUS ELEMENTS
thistupleHe = ("apple", 7, "orange")
print(thistupleHe)

#CREATE TUPLE WITH SINGLE ELEMENT
thistupleS = (7)
print(thistupleS)

#MODIFY A TUPLE (ERROR)
#thistuple = (7,8,9)
#thistuple[0]=5
#print(thistuple)

#ACCESSING ELEMENTS OF TUPLE - FROM THE FRONT
print(thistupleHo[0])

#ACCESSING ELEMENTS OF TUPLE - FROM THE BACK
print(thistupleHo[-1])

#SEARCH WITHIN A TUPLE
if "apple" in thistupleHo:
    print("Value is present")

#ADD ELEMENTS TO A TUPLE (ERROR)
#thistupleHo
#del thistupleHo
#print(thistupleHo)

#

