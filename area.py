def calcArea(width, length):
    return width * length;

width = float(input("Write the width: "))
length = float(input("write the length: "))

print(f"The area of the property with a width: {width}, and a length: {length} is: {calcArea(width, length)}")