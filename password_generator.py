import random
import string

print("🔐 Password Generator")

# Get length from user
length = int(input("Enter password length: "))

# Characters to use
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

print("Generated Password:", password)