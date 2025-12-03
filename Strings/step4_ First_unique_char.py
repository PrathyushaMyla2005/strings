'''Problem Statement

Given a string s, return the index of the first character that appears only once in the string.
If no such character exists, return -1.'''
def first_unique_char_bruteforce(s):
    # Loop through every index in the string
    for i in range(len(s)):
        
        # Count how many times the character at index i appears in s
        # s.count(s[i]) scans the whole string and counts occurrences
        if s.count(s[i]) == 1:
            
            # If the character appears only one time, this is the answer
            return i
    
    # If no unique character was found, return -1
    return -1
def first_unique_char_optimal(s):
    # Dictionary to store how many times each character appears
    freq = {}

    # First pass: count characters in the string
    for ch in s:
        # freq.get(ch, 0) returns the current count if present,
        # or 0 if the character is not in the dictionary yet.
        freq[ch] = freq.get(ch, 0) + 1

    # Second pass: find the first character with count = 1
    for i in range(len(s)):
        # Check if this character appears only once
        if freq[s[i]] == 1:
            # Return the index of the first unique character
            return i

    # If no unique character exists, return -1
    return -1
print(first_unique_char_bruteforce("leetcode"))      # 0
print(first_unique_char_bruteforce("loveleetcode"))  # 2
print(first_unique_char_bruteforce("aabb"))          # -1

print(first_unique_char_optimal("leetcode"))         # 0
print(first_unique_char_optimal("loveleetcode"))     # 2
print(first_unique_char_optimal("aabb"))             # -1
"""
Time Complexity:
Brute Force Approach: O(n^2) because for each character we count its occurrences in
the string.
Optimal Approach: O(n) since we traverse the string twice.
Space Complexity:
Brute Force Approach: O(1) as we use no extra space.
Optimal Approach: O(1) since the frequency dictionary will have at most 26 entries for lowercase letters"""
