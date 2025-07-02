import random
import string
import time

def generate_password(length,complexity):
    """
    Generates a random password of the specified length and complexity.
    Complexity and length are independent.

    Args:
        length (int): The desired length of the password.
        complexity_level (int):
            1: Basic (lowercase, digits)
            2: Medium (lowercase, uppercase, digits)
            3: Strong (lowercase, uppercase, digits, symbols)

    Returns:
        str: The generated password or an error message.
    """
    if length < 1:
        return "Error: Password length must be at least 1 character."
    
    character_pool = ""

    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if complexity == 1:
        character_pool = lower_case + digits
    elif complexity == 2:
        character_pool = lower_case + digits + upper_case
    elif complexity == 3:
        character_pool = lower_case + digits + upper_case + symbols
    else:
        return "invalid complexity level. Please choose 1, 2 or 3"

    # Generating the password -
    password = ''.join(random.choice(character_pool) for _ in range(length))

    return password

def main():

    # welcome message
    print("="*45)
    print("✨ WELCOME TO THE PASSWORD GENERATOR! ✨")
    print("="*45,"\n")

    # Getting password length 
    while True:
        try:
            length = int(input("How long the password length is required : "))
            if(length < 1):
                print("Sorry! password length must be at least 1. Please try again.\n")
            else:
                break
        except ValueError:
            print("Try again!\n")

    # Getting Complexity Level
    print("\n")
    print("Choose your password's strength level:")
    print(" 1️⃣  Basic: (lowercase letters & numbers)")
    print(" 2️⃣  Medium: (basic + UPPERCASE letters)")
    print(" 3️⃣  Strong: (medium + symbols)")
    print("\n")

    while True:
        try:
            complexity_level = int(input("Enter your choice (1, 2, or 3): "))
            if complexity_level not in [1, 2, 3]:
                print("Sorry! That's not in 1, 2, 3.Pick one of the option\n")
            else:
                break
        except ValueError:
            print("Try again!\n")

    print("Generating password ...")
    time.sleep(1) # a small delay 
    password = generate_password(length,complexity_level)

    print("🎉 Your password with complexity level ",complexity_level," and length ",length," is : ",password)

if __name__ == "__main__":
    main()


    
   