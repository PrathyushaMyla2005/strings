"""problem statement
Given a string s and a non-empty string p, find all the start indices of p's
anagrams in s.
Strings consists of lowercase English letters only and the length of both
strings s and p will not be larger than 20,100.
The order of output does not matter.
Example 1:
Input: s: "cbaebabacd" p: "abc
Output: [0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:  
Input: s: "abab" p: "ab"
Output: [0, 1, 2]
Explanation:    
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab"."""
def find_anagrams(s, p):
    # List to store all starting indices where an anagram of p is found in s
    result = []

    # Sort the pattern string p.
    # Why? Because any anagram of p will have the same sorted characters.
    p_sorted = ''.join(sorted(p))

    # Store the length of the pattern once (used many times)
    k = len(p)

    # Loop through string s and check every substring of length k
    # (We stop at len(s) - k + 1 to avoid going out of bounds)
    for i in range(len(s) - k + 1):

        # Extract the substring of s starting at index i with length k
        sub = s[i : i + k]

        # Sort the substring and compare with sorted p.
        # If they match → this substring is an anagram of p.
        if ''.join(sorted(sub)) == p_sorted:
            # If it is an anagram, record the starting index i
            result.append(i)

    # Return the list of all indices where anagrams were found
    return result


# Example usage
s = "cbaebabacd"
p = "abc"

# Should print: [0, 6]
print(find_anagrams(s, p))
s = "abab"
p = "ab"
# Should print: [0, 1, 2]
print(find_anagrams(s, p))
s = "abab"
p = "abc"
# Should print: []
print(find_anagrams(s, p))
'''tc: O(n * k log k) because for each of the n-k+1 substrings of length k, we sort the substring which takes O(k log k) time.
sc: O(k) for storing the sorted version of p and the substring.
'''
