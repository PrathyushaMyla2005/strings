'''problem: Write a function that takes a string as input and returns the length of the last word in the
string. A word is defined as a maximal substring consisting of non-space characters only.
example: Input: "Hello World"
Output: 5
'''
def length_of_last_word_bruteforce(s):
    # split() removes extra spaces and keeps only words
    words = s.split()
    
    # the last word is the last element of the list
    last_word = words[-1]
    
    # return length of that last word
    return len(last_word)
def length_of_last_word_optimal(s):
    i = len(s) - 1  # start from the last index
    length = 0      # this will store the count of last word

    # Step 1: Skip trailing spaces
    while i >= 0 and s[i] == " ":
        i -= 1

    # Step 2: Count characters of the last word
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1

    return length
print(length_of_last_word_bruteforce("Hello World"))  # 5
print(length_of_last_word_bruteforce("   fly me   to   the moon  "))  # 4
print(length_of_last_word_bruteforce("luffy is still joyboy"))  #
print(length_of_last_word_optimal("Hello World"))  # 5
print(length_of_last_word_optimal("   fly me   to   the moon  "))
print(length_of_last_word_optimal("luffy is still joyboy")) 
'''
Time Complexity:
Brute Force Approach: O(n) due to the split operation which scans the entire string.
Optimal Approach: O(n) since we may need to traverse the string twice in the worst case.
Space Complexity:
Brute Force Approach: O(m) where m is the length of the last word, due
to the storage of the split words.
Optimal Approach: O(1) as we use only a constant amount of extra space.
'''
