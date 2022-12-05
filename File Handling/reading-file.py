# reading a file

# r - read (only read)
# w- write (write, change)
# a - append (cannot change anything, just append to the end of the file)
# r+ - read and write (both)

employee_file = open("employees.txt", "r")

# This is the way how to check the is file readable
print(employee_file.readable())

# This read file line by line
print(employee_file.readline())
print(employee_file.readline())

# This take the whole lines of file and put them into an array
for employee in employee_file.readlines():
    print(employee)

# This reads whole file
print(employee_file.read())

# Generally if you opened a file you have to close that file

employee_file.close()
