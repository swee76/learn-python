# Array Functions

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Keren", "Jim", "Oscar", "Toby"]

friends.extend(lucky_numbers)
print(friends)
# in javascript this will be friends.concat(lucky_numbers)

friends.append("Creed")
print(friends)
# in javascript this will be friends.pussh("Creed")

friends.insert(1, "Kelly")
print(friends)
# in javascript this will be friends.splice(1,0,"Kelly)
# 1 is the index where you want to insert the value
# 0 means don't replace  the existing value at the specific index and
# shift it forward one position with other remaining after it

# if we put friends.splice(1,1,"Kelly")
# This replaces the value with given position value
