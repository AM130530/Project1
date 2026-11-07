answer = "yes"

while answer == "yes":
    number = int(input("Enter a number: "))

    multiplier = 1

    while multiplier <= 20:
        print(number, "x", multiplier, "=", number * multiplier)
        multiplier += 1

    answer = input("Do you want to continue with another table? (yes/no): ")

print("Program finished!")