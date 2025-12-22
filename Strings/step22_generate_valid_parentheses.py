'''problem statement:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]'''
def is_valid_parentheses(s):
    """
    This function checks whether the given string s
    is a VALID parentheses string.

    Rules:
    - '(' increases the balance by +1
    - ')' decreases the balance by -1
    - At no point should balance go negative
    - At the end balance must be exactly zero
    """

    balance = 0               # Start with 0 open parentheses

    for ch in s:              # Loop through each character in the string
        if ch == '(':         # If current character is an opening bracket
            balance += 1      # Increase balance (one more '(' seen)
        else:                 # Otherwise character must be ')'
            balance -= 1      # Decrease balance (closing one '(')

        if balance < 0:       # Balance going negative means:
                              # more ')' than '(' at this point → invalid
            return False      # So immediately return invalid

    # After the loop finishes:
    # If balance == 0 → every '(' matched with ')'
    # If balance != 0 → some '(' were not closed → invalid
    return balance == 0
#example
print(is_valid_parentheses("((()))"))  # True
print(is_valid_parentheses("(()())"))  # True
