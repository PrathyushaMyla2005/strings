""" problem: write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string 
example: Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
#brute force approach
def longest_common_prefix_bruteforce(strs):
    if not strs:
        return ""
    
    # Start with the first string as the initial prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the arraY
    for i in range(len(prefix)):
        for word  in strs[1:]:
            # If the current character doesn't match, return the prefix up to this point
            if i >= len(word) or word[i] != prefix[i]:
                return prefix[:i]   
    return prefix
  #optimal approach
def longest_common_prefix_optimal(strs):
    if not strs:
        return ""
    strs.sort()# sort the array 
    first = strs[0]# first string 
    last = strs[-1]# last string
    i = 0 # index to track common prefix length
    while i < len(first) and i < len(last) and first[i] == last[i]:# compare characters each string for example first and last string
        #are flower and flight in this case f and l are same so we continue
        i += 1
    return first[:i]# return the common prefix
print(longest_common_prefix_bruteforce(["flower","flow","flight"])) # "fl"
print(longest_common_prefix_bruteforce(["dog","racecar","car"]))   #
print(longest_common_prefix_optimal(["flower","flow","flight"]))   # "fl"
print(longest_common_prefix_optimal(["dog","racecar","car"]))     # ""
"""
Time Complexity:
Brute Force Approach: O(S) where S is the sum of all characters in all strings.
Optimal Approach: O(n log n) due to sorting the array of strings.
Space Complexity:
Brute Force Approach: O(1) as we use no extra space.
Optimal Approach: O(1) if we ignore the space used by sorting.
"""
