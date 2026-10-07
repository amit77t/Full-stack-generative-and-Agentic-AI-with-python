str= "Python Programming "

print(type(str))

print(str.upper())  # Convert to uppercase
print(str.lower())  # Convert to lowercase
print(str.strip())  # Remove whitespace from the beginning and end
print(str.replace("Python", "Java"))  # Replace substring
print(str.split())  # Split string into a list of words
print(str.find("Programming"))  # Find the index of a substring
print(str.startswith("Python"))  # Check if string starts with a substring
print(str.endswith("Programming"))  # Check if string ends with a substring
print(str.isalpha())  # Check if all characters are alphabetic
print(str.isdigit())  # Check if all characters are digits
print(str.isalnum())  # Check if all characters are alphanumeric
print(str.count("o"))  # Count occurrences of a substring
print(str.index("P"))  # Find the index of a character
print(str.capitalize())  # Capitalize the first character
print(str.title())  # Capitalize the first character of each word
print(str.swapcase())  # Swap case of all characters
print(str.center(30, "*"))  # Center the string with padding
print(str.ljust(30, "-"))  # Left justify the string with padding
print(str.rjust(30, "-"))  # Right justify the string with padding
print(str.zfill(30))  # Pad the string with zeros on the left


#slicing 

print(str[0:6])   # Python
print(str[7:])    # Programming
print(str[:6])    # Python
print(str[::2])  # Every second character
print(str[::-1]) # Reverse string
print(str[::3])  # Every third character
print(str[1:10:2])  # Characters from index 1 to 9 with step 2


#encoding and decoding
original_str = "Hello, World!"
encoded_str = original_str.encode("utf-8")  # Encode to bytes
print(encoded_str)  # Output: b'Hello, World!'

decoded_str = encoded_str.decode("utf-8")  # Decode back to string
print(decoded_str)  # Output: Hello, World!0