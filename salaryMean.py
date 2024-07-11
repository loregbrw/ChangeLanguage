total = 0

for i in range(5):
    salary = float(input(f"{i + 1}. Whats your salary? "))
    total += salary

mean = total / 5

print(f"Salaries total is: {total:.2f}")
print(f"Salaries mean is: {mean:.2f}")