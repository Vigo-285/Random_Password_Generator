import string
import random

def generate_password(length=12, uppercase=True, lowercase = True, digits=True, special_chars = True):
    characters = ''
    if uppercase:
        characters +=string.ascii_uppercase
    if lowercase: 
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation
    if not characters:
        print("Error: At least one charater type must be selected")
        return None

    password = ''.join(random.choice(characters) for _ in range (length))
    return password



print("welcom")
print("you can customize your password by selecting the character types to include")


password_length = int(input("enter the length of the password: "))

include_uppercase = input("include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase= input("include lowercase letters? (y/n): ").lower() == 'y'
include_digits= input("include digits? (y/n): ").lower() == 'y'
include_special_chars= input("include special characters? (y/n): ").lower() == 'y'

#generates the password bassed on user inputs
generate_password = generate_password(
    length=password_length,
    uppercase=include_uppercase,
    lowercase=include_lowercase,
    digits=include_digits,
    special_chars=include_special_chars

)

if generate_password:
    print("generated password: ",generate_password)
else:
    print("no password generated. Please try again ")




