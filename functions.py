# learn functions in python

def sayhi():
    print("Hello User")


print("Before func call")
sayhi()
print("After func call")


# In python function specifies using def keyword
# And no need to write a camelcase function name - use lowercase
# you can write func name with an underscore by separating two words

# indentation is mainly considered, same indented level considered as code block inside the function


def calculate_area_of_rectangle(width, height):
    return int(width) * int(height)


area1 = calculate_area_of_rectangle(6, 2)
print(area1)

area2 = calculate_area_of_rectangle(4, 6)
print(area2)


def greeting(name, age):
    print("Hi " + name + "!", "You are " + str(age))


greeting("Devi", 54)
greeting("Yash", 24)


def cube(num):
    return int(num) * int(num) * int(num)


cubeOfNumber = cube(3)
print(cubeOfNumber)

# after the return statement function doesn't execute
