def shopping_cart(**products):
    for item, price in products.items():
        print(item, f"₹{price}")
    print("Total:", f"₹{sum(products.values())}")

shopping_cart(apple=15, orange=12, mango=10)
