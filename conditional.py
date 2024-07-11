name = input("Whats your name? ")
age = input("Whats your age? ")
sex = input("Whats your sex (M-male and F-female)? ")

if sex == "M" and age >= 18 and age <= 65:
    print(f"{name} is between the age of 18 and 65, and is male!")

print(f"{name} is not between the age of 18 and 65, and is female!")
