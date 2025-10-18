import os
file_name = "sample.txt"

if os.path.exists(file_name):
    os.remove(file_name)
else:
    print(f"Error: The file {file_name} dosen not exist")