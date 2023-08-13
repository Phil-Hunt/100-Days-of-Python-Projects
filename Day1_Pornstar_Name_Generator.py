print("Hi, I'll generate a pornstar name for you\n")
street = input("What was the name of the first street you lived on?\n")
pet = input("What was the name of your first pet?\n")

# Split the street input by spaces and take the first part as people will naturally include the type of street after the name.

street_parts = street.split()
first_street_name = street_parts[0]

print("Your pornstar Name is " + pet + " " + first_street_name)