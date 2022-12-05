# writing a file

employee_file = open("employees.txt", "a")

employee_file.write("\nToby - Human Resources")

employee_file.write("\nKelly - Customer Service")

employee_file.close()

# write, overwrite the file - if there is no such file, it creates the file and write the content
employee_file = open("employees1.txt", "w")
employee_file.write("\nJonas - Security Officer")
employee_file.close()

data_file = open("index.html", "w")
data_file.write("<p>This is HTML</p>")
data_file.close()
