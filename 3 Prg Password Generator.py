import random
import string

def generate_password():
    print("🔐 Password Generator")
    length = int(input("Enter password length (8-20 recommended): "))

    if length < 4:
        print("⚠️ Length too short. Try again.")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))

    print(f"Generated Password: {password}")

generate_password()
