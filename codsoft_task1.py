import random
import string

def generate_password(length=10):
    # We Define a string containing characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # We Generate a random password by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    
    if password_length < 10:
        print("Sorry, Password length should be at least 10 characters.")
    else:
        password = generate_password(password_length)
        print(f"Generated Password: {password}")

    
