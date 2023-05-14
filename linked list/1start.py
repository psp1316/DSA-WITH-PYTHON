import random

def generate_random_password():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = ""

    for i in range(16):
     password += random.choice(characters)
    return password

print(generate_random_password())