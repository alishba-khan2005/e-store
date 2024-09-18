
def ecommerce_store():
    print("welcome to our store!")
    print("\nCategories:")
    print("1. Electronics")
    print("2. Clothes")
    print("3. Books")

while True:
    try:
        category_choice = int(input("choose a category (1-3):"))
        if 1 <= category_choice <= 3:
            break
        else:
            print("Invalid category choice. Please enter a number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if category_choice == 1:
    print("\nElectronic")
    print("1. Smartphones - $500")
    print("2. Laptop - $1000")
    print("3. Headphones - $150")
    print("4. Smartwatch - $250")
    print("5. Camera - $700")
    prices = [500, 1000, 150, 250, 700]

elif category_choice==2:
      print("\nClothing")
      print("1.tshirt")
      print("2.jeans")
      print("3.shoes")
      print("4.dress")
      print("5.jacket")
elif category_choice==3:

      print("\nBooks")
      print("1. Novel")
      print("2. Textbook")
      print("3. Comic book")
      print("4. Biography")
      print("5. Cookbook")
while True:
        try:
            item_choice = int(input("choose an item (1-5): "))
            if 1 <= item_choice <= 5:
                break
            else:
                print("Invalid item choice. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
item_price = prices[item_choice - 1]
print(f"\nItem price: ${item_price}")

checkout_choice = input("\nCheckout? (yes/no): ").lower()
if checkout_choice == "no":
        print(f"\nThank you for your purchase! Your total is ${item_price}.")
else:
        print("\nYour item has been removed from the cart.")
        ecommerce_store()