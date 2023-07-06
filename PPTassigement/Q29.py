def is_palindrome(value):
    lower = value.lower()
    return value == value[::-1]

print(is_palindrome(input('Enter the value: ')))
