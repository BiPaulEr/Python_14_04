ages = [22, 25, 19, 34, 23, 18]
index = 0

while index < len(ages) and ages[index] >= 21:
    index += 1

if index < len(ages):
    print(f"Policy violation found at index {index}, age: {ages[index]}")
else:
    print("No policy violations detected.")