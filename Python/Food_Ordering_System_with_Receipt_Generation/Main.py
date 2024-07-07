from fpdf import FPDF
import datetime

Menu = {
    "Burger": 100,
    "Fries": 40,
    "Coke": 30,
    "Sandwich": 80
}
order = {}

def show_menu(menu):
    for key, value in menu.items():
        print(f"{key}: {value}")

def add_to_order(item):
    if item in Menu:
        if item in order:
            order[item] += 1
        else:
            order[item] = 1
    else:
        print("Enter valid item")

def show_order(order):
    if order != {}:
        print("Current Order: ")
        for key, value in order.items():
            print(f"{key}: {value}")
        print("Total: ", order_total(order))
    else:
        pass

def order_total(order):
    total = 0
    for key, val in order.items():
        total += Menu[key] * order[key]
    return total

def generate_pdf(menu, order):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", size=24)
    pdf.cell(200, 10, txt="Fastest Food Order Receipt", ln=True, align='C')

    # Menu
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Menu and Pricing", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    for item, price in menu.items():
        pdf.cell(200, 10, txt=f"{item}: {price}", ln=True, align='L')
    
    pdf.cell(200, 10, txt="", ln=True)  # Empty line

    # Order
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Order Details", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    for item, quantity in order.items():
        pdf.cell(200, 10, txt=f"{item}: {quantity}", ln=True, align='L')
    
    # Total
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=f"Total: {order_total(order)}", ln=True, align='L')
    
    # Save PDF
    pdf.output(f"order_receipt{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf")
    print("PDF generated successfully!")

def main():
    userinput = ""
    print("Welcome to Fastest foods! What would you like to have?")
    show_menu(Menu)
    
    while userinput.lower() != "done":
        userinput = input("What would you like to have? (Type 'done' when finished): ").title()
        if userinput.lower() != "done":
            add_to_order(userinput)
            show_order(order)
    
    print(f"Thank you for your order! Your total is {order_total(order)}")
    generate_pdf(Menu, order)
if __name__ =="__main__":
    main()
