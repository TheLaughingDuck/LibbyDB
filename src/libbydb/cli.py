'''
This is the script that the user should first of all interact with.

It can also open the GUI with a simple command.
'''

import sys
from libbydb.utils.CRUD import CREATE
from libbydb.gui import App

def main():
    print("\nWelcome to the LibbyDB Command Line Interface (CLI)!")    
    HELP()

    while True:
        try:
            user_input = input(">").strip()
            if not user_input:
                # No non-whitespace input
                continue
            
            if user_input.upper() == "GUI":
                app = App()
                app.mainloop()

                print("Exiting the GUI, returning to the CLI")
                continue

            if user_input.upper() == "EXIT":
                print("Exiting the LibbyDB CLI")
                break
            
            if user_input.upper() == "HELP":
                HELP()
                continue

            # Evaluate possible PUT or GET requests

            command_parts = [i.lower() for i in user_input.split()]
            command = command_parts[0].upper()

            if command == "PUT" and len(command_parts) > 1:
                if command_parts[1] not in ["users", "loans", "employees", "media", "authors"]:
                    print("Unknown table")
                    continue
                print("The PUT functionality is not fully implemented yet, unfortunately.")
                continue

                #PUT(table=command_parts[1], variables=[], values=[])

        except KeyboardInterrupt:
            print("\nCLI Interrupted. Exiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

def HELP():
    '''
    Print a list of the available commands.
    '''
    print("\nThe available functionality are:")
    print("* Type 'GUI' to launch the Graphical User Interface.")
    print("* Type 'EXIT' to quit.")
    print("* Type 'PUT' to start formatting a PUT request to the database")
    print("* Type 'GET' to make a request to the database for data")
    print("* Type 'HELP' to see this list.")


if __name__ == "__main__":
    main()
