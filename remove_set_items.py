# thisset= {'orange','kiwi','mango'} #remove set items
# thisset.remove('mango') #Note: If the item to remove does not exist, remove() will raise an error.
# print(thisset) #To remove an item in a set, use the remove(), or the discard() method.

# thisset= {'orange','kiwi','mango'} #discard set items
# thisset.discard('kiwi')
# print(thisset) #Note: If the item to remove does not exist, discard() will NOT raise an error.


     ##You can also use the pop() method to remove an item, but this method will remove a random item,
#      ## so you cannot be sure what item that gets removed.
# thisset= {'orange','kiwi','mango'}
# x=thisset.pop()
# print(x) #The return value of the pop() method is the removed item.
# print(thisset)

# thisset= {'orange','kiwi','mango'} #clear() method empies the set
# thisset.clear()
# print(thisset)

thisset= {'orange','kiwi','mango'} #The del keyword will delete the set completely:
del thisset



