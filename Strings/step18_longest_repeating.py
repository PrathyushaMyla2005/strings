'''problem staement
Given a string s, find the length of the longest substring
that contains only one repeating character.
Example 1:
Input: s = "aaabbbccdaa"
Output: 3
Explanation: The longest substrings with one repeating character are "aaa" and "bbb", both of length 3.
Example 2:
Input: s = "abccccdd"
Output: 4
Explanation: The longest substring with one repeating character is "cccc", with length 4.'''
#brute force approach
# Function to find the length of the longest substring with one repeating character
# in the given string s
# This function uses a brute-force approach to check all possible substrings
# and determine the longest one with a single repeating character.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# n: length of the input string s
# k: length of the longest substring with one repeating character
# Note: This approach is not optimal for large strings due to its quadratic time complexity.
# It is provided here for educational purposes to illustrate the brute-force method.
# For larger strings, consider using a more efficient algorithm.
# Parameters:
def longest_repeating_char_substring(s):
    max_length = 0  # Variable to store the maximum length found

    # Iterate through each character in the string as a potential starting point
    for i in range(len(s)):
        count = 1  # Initialize count for the current character

        # Check subsequent characters to see how many times the current character repeats
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                count += 1  # Increment count if the same character is found
            else:
                break  # Stop counting if a different character is encountered

        # Update max_length if the current count is greater
        max_length = max(max_length, count)

    return max_length
# Example usage:
s = "aaabbbccdaa"
print(longest_repeating_char_substring(s))  # Output: 3
s = "abccccdd"
print(longest_repeating_char_substring(s))  # Output: 4
