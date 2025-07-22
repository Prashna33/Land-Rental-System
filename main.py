# Importing necessary modules
import read as reader
import operations as option
import write as updater
def main():
    try:
        # Reading land rental data
        rentalData = reader.readLand("lands.txt")

        while True:
            # Displaying menu options
            print('''
            ╔═════════════════════════════════════════════════════════════╗
            ║                        Welcome!!!                           ║
            ║              Choose any of the option below                 ║
            ║                                                             ║
            ║-------------------------------------------------------------║
            ║ Please choose an option (w , x, y, z) from the menu below:  ║
            ║                                                             ║
            ║           w = Display Land                                  ║
            ║           x = Rent Land                                     ║
            ║           y = Return Land                                   ║
            ║           z = Quit                                          ║
            ╚═════════════════════════════════════════════════════════════╝
            ''')
            userResponse = input("Enter your option: ").lower()  

            if userResponse == 'w':
                option.properties(rentalData) 
                
            elif userResponse == 'x':
                try:
                    name = input("Enter your full name: ")
                    if name == "":
                        print("Name cannot be empty!")
                        continue
                    if any(char.isdigit() for char in name):
                        raise ValueError
                except ValueError:
                    print("Name cannot contain numbers!")
                    continue
                option.rentedLand(rentalData, name) 
                updater.updateLand_info("lands.txt", rentalData) 
                
            elif userResponse == 'y':
                try:
                    name = input("Enter your full name: ")
                    if name == "":
                        print("Name should not be empty!")
                        continue
                    if any(char.isdigit() for char in name):
                        raise ValueError
                except ValueError:
                    print("Name should not contain numbers!")
                    continue
                option.returnedLand(rentalData, name)
                updater.updateLand_info("lands.txt", rentalData)

            elif userResponse == 'z':
                print("Thank You For Visiting Properties Nepal, Do Visit Again.")
                break
            else:
                print("Invalid option! Please select a letter between 'w' and 'z'!!!")
                continue

    except ValueError:
        print("Invalid option! Please select a letter between 'w' and 'z'!!!")
main()
