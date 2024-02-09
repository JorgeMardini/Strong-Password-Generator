import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ';', ':', '<', '>', ',', '.', '?', '/']

print("Password Generator")

nr_letters = int(input("How many letters would you like in your password?"))

password_list = []


for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)

nr_numbers = int(input("How many numbers would you like in your password?"))
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

nr_sc = int(input("How many special characters would you like in your password?"))

for char in range(1, nr_sc + 1):
  password_list += random.choice(special_characters)


random.shuffle(password_list)

password = ""

for char in password_list:
  password += char
  
print(f"Your password is: {password}")



