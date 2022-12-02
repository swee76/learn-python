# Array Functions

lucky_numbers = [14, 8, 15, 16, 23, 42]
friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]

friends.extend(lucky_numbers)
print(friends)
# in javascript this will be friends.concat(lucky_numbers)

friends.append("Creed")
print(friends)
# in javascript this will be friends.pussh("Creed")

friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)
# in javascript this will be friends.splice(1,0,"Kelly)
# 1 is the index where you want to insert the value
# 0 means don't replace  the existing value at the specific index and
# shift it forward one position with other remaining after it

# if we put friends.splice(1,1,"Kelly")
# This replaces the value with given position value

friends.remove("Jim")
print(friends)
# in Javascript this will be friends.splice(2,1,"Jim") - this remove the element but have to give the index
# To remove element by only giving the value of the element use filter()
# friends.filter((person)=> person != "Jim")

friends.pop()
print(friends)
# This removes the last element of the array same as the Javascript

# friends.clear()
# print(friends)
# remove every single item from the array (whole)

friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]
print(friends.index("Toby"))
# in javascript this will be friends.indexOf("Toby")

# Add a same named element to the list
friends.append("Oscar")
print(friends)

print(friends.count("Oscar"))
# This returns the no of items that have the given same value

fruits = ["Banana", "Mango", "Apple", "Pineapple", "Papaya"]
fruits.sort()
print(sorted(fruits))
# This cannot be typed in same line as print(sorted(fruits.sort()))
# we have to sort the list in a new line and print the sorted list in another line by using sorted(array_name)
# Otherwise if we try to print just after sort() the list it prints None

lucky_numbers.sort()
print(sorted(lucky_numbers))

lucky_numbers = [14, 8, 315, 16, 23, 42]
lucky_numbers.reverse()
print(lucky_numbers)
# This reverse() the array from Last to first element without sorting
# Javascript also have reverse()

friend_list = friends.copy()
print("Copied Array: " + str(friend_list))
# in javascript this will be friendList = friends.copyWithin()
