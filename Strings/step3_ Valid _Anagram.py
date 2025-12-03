'''Problem statement

Given two strings s and t, return True if t is an anagram of s, and False otherwise.
An anagram means both strings contain the same characters with the same frequencies (order does not matter)'''
def is_anagram_bruteforce(s, t):
    # If lengths are different, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Sorted versions of both strings
    sorted_s = sorted(s)   # sorts characters of s
    sorted_t = sorted(t)   # sorts characters of t

    # If sorted strings are equal → they have same characters
    return sorted_s == sorted_t
def is_anagram_optimal(s, t):
    # If lengths differ, strings can never be anagrams
    if len(s) != len(t):
        return False

    # Dictionary to store character counts from s
    freq = {}

    # Count characters in s
    for ch in s:
        # freq.get(ch, 0) gives existing count or 0 if not present
        freq[ch] = freq.get(ch, 0) + 1  # add 1 to the count

    # Now use characters from t
    for ch in t:
        # If a character in t was never in s → not anagram
        if ch not in freq:
            return False

        # Use one count of this character
        freq[ch] -= 1

        # If count becomes negative → t has extra letters → not anagram
        if freq[ch] < 0:
            return False

    # If all counts match correctly → strings are anagrams
    return True
print(is_anagram_bruteforce("anagram", "nagaram"))  # True
print(is_anagram_bruteforce("rat", "car"))          # False

print(is_anagram_optimal("anagram", "nagaram"))     # True
print(is_anagram_optimal("rat", "car"))             # False
"""
Time Complexity:
Brute Force Approach: O(n log n) due to sorting both strings.
Optimal Approach: O(n) since we traverse both strings once.
Space Complexity:
Brute Force Approach: O(1) if we ignore the space used for sorting.
Optimal Approach: O(1) since the frequency dictionary will have at most 26 entries for lowercase letters.
"""