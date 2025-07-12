import datetime
import write  # Assuming write is a module that handles customer transactions and invoice generation

def generate_invoice_terminal(invoice_type, customer_name, kitta_no, duration=None, fine=None, rental_date=None, return_date=None, price_per_month=None):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    invoice = f"{invoice_type.capitalize()} Invoice\n"
    invoice += "--------------------------------------------------\n"
    
    invoice +="\t\t\t\t\t\t\t\t\t\t\t\t TECHNO PROPERTY NEPAL \n\n\t\t\t\t\t\t\t\t\t\t\t\t    KATHMANDU,NEPAL \n\n\t\t\t\t\t\t\t\t\t\t\t\t   PHONE: 041-9876532 \n"

    invoice += f"Customer Name: {customer_name}\n"
    invoice += f"Kitta Number: {kitta_no}\n"
    invoice += f"Transaction Date: {now}\n"

    if invoice_type == "rent":
        invoice += f"Rental Date: {rental_date}\n"
        invoice += f"Duration: {duration} months\n"
        invoice += f"Price: {duration * price_per_month}\n"
    elif invoice_type == "return":
        invoice += f"Return Date: {return_date}\n"
        invoice += f"Duration: {duration} months\n"
        invoice += f"Fine: {fine}\n"
        invoice += f"Total Price: {duration * price_per_month + fine}\n"

    print(invoice)

def rent_land(inventory):
    now = datetime.datetime.now()
    print("----------------------------------------------------------------------\n")
    kitta_no = input("Enter Kitta Number to rent: ")
    
    if kitta_no in inventory and inventory[kitta_no]['status'] == 'Available':
        customer_name = input("Enter Customer Name: ")
        
        duration = get_integer_input("Enter rental duration (in months): ")
        
        inventory[kitta_no]['status'] = 'Not Available'
       
        if customer_name not in write.customer_transactions:
            write.customer_transactions[customer_name] = []
        
        write.customer_transactions[customer_name].append({
            'transaction_type': 'Rent', 
            'land_info': {'kitta_no': kitta_no, **inventory[kitta_no]}, 
            'duration': duration, 
            'rented_date': now.strftime('%Y-%m-%d %H:%M:%S')
        })
        
        write.generate_customer_invoice(customer_name)
        generate_invoice_terminal("rent", customer_name, kitta_no, duration=duration, rental_date=now.strftime('%Y-%m-%d %H:%M:%S'), price_per_month=inventory[kitta_no]['price'])
        print("-----------------------------------------------------------------------\n")
        print("Land rented successfully!")
    else:
        print("Land Unavailable or Please enter the correct Kitta No.")      
    
    return inventory

def return_land(inventory):
    print("-----------------------------------------------------------------------------\n")
    kitta_no = input("Enter Kitta Number to return: ")
    
    if kitta_no in inventory and inventory[kitta_no]['status'] == 'Not Available':
        customer_name = input("Enter Customer Name: ")
        
        return_rented_duration = get_integer_input("Enter original rental duration (in months): ")
        
        now = datetime.datetime.now()
        return_date = now.strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            actual_rented_duration = write.customer_transactions[customer_name][0]['duration']
        except (KeyError, IndexError):
            print("This customer hasn't done any transactions before.")
            return return_land(inventory)
        
        
        # Calculate total rented months

        '''
        this here is hard coded
        '''
        # Adding 1 to include the current month
        
        # Calculate months late
        months_late = max(0, return_rented_duration - actual_rented_duration)
        price_per_month = inventory[kitta_no]['price']
        
        # Calculate the fine
        fine = round(0.1 * months_late * price_per_month)
        
        # Generate and display invoice
        write.generate_return_invoice(customer_name, kitta_no, inventory[kitta_no], return_rented_duration, fine)
        generate_invoice_terminal("return", customer_name, kitta_no, duration=return_rented_duration, fine=fine, return_date=return_date, price_per_month=price_per_month)
        
        # Update inventory status
        inventory[kitta_no]['status'] = 'Available'
        print("-----------------------------------------------------------\n")
        print("Land returned successfully!")
    else:
        print("Land not currently rented or invalid Kitta Number.")

def get_integer_input(prompt, error_message="Invalid input. Please enter a number."):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)
