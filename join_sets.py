   #There are several ways to join two or more sets in Python.
   #You can use the union() method that returns a new set containing all items from both sets,
   #or the update() method that inserts all the items from one set into another:
# thisset1= {'orange','kiwi','mango'} #Join 2 sets
# thisset2= {1,2,3}
# newset= thisset1.union(thisset2) #join 2 sets using union() method:
# print(newset) #The union() method returns a new set with all items from both sets:

# thisset1= {'orange','kiwi','mango'}
# thisset2= {1,2,3}
# thisset1.update(thisset2) #The update() method inserts the items in thisset2 into thisset1:
# print(thisset1)  #Note: Both union() and update() will exclude any duplicate items.


# set1= {'orange','kiwi','mango'} #Keep only the duplicates
# set2= {'apple','mango','banana'}
# set1.intersection_update(set2) #The intersection_update() method will keep only the items that are present in both sets.
# print(set1)

# set1= {'orange','kiwi','mango'}
# set2= {'apple','mango','banana'}
# set3 = set1.intersection(set2)
# print(set3) #The intersection() method will return a new set, that only contains the items that are present in both sets.

# set1= {'orange','kiwi','mango'}#Keep All, But NOT the Duplicates
# set2= {'apple','mango','banana'}
# set1.symmetric_difference_update(set2)
# print(set1) #The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

# set1= {'orange','kiwi','mango'}
# set2= {'apple','mango','banana'}
# set3= set1.symmetric_difference(set2)  #The symmetric_difference() method will return a new set,
# print(set3) # that contains only the elements that are NOT present in both sets.

set1={'jiyad',10,True}
set2={2,1,'muhammed'}  #Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
set3=set1.symmetric_difference(set2)
print(set3) #True and 1 is considered the same value: