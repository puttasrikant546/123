# app.py

menu =  {
    'tatapunch': 613000,
    'hyundaicreta' : 2200000,
    'marutifronx' : 1300000,
    'mahindra thar' : 1700000,
    'Audi' : 4400000,
    'BMW': 7400000,
    'Honda' : 6300000,
    'landrover' : 10000000,
    'Kia' : 1100000,
    'ferrari': 30000000,
    'lamborghini' : 300000000,
}

def welcome_message():
    print("Welcome to Srikant's Super Luxury Car Showroom")
    print("Check the menu of available cars in the showroom:")
    print("Out of menu, no cars are available.")
    print(f"You can take a loan or give money directly. The price will be reduced according to your wish.")
    print("\nAvailable cars:")
    for car, price in menu.items():
        print(f"{car} = {price}")

def order_car():
    order_total = 0
    item_1 = input("Enter the name of the car you want to order: ").lower()
    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your car {item_1} has been added to your order.")
        payment_method = input("Do you want to take a loan or pay directly? (loan/direct): ").lower()
        print(f"Your car warranty is for three years. Any problems? Free service is available.")
    else:
        print(f"Order item {item_1} is not available!")
    
    another_order = input("Do you want to add another car? (yes/no): ").lower()
    if another_order == "yes":
        item_2 = input("Enter the name of the second car you want to order: ").lower()
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your car {item_2} has been added to your order.")
            print(f"Your car warranty is for three years. Any problems? Free service is available.")
        else:
            print(f"Order item {item_2} is not available!")
    else:
        print("No second car added to your order.")
    
    print(f"Total cost of your order: {order_total}")

# Main function to start the process
welcome_message()
order_car()
