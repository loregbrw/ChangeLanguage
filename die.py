values = [0, 0, 0, 0, 0, 0]

for i in range(20):
    num = int(input("Write the number rolled on the die (from 1 to 6): "))
    values[num - 1] += 1;

for i in range(1, 7):
    print(f"The number {i} came up {values[i - 1]} times on the die.")