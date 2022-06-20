#!/usr/bin/env python3
# regexSearch.py opens all .txt files in a directory, searches for any line
# that matches a user-supplied regex. Print the results to the screen.

import os, re, sys
from pathlib import Path

while True:
    # Get search directory from user
    searchDir = input("Please enter the absoloute path to the directory you would like to search. ")
    # Check that path and directory are valid
    if os.path.isabs(searchDir) and os.path.isdir(searchDir):
        # Collect only .txt files
        searchDir = Path(searchDir)
        textFiles = list(searchDir.glob('*.txt'))
    else:
        print("Incorrect path, please run program again")
        sys.exit()

    # Get regex pattern from user
    rPattern = re.compile(input("Please enter your regex search pattern. "))

    # Open files and search 
    for file in textFiles:
        with open(os.path.join(searchDir, file)) as f:
            textfile = f.read()
        matches = re.findall(rPattern, textfile)
        # Print matches
        if not re.search(rPattern, textfile) == None:
            print(f"The following matches were found for file: {file.name}")
            print(f"{', '.join([match for match in matches])}")  
        else:
            print(f"Sorry! No matches for file {file.name}")  
        #matches += f'Match # {matchNum}: ' + str(matches[0:][0:]) + f'from file {file}\n'

        print('Would you like to search another directory? (y/n)')
        answer = input()
        
        if answer.lower() == 'n':
            sys.exit()
        


   



