''' valid palindrome: means that after removing all non-alphanumeric characters and ignoring cases,
the string reads the same forwards and backwards.
Problem statement
Given a string s, determine if it is a valid palindrome.
Example: "A man, a plan, a canal: Panama" is a valid palindrome.
    input: s = "A man, a plan, a canal: Panama"
    output: True'''
# Brute-force approach: build a cleaned string and compare with its reverse
def is_palindrome_bruteforce(s):
    result = ""  # store only letters/digits in lowercase

    # build cleaned lowercase string
    for ch in s:
        if ch.isalnum():        # keep only letters and digits
            result += ch.lower()

    # check if cleaned string equals its reverse
    return result == result[::-1]


# -------------------------
# Simple examples
# -------------------------

print(is_palindrome_bruteforce("A man, a plan, a canal: Panama"))  
# True

print(is_palindrome_bruteforce("race a car"))  
# False
# Optimal approach: two pointers, no extra string created
def is_palindrome_optimal(s):
    left = 0
    right = len(s) - 1

    while left < right:

        # skip non-alphanumeric on left
        while left < right and not s[left].isalnum():
            left += 1

        # skip non-alphanumeric on right
        while left < right and not s[right].isalnum():
            right -= 1

        # compare lowercase characters
        if s[left].lower() != s[right].lower():
            return False

        # move inward
        left += 1
        right -= 1

    return True


# -------------------------
# Simple examples
# -------------------------

print(is_palindrome_optimal("A man, a plan, a canal: Panama"))  
# True

print(is_palindrome_optimal("race a car"))  
# False
"""✅ Brute Force

Time Complexity: O(n) → we traverse the whole string once to build result and once to compare with its reverse.
Space Complexity: O(n) → we create a new cleaned string of size up to n.

✅ Optimal (Two Pointers)

Time Complexity: O(n) → each character is checked at most once while moving left and right pointers.
Space Complexity: O(1) → uses only two pointers, no extra string is created."""