'''problem: our job:

Check if the string can become a palindrome
👉 after removing at most ONE character.

That’s it.Input: s = "abca"
Check from left & right:

a == a ✔️

b != c ❌ → mismatch came

We can remove b → string becomes "aca" → palindrome ✔️
'''
#brute force
def validPalindrome(s):

    # function to check a string is palindrome or not
    def is_palindrome(x):
        if x == x[::-1]:   # reverse and compare
            return True
        return False

    # if the original string is already a palindrome
    if is_palindrome(s):
        return True

    # try removing each character
    for i in range(len(s)):
        # make a new string WITHOUT the character at index i
        new_string = s[:i] + s[i+1:]

        # check if this new string becomes palindrome
        if is_palindrome(new_string):
            return True

    # after checking all possibilities
    return False
#optimal
def validPalindrome(s):

    # Helper function to check if s[left:right] is a palindrome
    def is_palindrome(left, right):
        # Move both pointers toward the center
        while left < right:
            # If mismatch occurs → not a palindrome
            if s[left] != s[right]:
                return False
            # Move left pointer forward
            left += 1
            # Move right pointer backward
            right -= 1
        # If loop finishes → it's a palindrome
        return True

    # Start pointers at both ends
    left, right = 0, len(s) - 1

    # Check characters from both sides
    while left < right:
        # If characters match → move inward
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # MISMATCH FOUND — try removing left or right one time only
            # Option 1: skip left character → (left + 1, right)
            # Option 2: skip right character → (left, right - 1)
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)

    # If no mismatch OR mismatch fixed → string is valid palindrome
    return True
print(validPalindrome("abca"))      # Output: True
print(validPalindrome("racecar"))   # Output: True
print(validPalindrome("abc"))      # Output: False
'''Problem Summary
You are given a string s consisting of only the characters 'L' and 'R'.
Your task is to split the string into the maximum number of balanced substrings.    
A balanced substring has an equal number of 'L' and 'R' characters.
📝 Example
Input:
s = "RLRRLLRLRL"
Output:4
Explanation:
The balanced substrings are "RL", "RRLL", "RL", "RL".
💡 Why do we do this?
Balancing strings is a common problem in parsing and data validation.
🚀 Optimal Code (Python
⭐ Very Simple Example
Input
s = "LLLLRRRR" 
After full string:
L = 4
R = 4 → equal → only 1 piece
✔️ Output)'''
'''tc O(n) → we check each character once.
sc O(1) → we use only constant extra space.
for brute force
TC: O(n^2) → In worst case, for each character, we may check
each substring for palindrome.
SC: O(1) → we use only constant extra space.
'''