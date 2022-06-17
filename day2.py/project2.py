# To generate a tip calculator

print("Welcome to tip Calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage of tip would you like to give? 10,12,15 ? (in %) "))
people = int(input("How many people to split the bill? "))
totaltip = bill * (tip/100)
print("Each person should pay $ ", round((bill+totaltip)/people,2))