def main():
    while True:
        logo_print()
        packaging_name = input("Enter the packaging name: ")
        type_of_coffee_beans = input("Enter the type of coffee beans: ")
        weight_of_coffee_beans = float(input("Enter the weight (in grams): "))  # Convert to float
        price_of_coffee_beans = float(input("Enter the coffee beans price per gram ($): "))  # Convert to float
        packaging_tone = input("Enter the packaging tone: ")
        price_of_packaging_tone = float(input("Enter the packaging price ($): "))  # Convert to float
        selling_price = float(input("Enter the selling price ($): "))  # Convert to float
        confirmation = input("Confirm? (Y): ")

        if confirmation == 'Y':
            output(packaging_name, type_of_coffee_beans, weight_of_coffee_beans, price_of_coffee_beans, packaging_tone, price_of_packaging_tone, selling_price)
            input()
            infinity_void(25)

        else:
            infinity_void(25)
            continue

def output(packaging_name, type_of_coffee_beans, weight_of_coffee_beans, price_of_coffee_beans, packaging_tone, price_of_packaging_tone, selling_price):
    infinity_void(5)
    print("--- Coffee Packaging Details --- \n")
    print("Packaging Name: " + packaging_name)
    print("Packaging Tone: " + packaging_tone)
    print("Packaging Price: $" + str(price_of_packaging_tone))
    print("Packaging Selling Price: $" + str(selling_price) + "\n")
    print(f"{type_of_coffee_beans} | {weight_of_coffee_beans}g | ${price_of_coffee_beans}/g \n")

    # Calculate profit/loss
    profit_loss_value = selling_price - ((weight_of_coffee_beans * price_of_coffee_beans) + price_of_packaging_tone)
    print("Profit/Loss Value: $" + str(profit_loss_value))

    # Calculate profit/loss percentage
    profit_loss_percentage = (profit_loss_value / selling_price) * 100
    print("Profit/Loss Percentage: " + str(profit_loss_percentage) + "%")


def logo_print():
    print("""
         ___  ___
        |   \/   |
        |  \  /  | ___
        |  |\/|  |/   '
        |  |  |  |
        |__|  |__|\__
    """)

def infinity_void(x):
    for i in range(x):
        print("")


if __name__ == "__main__":
    main()
