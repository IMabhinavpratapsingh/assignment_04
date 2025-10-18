data = str(input("enter text to write to the file: "))
with open("output.txt" , "wt") as file:
    content = file.write(data + '\n')
    print(f" Data has been successfully saved to 'output.txt'\n.")

add_data = str(input("enter additional data to append: "))
with open("output.txt" , "at") as file:
    content2 = file.write(add_data + '\n')
    print(f" Data has been successfully appended. ")

print("\nFinal content of the output is: ")
with open("output.txt" , "rt") as file:
    result = file.read()
    print(result)