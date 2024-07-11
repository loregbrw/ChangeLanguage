def calcPrice(price, total):
    return total / price

name = input("Write your name: ")
literprice = float(input("Write the price per gasoline liter :"))
payment = float(input("Write the payment amout: "))

print(f"You're gonna fill {(calcPrice(literprice, payment)):.2f} liter of gasoline")