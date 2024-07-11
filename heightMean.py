minHeight = 0; maxHeight = 0
womenHeight =[0, 0]; allHeight = [0, 0]

for i in range(10):
    gender = int(input("What's your gender? 1 for male and 2 for female: "))
    height = float(input("What's yout height?: "))

    if (height < minHeight or minHeight == 0):
        minHeight = height

    if (height > maxHeight):
        maxHeight = height

    if (gender == 2):
        womenHeight[0] += height
        womenHeight[1] +=1

    allHeight[0] += height
    allHeight[1] += 1

womenMean = womenHeight[0] / womenHeight[1]
avgMean = allHeight[0] / allHeight[1]

print(f"The min height is {minHeight}")
print(f"The max height is {maxHeight}")
print(f"The women height mean is {womenMean}")
print(f"The total height mean is {avgMean}")