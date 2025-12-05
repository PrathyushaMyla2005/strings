'''problem statement: Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:'''
def upper(word):
    # This function checks if ALL characters in the word are uppercase.
    for ch in word:                 # Loop through each character in the word
        if not ch.isupper():        # If any character is NOT uppercase
            return False            # Rule fails → return False
    return True                     # All characters uppercase → return True


def lower(word):
    # This function checks if ALL characters in the word are lowercase.
    for ch in word:                 # Loop through each character
        if not ch.islower():        # If any character is NOT lowercase
            return False            # Rule fails → return False
    return True                     # All characters lowercase → return True


def first_upper(word):
    # This function checks if FIRST letter is uppercase,
    # and all remaining letters are lowercase.

    if not word[0].isupper():       # Check first letter is uppercase
        return False                # If not uppercase → invalid

    for ch in word[1:]:             # Loop through all letters except the first
        if not ch.islower():        # If any remaining letter is NOT lowercase
            return False            # Rule fails → return False
            
    return True                     # First letter uppercase + rest lowercase → True


def detectCapitalUse(word):
    # This function applies all 3 rules.
    
    # If ANY of the three functions return True → correct usage of capitals
    if upper(word) or lower(word) or first_upper(word):
        return True                 # Valid capitalization pattern found
    else:
        return False                # None of the rules matched → invalid


# Take input from user
word = input("Enter the word: ")

# Print result
print(detectCapitalUse(word))
def detectCapitalUse(word):
    # Case 1: All letters are uppercase
    if word.isupper():
        return True
    
    # Case 2: All letters are lowercase
    if word.islower():
        return True
    
    # Case 3: First letter uppercase + rest lowercase
    if word[0].isupper() and word[1:].islower():
        return True
    
    # Otherwise invalid capital usage
    return False
'''tim e complexity: O(n), where n is the length of the word. We may need to check each character in the word to determine its case.
space complexity: O(1), as we are using a constant amount of extra space regardless of
 the input size.
 for brute force approach
 tc : O(1) because we are using built-in functions which are optimized
 sc: O(1) because we are not using any extra space'''