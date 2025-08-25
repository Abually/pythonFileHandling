# Create a program that reads a file and writes a modified version to a new file.

# Read the original file
with open("friends.txt", "r") as fileOne:
    content = fileOne.read()

# Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("friends_modified.txt", "w") as fileTwo:
    fileTwo.write(modified_content)

#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read

filename = input("Enter the filename to read: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: The file '{filename}' cannot be read.")

# End of code

