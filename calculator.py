def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2;

while True:
    op = input("Choose a option:\nSm - sum\nSb - sub\nM - mul\nD - div\n# - leave\n-> ")

    if op == "#":
        break

    num1 = int(input("Write the fist integer number: "))
    num2 = int(input("Write the fist integer number: "))

    match op:
        case "Sm":
            print(f"{num1} + {num2} = {sum(num1, num2)}")
        case "Sb":
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        case "M":
            print(f"{num1} * {num2} = {mul(num1, num2)}")
        case "D":
            print(f"{num1} / {num2} = {div(num1, num2)}")

    print()