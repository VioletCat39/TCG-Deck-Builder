""" Bakugan Search by VioletCat39 """
from bakuganmaker import *

# Variables for terminal system
BEGINNING_SCREEN = """
                    ......$$$$$$..$$.......$$..$$$$$$$$$$..$$$$$$$$$$....$$$$$$$...$$$$$$$$$$..
                    ....$$........$$.......$$..$$..........$$..........$$..........$$..........
                    ..$$..........$$.......$$..$$..........$$..........$$..........$$..........
                    .$$...........$$.......$$..$$..........$$..........$$..........$$..........
                    .$$...........$$$$$$$$$$$..$$$$$$$$$$..$$$$$$$$$$....$$$$$$....$$$$$$$$$$..
                    ..$$..........$$.......$$..$$..........$$..................$$..$$..........
                    ....$$........$$.......$$..$$..........$$..................$$..$$..........
                    ......$$$$$$..$$.......$$..$$$$$$$$$$..$$$$$$$$$$..$$$$$$$$....$$$$$$$$$$..
                    """
OTHER_SCREEN =      """
                    .
                    .
                    .
                    .
                    .
                    .
                    .
                    .
                    """

# Note: The sample is included in this database creator
# Will modify later to take user-input csv
BAKUGAN_DATABASE = create_bakugan_database("CardIdentifier/Bakugan/text/bakugan_sample.csv")


TITLE_SCREEN = "\nHello, and welcome to the Bakugan Terminal System!\n\nThis System is designed to help you search for Bakugan quickly and simply based on a couple of simple inputs.\nTo get started, input 'y'. You can exit this program at any time by inputing 'q' or 'exit'."
ATTRIBUTE_SEARCH_SCREEN = "\n\n\nPlease input a number for the attribute of the Bakugan you are searching for:\n\n1. Pyrus\n2. Aquos\n3. Subterra\n4. Haos\n5. Darkus\n6. Ventus\n7. Other"
NAME_SELECT_SCREEN = "\n\n\nPlease input the number of one of the following Bakugan to get a full description:\n"
# A terminal function with the proper display output for the Bakugan searching for
def bakugan_terminal_system():
    """
    The function for the terminal display system.
    """
    quit_terminal = False
    print(TITLE_SCREEN)
    while quit_terminal == False:
        continue_prompt = input("Input y to get started, or q to quit: ")
        if continue_prompt == "q" or continue_prompt == "exit":
            print("Goodbye!")
            quit_terminal = True
            break
        elif continue_prompt.lower() == "y":
            # Do stuff
            print(ATTRIBUTE_SEARCH_SCREEN)
            attribute_prompt = input("Please input a number from 1 to 7: ")
            if attribute_prompt == "q" or attribute_prompt == "exit":
                print("Goodbye!")
                quit_terminal = True
                break
            name_selector_string = ""
            if attribute_prompt == "1":
                target_attribute1 = "pyrus"
                target_attribute2 = "pyrus2"
                target_attribute3 = "pyrus3"
                for key in BAKUGAN_DATABASE:
                    if BAKUGAN_DATABASE[key].get_attribute() == target_attribute1 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute2 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute3:
                        name_selector_string += "\n" + str(key) + " "+ BAKUGAN_DATABASE[key].display_basic()
            elif attribute_prompt == "2":
                target_attribute1 = "aquos"
                target_attribute2 = "aquos2"
                target_attribute3 = "aquos3"
                for key in BAKUGAN_DATABASE:
                    if BAKUGAN_DATABASE[key].get_attribute() == target_attribute1 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute2 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute3:
                        name_selector_string +=  "\n" + str(key) + " "+ BAKUGAN_DATABASE[key].display_basic()
            elif attribute_prompt == "3":
                target_attribute1 = "subterra"
                target_attribute2 = "subterra2"
                target_attribute3 = "aurelus"
                for key in BAKUGAN_DATABASE:
                    if BAKUGAN_DATABASE[key].get_attribute() == target_attribute1 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute2 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute3:
                        name_selector_string += "\n" + str(key) + " "+ BAKUGAN_DATABASE[key].display_basic()
            elif attribute_prompt == "4":
                target_attribute1 = "haos"
                target_attribute2 = "haos2"
                target_attribute3 = "haos3"
                for key in BAKUGAN_DATABASE:
                    if BAKUGAN_DATABASE[key].get_attribute() == target_attribute1 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute2 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute3:
                        name_selector_string += "\n" + str(key) + " "+ BAKUGAN_DATABASE[key].display_basic()
            elif attribute_prompt == "5":
                target_attribute1 = "darkus"
                target_attribute2 = "darkus2"
                target_attribute3 = "darkus3"
                for key in BAKUGAN_DATABASE:
                    if BAKUGAN_DATABASE[key].get_attribute() == target_attribute1 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute2 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute3:
                        name_selector_string += "\n" + str(key) + " "+ BAKUGAN_DATABASE[key].display_basic()
            elif attribute_prompt == "6":
                target_attribute1 = "ventus"
                target_attribute2 = "ventus2"
                target_attribute3 = "ventus3"
                for key in BAKUGAN_DATABASE:
                    if BAKUGAN_DATABASE[key].get_attribute() == target_attribute1 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute2 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute3:
                        name_selector_string += "\n" + str(key) + " "+ BAKUGAN_DATABASE[key].display_basic()
            elif attribute_prompt == "7":
                target_attribute1 = "genesis"
                target_attribute2 = "clear"
                target_attribute3 = "diamond"
                target_attribute4 = "diamond2"
                target_attribute5 = "nulltype"
                target_attribute6 = "galaxy"
                for key in BAKUGAN_DATABASE:
                    if BAKUGAN_DATABASE[key].get_attribute() == target_attribute1 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute2 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute3 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute4 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute5 or BAKUGAN_DATABASE[key].get_attribute() == target_attribute6:
                        name_selector_string += "\n" + str(key) + " " + BAKUGAN_DATABASE[key].display_basic()
            else:
                print("Invalid Input, please try again.")
                continue
            print(NAME_SELECT_SCREEN)
            print(name_selector_string)
            # temporary
            print("Please input the identification number of the Bakugan you wish to search up.")
            bakugan_id = input("Bakugan number: ")
            print(BAKUGAN_DATABASE[str(bakugan_id)])
            print()
            print("Do you wish to continue?")
            continue_terminal_prompt = input("Y or N: ")
            if continue_terminal_prompt.lower() == "y":
                continue
            else:
                break
        else:
            print("Invalid Input, please try again.")
            continue
# Main function to run the terminal system 
def main():
    """
    Main Function
    """
    print(BEGINNING_SCREEN)
    bakugan_terminal_system()
# Runguard
if __name__ == "__main__":
    main()