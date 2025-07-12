import read
import operation


# this function loads all the land inventory information store in my file

def save_land_data(filename, inventory):
   with open(filename, 'w') as file:
        for kitta_no, land_data in inventory.items():
            file.write(f"{kitta_no},{land_data['city']},{land_data['direction']},{land_data['area']},{land_data['price']},{land_data['status']}\n")


# this one here we rent our land based on the kita number


def main():
    inventory = read.load_land_data('land.txt')
    print()
    print("\t\t\t\t\t\t\t\t\t\t\t\t TECHNO PROPERTY NEPAL \n\n\t\t\t\t\t\t\t\t\t\t\t\t    KATHMANDU,NEPAL \n\n\t\t\t\t\t\t\t\t\t\t\t\t   PHONE: 041-9876532 \n" )
    print()
    print("---------------------------------------------------------------********************************************************************************---------------------------------------------------------------")
    print()
    print("\t\t\t\t\t\t\t\t\t\t\t  WELCOME TO TECHNO PROPERTY NEPAL !! \n")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print()
    print("Greetings, Sir or Madam We would want to provide our consumers with the opportunity to rent land in various regions of Nepal. Each month, the rental fee would be charged. You can access the service tour below.  \n")
    print("Please choose appropriate option.")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    while True:
        
        print()
        print("1. Display Lands")
        print("2. Rent Land")
        print("3. Return Land")
        print("4. Exit")

        choice = operation.get_integer_input("Enter your choice: ")

        if choice == 1:
            read.display_available_lands(inventory)

        elif choice == 2:
            read.display_available_lands(inventory)
            operation.rent_land(inventory)
            print("Thanks for visting us")
            
        elif choice == 3:
            operation.return_land(inventory)
        elif choice == 4:
            print("Exiting... ")
            print("Thanks for Visting Us")
            return
        else:
            print("Invalid Choice")

    save_land_data('land_inventory.txt', inventory)

if __name__ == '__main__':
    main()
