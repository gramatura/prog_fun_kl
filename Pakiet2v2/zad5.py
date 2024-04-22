def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(is_palindrome("Kamil Slimak"))
print(is_palindrome("Kamil Nie Slimak"))