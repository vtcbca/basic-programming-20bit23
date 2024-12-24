def is_palindrome_reversed(s):
    return s == ''.join(reversed(s))

input_str = input("Enter a string: ").lower()
if is_palindrome_reversed(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")
