# Working with lists

friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]
print(friends)

print(friends[0])

print(friends[-2])
# negative index print values from end of the array
# This feature is not in the Javascript

# Given index position, and all elements in array after it, will print out
print(friends[1:])

# To print specific index range to print
print(friends[1:4])

# Modify values inside the array

friends[2] = "Mike"
print(friends[2])