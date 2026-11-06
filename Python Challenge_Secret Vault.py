print("===== SECRET VAULT 🏦💳💸=====")

secret_pin = "6729"
attempts = 0
max_attempts = 5

while attempts < max_attempts:

    pin = input("Enter your PIN🧑‍💻: ")

    if pin == secret_pin:
        print("ACCESS GRANTED!🥳")
        print("Vault unlocked!🥳")
        break

    else:
        attempts += 1

        print("Incorrect PIN!🤡")

        for i in range(len(secret_pin)):
            if i < len(pin):
                if pin[i] == secret_pin[i]:
                    print("Digit", pin[i], "is correct and in position", i + 1)
                else:
                    print("Digit", pin[i], "is incorrect.")

        remaining = max_attempts - attempts

        if remaining > 0:
            print("Attempts left:", remaining)
        else:
            print("ACCESS DENIED!🤡")
            print("The vault is locked.🤡")

print("===== PROGRAM ENDED =====")