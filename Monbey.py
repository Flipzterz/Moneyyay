def null():
    print("")

pennies = int(input("Enter your desired number of pennies: "))

dollars = pennies // 100
pennies %= 100

quarters = pennies // 25
pennies %= 25

dimes = pennies // 10
pennies %= 10

nickels = pennies // 5
pennies %= 5

remaining_pennies = pennies

total = dollars + quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + remaining_pennies * 0.01

# Print results
print("Dollar Bills =", dollars)
print("Quarters =", quarters)
print("Dimes =", dimes)
print("Nickels =", nickels)
print("Pennies =", remaining_pennies)
print("Total Money: $", total)
