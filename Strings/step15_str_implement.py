'''ou are given two strings:

haystack → the big string

needle → the small string you are searching for

👉 Your task:
Find the index of the first occurrence of needle inside haystack.

If needle does not appear, return -1.

If needle is an empty string "", return 0.

⭐ Understanding With Real-Life Example

Imagine haystack is a paragraph, and needle is a word you want to search.

Example:

haystack = "hello world"
needle   = "world"


Here, the word "world" starts at index 6:

 h e l l o   w o r l d
 0 1 2 3 4 5 6 7 8 9 10
            ↑
      needle found here


So output = 6'''
#brute force
def strStr(haystack, needle):                 # define a function that accepts two strings
    if needle == "":                          # if needle is an empty string
        return 0                              # by rule, return 0

    n = len(haystack)                          # store length of haystack in n
    m = len(needle)                            # store length of needle in m

    # We try every possible starting index i where needle can fit inside haystack
    for i in range(n - m + 1):                # loop from 0 to (n-m)
        match = True                          # assume that needle matches from this index

        # check each character of needle
        for j in range(m):                    # loop through each character of needle
            if haystack[i + j] != needle[j]:  # compare haystack's char with needle's char
                match = False                 # if any character doesn't match → no match
                break                         # break inner loop, no need to check further

        if match == True:                     # if match is still true after checking all characters
            return i                          # return the starting index i

    return -1                                 # after full scan, if no match found → return -1
print(strStr("hello", "ll"))      # Output: 2
print(strStr("sadbutsad", "sad")) # Output: 0
print(strStr("leetcode", "leeto"))# Output: -1
print(strStr("abc", ""))          # Output: 0
'''tc O(n * m) → for each of the n-m+1 starting positions, we may check up to m characters.
sc O(1) → we use only constant extra space.'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":                      # If needle is empty → return 0
            return 0
        
        n = len(haystack)
        m = len(needle)

        # only check up to n - m
        for i in range(n - m + 1):            # start checking from each possible index
            if haystack[i : i + m] == needle: # compare substring directly
                return i                      # match found → return index
        
        return -1                             # no match found
print(Solution().strStr("hello", "ll"))      # Output: 2
print(Solution().strStr("sadbutsad", "sad")) # Output:
print(Solution().strStr("leetcode", "leeto"))# Output: -1
'''tc O(n * m) → slicing creates a new substring of length m for each of the n-m+1 positions.
sc O(m) → slicing creates a new substring of length m.'''
