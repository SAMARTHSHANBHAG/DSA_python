# Write a function to check if a given string is a palindrome. A palindrome is a word, phrase, 
# or sequence that reads the same backward as forward (ignoring spaces, punctuation, and case).
# Example: -
# Input: "madam"  
# Output: True  

# Input: "hello"  
# Output: False

def is_palindrome(s):
    # Reverse the string using slicing
    reversed_s = s[::-1]
    
    # Compare the original string with the reversed one
    return s == reversed_s

# Example Usage
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
