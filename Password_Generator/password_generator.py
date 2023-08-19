import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/'] 

print("Welcome to the Py password generator.\n")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

# Generate random components for the password

random_letters = [random.choice(letters) for _ in range(nr_letters)]
random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

# Combine the components and shuffle

password_components = random_letters + random_numbers + random_symbols
random.shuffle(password_components)

# Generate the final password by joining the components

final_password = ''.join(str(component) for component in password_components)
print("Generated Password:", final_password)
