def main():
    price = float(input('Items Price($): '))  # Ask user for items price
    discount = float(input('Discount(%): '))  # Ask user for discount if any

    final_price = calculate_discount(price, discount)  # Call the function
    if discount > 20:
        print('Discount has been applied.')
    else:
        print('No Discount applied.')
    print(f'Your Items Price is: {round(final_price, 2)}')


def calculate_discount(price, discount):
    if discount > 20:
        return price - (price * (discount / 100))
    else:
        return price


main()