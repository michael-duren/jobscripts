#!/usr/bin/env python3
# Delete unwanted large files larger then 100MB
# Get folder name from user

import os, shutil

# TODO: Get directory name to search
sdir = input("What directory would you like to search? ")

# TODO: Get a list of large files in directory
largeFiles = []
for file in os.listdir(sdir):
    f_size = os.path.getsize(file)
    if f_size >= 5**8:
        largeFiles.append(file)
    
    
# TODO: Ask user if they want to delete files, delete files
deletedFiles = []
for file in largeFiles:
    print(f"The file {file} is larger than 500 MB. Would you like to delete? (yes/no) "
          "WARNING FILE {file} WILL BE PERMANETLY DELETED!")
    answer = input()
    if answer.lower() == 'yes':
        deletedFiles.append(file)
        shutil.rmtree(file)
    else:
        print(f"File {file} not deleted.")
        
print(f"The following files were deleted: {deletedFiles[:]} ")
    

