import random
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6."

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice("!@#$%^&*()_-=+\\|[]{}:;'\"/?.>")
      ]

    all_characters = lowercase + uppercase + digits
    password = password + random.choices(all_characters, k = length - len(password))

    random.shuffle(password)

    return ''.join(password)

password_lenght = int(input("Enter password lenght: "))
password = generate_password(password_lenght)

print(f"Generated password: {password}")