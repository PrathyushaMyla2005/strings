'''problem statement
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
'''
def groupAnagrams(strs):                     # function receives list of strings
    groups = []                              # stores final answer → list of groups (each group = list of anagrams)

    for word in strs:                        # pick each word one by one
        placed = False                       # flag to check if word is added to any existing group

        # ----------------------------------------------------------
        # Try to place the word inside an existing group
        # ----------------------------------------------------------
        for group in groups:                 # check every group we have already created
            # Compare sorted version of current word and first word in this group
            if sorted(word) == sorted(group[0]):
                group.append(word)           # anagram found → add the word to this group
                placed = True                # mark as placed
                break                        # no need to check other groups

        # ----------------------------------------------------------
        # If the word didn't match any group, create a new group
        # ----------------------------------------------------------
        if not placed:                       # if not added anywhere
            groups.append([word])            # make a new group with this word

    return groups                             # return all groups
# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
strs = [""]
print(groupAnagrams(strs))
'''tc = O(n * k log k) beacause for each of the n strings we are sorting a string of length k
sc = O(n * k) because we are storing all the strings in the hashmap
where n is the number of strings in the input list and k is the maximum length of a string in the list.
n: number of strings in the input list'''
