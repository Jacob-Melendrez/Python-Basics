price = input("How much for the truck? (Need exact decimal value.)")
price = float(price)

if price < 10000:
    print("I'll take it.")
else:
    print("Too expensive.")