enrollment = input("Whats your enrollment? ")

grade1 = float(input("Write your first grade? "))
grade2 = float(input("Write your second grade? "))
grade3 = float(input("Write your third grade? "))

mean = (grade1 + grade2 + grade3) / 3

print(f"Mean: {mean:.2f}")

concept = ""
status = ""

if mean >= 9:
    concept = "A"
    status = "APPROVED"
elif mean >= 7.5:
    concept = "B"
    status = "APPROVED"
elif mean >= 6:
    concept = "C"
    status = "APPROVED"
elif mean >= 4:
    concept = "D"
    status = "FAILED"
else:
    concept = "E"
    status = "DUMB"


print(f"Concept: {concept}, {status}")