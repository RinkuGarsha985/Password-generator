import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Password Generator")

    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_digits, use_symbols)
        print(f"\n✅ Generated Password: {password}")

    except ValueError:
        print("❌ Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()