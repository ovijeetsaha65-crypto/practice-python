print("Welcome to the Sample String")
def count_characters(text):
    alphabets = 0
    digits = 0
    special_chars = 0

    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            alphabets += 1
        # Check if the character is a number
        elif char.isdigit():
            digits += 1
        # Everything else (including spaces) is a special character
        else:
            special_chars += 1

    print(f"The number of Alphabets in the string is: {alphabets}")
    print(f"The number of Digits in the string is : {digits}")
    print(f"The number of Special characters in the string is: {special_chars}")

sample_string = input("Enter Your String: ")
count_characters(sample_string)