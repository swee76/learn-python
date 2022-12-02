# if-statements & comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print("Maximum number is " + str(max_num(2, 3, 7)))

# Get values from keyboard and obtain max number
input_value1 = input("Input no 1: ")
input_value2 = input("Input no 1: ")
input_value3 = input("Input no 1: ")

print(max_num(input_value1, input_value2, input_value3))

# <  - less than
# >  - greater than
# ==  -equal to
# <=  - less than or equal to
# >=  - greater than or equal to
# !=  - not equal to


