import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    if length <= 0:
        raise ValueError("Password length must be greater than zero.")
    
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
    
    password = ''.join(random.SystemRandom().choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length_input = input("Enter password length: ").strip()
        if not length_input.isdigit() or int(length_input) <= 0:
            raise ValueError("Invalid input. Please enter a positive integer.")
        length = int(length_input)
        
        use_digits = input("Include digits? (y/n): ").strip().lower()
        if use_digits not in {'y', 'n'}:
            raise ValueError("Invalid input. Please enter 'y' or 'n'.")
        
        use_specials = input("Include special characters? (y/n): ").strip().lower()
        if use_specials not in {'y', 'n'}:
            raise ValueError("Invalid input. Please enter 'y' or 'n'.")
        
        password = generate_password(length, use_digits == 'y', use_specials == 'y')
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)
