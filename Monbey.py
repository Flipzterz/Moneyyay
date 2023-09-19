pennies = int(input("Enter the number of pennies: "))

dollars = pennies // 100
pennies %= 100

quarters = pennies // 25
pennies %= 25

dimes = pennies // 10
pennies %= 10

nickels = pennies // 5
pennies %= 5

remaining_pennies = pennies

#results
print("Dollar Bills =", dollars)
print("Quarters =", quarters)
print("Dimes =", dimes)
print("Nickels =", nickels)
print("Pennies =", remaining_pennies)
