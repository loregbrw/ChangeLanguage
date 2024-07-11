nums = []

for i in range(10):
    num = int(input(f"Write the {i + 1}º value: "))
    nums.append(num)

search = int(input("Write a number to look for: "))

found = 0

for i in nums:
    if i == search:
        found += 1

print(f"The number was found {found} times")
