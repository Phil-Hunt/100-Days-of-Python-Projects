print("Welcome to the tip calculator\n")
bill = float(input("How much is the bill? $"))
people = int(input("How many people are paying? "))
tip_input = input("How much do you want to tip? 10%, 12% or 15% ? ")

# Remove '%' symbol and convert to integer

tip = None
try:
    tip = int(tip_input.rstrip('%'))
except ValueError:
    print("Invalid tip input.")
    exit()

if tip == 10:
    bill_with_tip = bill * 1.10
elif tip == 12:
    bill_with_tip = bill * 1.12
elif tip == 15:
    bill_with_tip = bill * 1.15
else:
    print("Invalid tip percentage selected.")
    exit()

amount_per_person = bill_with_tip / people

print(f"Each person should pay: ${round(amount_per_person, 2)}")
