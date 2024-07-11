WOMEN_VALUES = [62.1, 44.7]
MEN_VALUES = [72.7, 58]

def idealWeight(sex, height):
    value = []

    if sex == "M":
        value = MEN_VALUES
    elif sex == "F":
        value = WOMEN_VALUES

    return (value[0] * height) - value[1]


sex = input("Enter your gender (M for male and F for female): ")
height = float(input("Enter you height: "))

print(f"Your ideal weight is: {(idealWeight(sex, height)):.2f}")
