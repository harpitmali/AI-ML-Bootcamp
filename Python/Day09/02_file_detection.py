import os

file_path  = "/Users/harpitmali/AI-ML-Bootcamp/test3.txt"

if os.path.exists(file_path):
    print(f"The file path '{file_path}' exists.")
else:
    print("That file path doesn't exists.")