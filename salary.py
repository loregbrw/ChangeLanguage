DAYS = 22

hours = int(input("Write the number of hours worked in per day: "))
value = float(input("Write the value of the hour worked on the day: "))

salary = hours * value * DAYS

print(f"Your monthly salary is: {salary:.2f}")