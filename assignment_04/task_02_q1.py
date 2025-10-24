# data = str(input("enter text to write to the file: "))
# with open("output.txt" , "wt") as file:
#     content = file.write(data + '\n')
#     print(f" Data has been successfully saved to 'output.txt'\n.")

# add_data = str(input("enter additional data to append: "))
# with open("output.txt" , "at") as file:
#     content2 = file.write(add_data + '\n')
#     print(f" Data has been successfully appended. ")

# print("\nFinal content of the output is: ")
# with open("output.txt" , "rt") as file:
#     result = file.read()
#     print(result)


message = str(input("enter your message: ")) # taking input
with open("output.txt" , "wt") as file: #opening the file 
    data = file.write(message + "\n") #now writing the input in the file
    print(f"Your message has been succcessfully saved to file: \n")

add_message = str(input("enter additional data to append: "))
with open("output.txt" , "at") as file:
    data2 = file.write(add_message + '\n')
    print(f"Data has been successfully added to message. \n")

print("Final content of the output is: ")
with open("output.txt","rt") as file:
    result = file.read()
    print(result)


# >> OUTPUT >>
# enter your message: Abhinav
# Your message has been succcessfully saved to file: 

# enter additional data to append: Pratap SIngh
# Data has been successfully added to message. 

# Final content of the output is:
# Abhinav
# Pratap SIngh