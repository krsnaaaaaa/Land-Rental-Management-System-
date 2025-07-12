def display_available_lands(inventory):
    print("Available Lands:")
    for kitta_no, land_data in inventory.items():
        # if status of the land is 'available' then we simply show it to the user that the land is available for rent 
            print(f"  Kitta Number: {kitta_no}, City: {land_data['city']}, Area: {land_data['area']} anna ,   Status:{land_data['status']}")

def load_land_data(filename):
     inventory = {}
     with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            # i am using the dictionary data structure to store the land inventory information
            inventory[data[0]] = {
                'city': data[1],
                'direction': data[2],
                'area': int(data[3]),
                'price': int(data[4]),
                'status': data[5].strip()
            }
        return inventory
