import random  # To generate random values
import string  # To get letters, digits, and symbols

# Define a function to suggest a strong password based on email
def suggest_password(email):
    username = email.split('@')[0]  # Take the part before '@' in the email
    base = username[:4].capitalize()  # Take first 4 letters and capitalize the first letter

    # Combine digits, symbols, and uppercase letters to make the password strong
    extras = string.digits + string.punctuation + string.ascii_uppercase

    # Pick 4 random characters from extras and join them into a string
    random_part = ''.join(random.choice(extras) for _ in range(4))

    # Combine base + random part to make final password
    password = base + random_part

    return password  # Give back the password

# Use the function with an example email
email = "nandhini123@gmail.com"
print("Suggested Password:", suggest_password(email))  # Print the generated password
