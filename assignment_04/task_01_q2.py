import os #importing os
file_name = "sample.txt" #make a variable storing file name

if os.path.exists(file_name): # checking if file existing or not
    os.remove(file_name) # if file exist then os will delete the file
else:
    print(f"Error: The file {file_name} dosen not exist") #if file not exists

# >> OUTPUT >>
# Error: The file sample.txt dosen not exist