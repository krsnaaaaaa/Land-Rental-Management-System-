import datetime

customer_transactions = {}

def generate_customer_invoice(customer_name):
    if customer_name in customer_transactions:
        with open(f'{customer_name}_Rent_invoice.txt', 'w') as f:
            f.write("TechnoPropertyNepal\n")
            f.write("---------------------------------------------------\n")
            total_amount = 0
            for transaction in customer_transactions[customer_name]:
                f.write(f'Customer Name: {customer_name}\n')
                f.write(f'Transaction Type: {transaction["transaction_type"]}\n')
                f.write(f'Kitta Number: {transaction["land_info"]["kitta_no"]}\n')
                f.write(f'City/District: {transaction["land_info"]["city"]}\n')
                f.write(f'Direction: {transaction["land_info"]["direction"]}\n')
                f.write(f'Area of Land: {transaction["land_info"]["area"]} anna\n')
                f.write(f'Date and Time: {transaction["rented_date"]}\n')
                f.write(f'Duration of Rent: {transaction["duration"]} months\n')
                total_amount += transaction["duration"] * transaction["land_info"]["price"]
            f.write(f'Total Amount: {total_amount}\n\n')
    else:
        print("No transactions found for this customer.")

def generate_return_invoice(customer_name, kitta_no, land_info, duration, fine):
    now = datetime.datetime.now()
    if customer_name in customer_transactions:
        with open(f'{customer_name}_Return_invoice.txt', 'w') as f:
            f.write("TechnoPropertyNepal\n")
            f.write("---------------------------------------------------\n")
            f.write(f'Customer Name: {customer_name}\n')
            f.write(f'Transaction Type: Return\n')
            f.write(f'Kitta Number: {kitta_no}\n')
            f.write(f'City/District: {land_info["city"]}\n')
            f.write(f'Direction: {land_info["direction"]}\n')
            f.write(f'Area of Land: {land_info["area"]} anna\n')
            f.write(f'Date and Time of Return: {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
            f.write(f'Duration of Rent: {duration} months\n')
            total_amount = duration * land_info['price'] + fine
            f.write(f'Total Amount: {total_amount}\n')
            f.write(f'Fine: {fine}\n\n')
    else:
        print("No transactions found for this customer.")
