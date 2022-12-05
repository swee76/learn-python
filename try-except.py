# in python also have try except block to handle errors

try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

# In javascript we use try-catch block to handle exceptions
# try{
#
# }catch (Exception e){
#  console.log(e)
# }
