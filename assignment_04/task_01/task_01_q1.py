with open("sample.txt" , "wt") as file:
    file.write("Reading file content: \n")
    file.write("Line 1: Hi im abhinav. \n")
    file.write("Line 2: and this is a second line. \n")
    file.write("Line 3: and herer the another 3rd line. \n")


with open("sample.txt" , "rt") as file:
    content = file.read()
    print(content)


# # >> output >> :
# # Reading file content: 
# # Line 1: Hi im abhinav.
# # Line 2: and this is a second line.
# # Line 3: and herer the another 3rd line.