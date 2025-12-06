'''xample 1:

Input:
s = "babad"

Possible palindromes: "bab", "aba"
Both length 3.
Output: "bab" (or "aba" is also correct)
Example 2:
Input:
s = "cbbd"
Output: "bb"
Explanation: The longest palindromic substring is "bb".
'''
def longestPalindrome(s):
    n = len(s)                 # length of the string
    longest = ""               # this will store the longest palindrome found

    # try every possible starting index i
    for i in range(n):
        # try every possible ending index j (substring ends at j-1)
        for j in range(i + 1, n + 1):
            sub = s[i:j]       # take substring from index i to j-1

            # check if 'sub' is palindrome using reverse string
            if sub == sub[::-1]:
                
                # if this palindrome is longer than the current longest
                if len(sub) > len(longest):
                    longest = sub   # update longest palindrome

    return longest               # return the final answer
# Example usage:
s = "babad"
print(longestPalindrome(s))  # Output: "bab" or "aba"
s = "cbbd"
print(longestPalindrome(s))  # Output: "bb"
'''tc: O(n^3) because we are checking all substrings (O(n^2)) and for each substring we are checking if it is a palindrome (O(n)).
sc: O(1) if we don't count the output string, otherwise O(n) for storing the longest palindrome.
n: length of the input string s'''
