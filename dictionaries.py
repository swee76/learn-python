# Dictionaries
# Key value pair

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# One way to get the value of dictionary
print(monthConversions["Jan"])

# another way to get the value of dictionary
print(monthConversions.get("Dec"))

# undetectable key search, default value is given
print(monthConversions.get("Luv", "Not a valid key"))

# not only strings, but also numbers can be used as key of a value in dictionary
colorList = {
    0: "Black",
    1: "White",
    2: "yellow",
    3: "Red",
    4: "Orange",
    5: "Green",
    6: "Blue"
}

print(colorList[1])
print(colorList.get(4))
print(colorList.get(10, "Not in range"))
