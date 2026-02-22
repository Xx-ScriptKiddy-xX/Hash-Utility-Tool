import hashlib
import os
from tkinter import filedialog, Tk
import sys

# -------------------------------------------------------------
# File Hash Utility
# Allows users to calculate and compare cryptographic hashes
# using common algorithms such as SHA256, MD5, and SHA1.
#
# Features:
# - File selection via GUI dialog
# - Drag-and-drop support
# - Hash calculation and comparison
# - Robust error handling
# -------------------------------------------------------------


def calculate_hash(file_path, algorithm):
    """
    Calculates the cryptographic hash of a file using
    the specified algorithm.

    Reads the file in chunks to prevent high memory usage.
    """

    try:
        # Attempt to create a hash object using the selected algorithm
        # (Example: sha256, md5, sha1)
        hash_func = hashlib.new(algorithm)

    except ValueError:
        # Triggered if the algorithm name is invalid
        os.system('cls')
        print(f"Invalid hash algorithm: {algorithm}")
        return None

    try:
        # Open the file in binary mode for hashing
        with open(file_path, "rb") as file:

            # Read file in 8KB chunks to avoid loading large files into memory
            while chunk := file.read(8192):
                hash_func.update(chunk)

        # Return the final hexadecimal hash value
        return hash_func.hexdigest()

    except FileNotFoundError:
        # If the file does not exist
        os.system('cls')
        print("File not found.")
        return None

    except PermissionError:
        # If the file is locked or access is denied
        os.system('cls')
        print("Permission denied while reading the file.")
        return None

    except Exception as e:
        # Catch any other unexpected file-related errors
        os.system('cls')
        print(f"Error reading file: {e}")
        return None


def select_file_dialog():
    """
    Opens a file selection dialog using Tkinter
    and returns the selected file path.
    """

    try:
        # Create a hidden Tkinter window
        root = Tk()
        root.withdraw()

        # Open file dialog
        file_path = filedialog.askopenfilename()

        # Destroy Tkinter instance to free resources
        root.destroy()

        return file_path

    except Exception as e:
        # Catch GUI-related errors
        os.system('cls')
        print(f"File dialog error: {e}")
        return None


def compare_hashes(original_hash, algorithm):
    """
    Prompts the user to select a file and compares
    its hash against a known hash value.
    """

    try:
        # Open file selection dialog
        file_path = select_file_dialog()

        if not file_path:
            os.system('cls')
            print("No file selected.")
            return

        # Calculate hash of selected file
        selected_hash = calculate_hash(file_path, algorithm)

        os.system('cls')

        # Compare results if hashing succeeded
        if selected_hash:

            if selected_hash == original_hash:
                print(f"Hashes match!\nHash: {original_hash}")

            else:
                print(f"Hashes do not match.\nOriginal: {original_hash}\nSelected: {selected_hash}")

    except Exception as e:
        # Catch unexpected comparison errors
        os.system('cls')
        print(f"Comparison error: {e}")


def find_hash(algorithm):
    """
    Prompts the user to select a file and displays
    its calculated hash value.
    """

    try:
        # Open file dialog
        file_path = select_file_dialog()

        if not file_path:
            os.system('cls')
            print("No file selected.")
            return

        # Generate hash
        selected_hash = calculate_hash(file_path, algorithm)

        os.system('cls')

        # Display hash if successful
        if selected_hash:
            print(f"The hash of the selected file using '{algorithm}' is:\n{selected_hash}")

    except Exception as e:
        # Catch unexpected calculation errors
        os.system('cls')
        print(f"Hash calculation error: {e}")


def main():
    """
    Main program loop.
    Handles drag-and-drop input and user menu navigation.
    """

    try:
        file_path = None

        # Check for drag-and-drop file from command line
        if len(sys.argv) > 1:

            file_path = sys.argv[1]

            # Validate file path
            if not os.path.isfile(file_path):

                os.system('cls')
                print(f"Invalid file path: {file_path}")
                file_path = None

            else:
                os.system('cls')
                print(f"Drag-and-drop file detected: {file_path}")

        # Main application loop
        while True:

            print("\nFile Hash Utility Menu:")
            print("M - Compare a file's hash to a known hash")
            print("C - Calculate a file's hash")
            print("Q - Quit")

            user_input = input("Your choice: ").strip().lower()

            os.system('cls')

            if user_input == 'm':

                # Compare mode
                original_hash = input("Enter the original hash: ").strip()
                algorithm = input("Enter the hash algorithm (e.g., sha256, md5, sha1): ").strip()

                compare_hashes(original_hash, algorithm)

            elif user_input == 'c':

                # Calculation mode
                algorithm = input("Enter the hash algorithm (e.g., sha256, md5, sha1): ").strip()

                find_hash(algorithm)

            elif user_input == 'q':

                # Exit program
                print("Exiting program.")
                break

            else:
                print("Invalid option. Please try again.")

    except KeyboardInterrupt:
        # Handle Ctrl+C cleanly
        os.system('cls')
        print("\nProgram interrupted by user.")

    except Exception as e:
        # Catch any fatal runtime errors
        os.system('cls')
        print(f"Fatal error: {e}")


# -------------------------------------------------------------
# Program Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":

    try:
        # Clear terminal on startup
        os.system('cls' if os.name == 'nt' else 'clear')

        # Launch main application
        main()

    except Exception as e:
        # Catch startup errors
        print(f"Startup error: {e}")
        sys.exit(1)