from fpdf import FPDF  # Import FPDF library to generate PDFs
import datetime  # Import datetime library to handle date and time

# Define the menu with items and their prices
Menu = {
    'Burger': 100,
    'Fries': 40,
    'Coke': 30,
    'Sandwich': 80
}
order = {}  # Initialize an empty order dictionary

# Function to display the menu
def show_menu(menu):
    for key, value in menu.items():
        print(f'{key}: {value}')  # Print each item and its price

# Function to add an item to the order
def add_to_order(item):
    if item in Menu:  # Check if the item is in the menu
        if item in order:
            order[item] += 1  # Increment the quantity if the item is already in the order
        else:
            order[item] = 1  # Add the item to the order with quantity 1
    else:
        print('Enter valid item')  # Print error message if the item is not in the menu

# Function to display the current order and total cost
def show_order(order):
    if order != {}:  # Check if the order is not empty
        print('Current Order: ')
        for key, value in order.items():
            print(f'{key}: {value}')  # Print each item and its quantity
        print('Total: ', order_total(order))  # Print the total cost
    else:
        pass

# Function to calculate the total cost of the order
def order_total(order):
    total = 0
    for key, val in order.items():
        total += Menu[key] * order[key]  # Calculate total cost by summing up the cost of each item
    return total

# Function to generate a PDF receipt for the order
def generate_pdf(menu, order):
    pdf = FPDF()  # Create a new PDF object
    pdf.add_page()  # Add a new page to the PDF
    
    # Add title to the PDF
    pdf.set_font('Arial', size=24)
    pdf.cell(200, 10, txt='Fastest Food Order Receipt', ln=True, align='C')

    # Add menu to the PDF
    pdf.set_font('Arial', size=16)
    pdf.cell(200, 10, txt='Menu and Pricing', ln=True, align='L')
    pdf.set_font('Arial', size=12)
    for item, price in menu.items():
        pdf.cell(200, 10, txt=f'{item}: {price}', ln=True, align='L')
    
    pdf.cell(200, 10, txt='', ln=True)  # Add an empty line

    # Add order details to the PDF
    pdf.set_font('Arial', size=16)
    pdf.cell(200, 10, txt='Order Details', ln=True, align='L')
    pdf.set_font('Arial', size=12)
    for item, quantity in order.items():
        pdf.cell(200, 10, txt=f'{item}: {quantity}', ln=True, align='L')
    
    # Add total cost to the PDF
    pdf.set_font('Arial', size=14)
    pdf.cell(200, 10, txt=f'Total: {order_total(order)}', ln=True, align='L')
    
    # Save the PDF with a filename that includes the current date and time
    pdf.output(f'order_receipt{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.pdf')
    print('PDF generated successfully!')  # Print confirmation message

# Main function to handle user interaction and order process
def main():
    print('Welcome to Fastest Foods! What would you like to have?')
    show_menu(Menu)
    
    while True:
        user_input = input('What would you like to have? (Type "done" when finished): ').title()
        if user_input.lower() == 'done':
            break
        add_to_order(user_input)
        show_order(order)
    
    print(f'Thank you for your order! Your total is {order_total(order)}')
    generate_pdf(Menu, order)

# Run the main function if this script is executed
if __name__ == '__main__':
    main()
