import os

folders = input("Enter folder name/s: ").split(",")
print(folders)

for folder in folders:
    try:
        files = os.listdir(folder)
        print(folder)

    except FileNotFoundError:
        print("Please provide a valid directory name")

        continue

    for file in files:
        print(file)