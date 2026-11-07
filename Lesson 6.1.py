answer = "yes"

while answer == "yes":
    number = int(input("Enter a number: "))

    multiplier = 1

    while multiplier <= 10:
        print(number, "x", multiplier, "=", number * multiplier)
        multiplier += 1

    answer = input("Do you want to continue? (yes/no): ")

print("Program finished!")