
import os
import shutil 

# Create file
def create_file():
    filename = input("Enter file name: ")
    content = input("Enter content: ")

    with open(filename, "w") as file:
        file.write(content)

    print("File created successfully")


# Read file
def read_file():
    
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            print("\nFile Content:")
            print(file.read())

    except FileNotFoundError:
        print("File not found")


# Append file
def append_file():
    filename = input("Enter file name: ")
    content = input("Enter text to add: ")

    try:
        with open(filename, "a") as file:
            file.write("\n" + content)

        print("Content added successfully")
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print("Error:", e)


# Delete file
def delete_file():
    filename = input("Enter file name: ")

    try:
        os.remove(filename)
        print("File deleted successfully")

    except FileNotFoundError:
        print("File not found")


# List files
def list_files():
    files = os.listdir()

    print("\nFiles in current directory:")
    for file in files:
        print(file)

# Rename File
def rename_file():
    old_name = input("Enter old file name: ")
    new_name = input("Enter new file name: ")

    try:
        os.rename(old_name, new_name)
        print("File renamed successfully")

    except FileNotFoundError:
        print("File not found")
    except Exception  as e:
        print('Error:', e)

# Copy file
def copy_file():
    source = input("Enter source file name:" )
    destination = input("Enter destination file name: ")
    try:
        shutil.copy(source, destination)
        print('File copied successfully')
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print('Error:', e)

# Main menu
def menu():
    while True:
        print("\n========= FILE MANAGER ==========")
        print("1. Create File")
        print("2. Read File")
        print("3. Append File")
        print("4. Delete File")
        print("5. List Files")
        print("6. Rename File")
        print("7. Copy_file")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            read_file()

        elif choice == "3":
            append_file()

        elif choice == "4":
            delete_file()

        elif choice == "5":
            list_files()
        
        elif choice == "6":
            rename_file()

        elif choice == "7":
            copy_file()

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# Run program
menu()