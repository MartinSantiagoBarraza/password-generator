import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_pass = ""
random_letters = random.choices(letters, k=nr_letters)
random_numbers = random.choices(numbers, k=nr_numbers)
random_symbols = random.choices(symbols, k=nr_symbols)

str_letters = str(random_letters)
str_numbers = str(random_numbers)
str_symbols = str(random_symbols)

simple_letters = ' '.join(str_letters)
simple_numbers = ' '.join(str_numbers)
simple_symbols = ' '.join(str_symbols)

random_pass += simple_letters+simple_numbers+simple_symbols

password = ""
for char in random_pass:
  password += char

print(f"The characters you can use for your password are: {password}")