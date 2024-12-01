# Password Manager Script
# Author: Princedhorn Wongsuphap
# Purpose: To store and retrieve login credentials securely.
# Date Started: 13/10/2023
# Date Ended: 25/10/2023

import os

# Initialize an empty dictionary for credential storage
credentials = {}

# Define the file path for storing credentials
file_path = "credentials.txt"

# Check if the credential file already exists, and if not, create it
if not os.path.exists(file_path):
    with open(file_path, 'w'):
        pass

# Function to add credentials to the dictionary and file


def add_credentials():
    URL_name = input("Enter URL/resource name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if inputs are at least 8 characters
    if len(username) < 8 or len(password) < 8:
        print("Input length for usernames and passwords must be at least 8 characters. Please try again.")
        return

    # Add the credential to the dictionary
    credentials[URL_name] = {
        'username': username, 'password': password}

    # Append the credential to the file
    with open(file_path, 'a') as file:
        file.write(f"URL: {URL_name}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write("\n")  # Add spacing between entries

    print("Credential added successfully!")


# Main menu loop
while True:
    # Display menu options
    print("\nPassword Manager Menu:")
    print("1. Add stored credentials")
    print("2. View stored credentials")
    print("3. Exit")

    # Get user's choice
    choice = input("Enter your choice (1/2/3): ")

    # Handle user's choice
    if choice == "1":
        # Add stored credentials
        add_credentials()

    elif choice == "2":
        # View stored credentials
        if not credentials:
            print("No credentials stored yet.")
        else:
            print("\nStored Credentials:")
            with open(file_path, 'r') as file:
                print(file.read())

    elif choice == "3":
        # Exit the script
        print("Exiting the Password Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
