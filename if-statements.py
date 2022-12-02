# if-statements

is_male = True
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are a neither male nor tall")

# or operator denote by using or in lowercase

if is_male and is_tall:
    print("You are not a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but tall")
else:
    print("You either male or tall or both")

# and operator denote by using and in lowercase
