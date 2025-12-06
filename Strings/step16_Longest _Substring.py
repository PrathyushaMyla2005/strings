'''problem statement
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.'''
def lengthOfLongestSubstring(s):
    max_len = 0                     # will store the longest substring length

    # Try every index 'i' as the starting point of a substring
    for i in range(len(s)):
        seen = set()               # stores characters found in current substring

        # Extend substring from index i to j
        for j in range(i, len(s)):

            # If a character repeats → stop this substring
            if s[j] in seen:
                break

            # Otherwise add the character and update length
            seen.add(s[j])                     # add current character
            current_length = j - i + 1         # compute length of substring s[i:j+1]
            max_len = max(max_len, current_length)  # update global longest length

    return max_len
# Example usage:
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3
