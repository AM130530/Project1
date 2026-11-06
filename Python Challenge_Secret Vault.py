from random import randint

print("===== SECRET VAULT =====")

secret_pin = str(randint(0000, 9999))

attempts = 0

while attempts < 5:

    pin = input("Enter the secret PIN: ")

    if pin == secret_pin:
        print("Correct PIN!")
        print("ACCESS GRANTED!")
        break

    else:
        print("Wrong PIN!")
        attempts = attempts + 1

        for digit in pin:

            if digit in secret_pin:
                position = secret_pin.find(digit) + 1
                print(digit, "is in the PIN, in position", position)

            else:
                print(digit, "is not in the PIN.")

        print("Attempts left:", 5 - attempts)

if attempts == 5:
    print("ACCESS DENIED!")
    print("The vault is locked.")

print("===== END =====")