# 1
def print_user_details(first_name, last_name, college, department, mobile_number):
    full_name = first_name + " " + last_name
    college_details = f"{college} Department of {department}"
    
    ascii_name = ', '.join(f"{char}-{ord(char)}" for char in full_name.replace(' ', ''))
    
    ascii_mobile = ', '.join(f"{digit}-{ord(digit)}" for digit in mobile_number)

    addition_results = ', '.join(f"{name_char}+{mob_digit} = {ord(name_char) + ord(mob_digit)}" for name_char, mob_digit in zip(full_name.replace(' ', '')[:4], mobile_number[:4]))

    print(f"Your Name is : {full_name}")
    print(f"Your College Name : {college_details}")
    print(f"ASCII value name is : {ascii_name}")
    print(f"ASCII value of Mobile Number: {ascii_mobile}")
    print(f"Result of Addition: {addition_results}")

print_user_details("Face", "Prep", "XXXXX College", "CSE", "9894")

# 2
def arithmetic_operations(a, b):
    print(f"Addition – {a + b}")
    print(f"Subtraction - {a - b}")
    print(f"Multiplication – {a * b}")
    print(f"Division – {a / b}")
    print(f"Modulus – {a % b}")
    print(f"Exponentiation – {a ** b}")

def swap_three_values(x, y, z):
    print("Before Swapping")
    print(f"First value – {x}")
    print(f"Second value – {y}")
    print(f"Third Value – {z}")

    x = x ^ y ^ z
    y = x ^ y ^ z
    z = x ^ y ^ z
    x = x ^ y ^ z

    print("After Swapping")
    print(f"First value – {x}")
    print(f"Second Value - {y}")
    print(f"Third Value – {z}")

arithmetic_operations(30, 20)
swap_three_values(30, 20, 10)

# 3
import re

def process_username_input(username):
    print(f'Hi ! Your Entered Input is "{re.sub(r"[^a-zA-Z@#$%^&*]", "", username)}"')

def split_characters_and_specials(input_str):
    letters = ''.join(filter(str.isalpha, input_str))
    specials = ''.join(filter(lambda x: not x.isalnum(), input_str))
    print(f"Your entered Characters are – {letters}")
    print(f"Your entered Special Characters are - {specials}")

process_username_input("face123@#$%^")
split_characters_and_specials("faceprep12345!@#$%^&")
