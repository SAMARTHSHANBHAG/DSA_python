# Given a string s, find the first non-repeating character and return its index. If it doesn't exist, return -1.

# Input: s = "leetcode"
# Output: 0

# Input: s = "loveleetcode"
# Output: 2

# Input: s = "aabb"
# Output: -1

def first_unique_character(s):
    # Step 1: Count the frequency of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Step 2: Find the first unique character
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    # Step 3: If no unique character exists
    return -1

# Example Usage
print(first_unique_character("leetcode"))       # Output: 0
print(first_unique_character("loveleetcode"))  # Output: 2
print(first_unique_character("aabb"))          # Output: -1

