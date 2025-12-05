'''You have a string made of L and R.

A balanced part means:

👉 Same number of L and R
Example:

"LR" → balanced

"RLLR" → balanced

"RRLL" → balanced

Your job:

✔️ Cut the string into as many balanced pieces as you can.
⭐ THE SIMPLE TRICK

You walk through the string.

You count how many L and how many R you have seen.

Whenever:

👉 L count == R count,
you found a balanced piece.

Increase answer by 1.

⭐ VERY SIMPLE EXAMPLE
Input
s = "RLRRLLRLRL"


We count L and R:

Character	L Count	R Count	Balanced?
R	0	1	No
L	1	1	YES → 1 piece
R	1	2	No
R	1	3	No
L	2	3	No
L	3	3	YES → 2 pieces
R	3	4	No
L	4	4	YES → 3 pieces
R	4	5	No
L	5	5	YES → 4 pieces
✔️ Final Answer = 4
⭐ Another Example (Very easy)
Input
s = "LRLRLR"


Walk through:

L (1), R (1) → equal → 1 piece

L (2), R (2) → equal → 2 pieces

L (3), R (3) → equal → 3 pieces

✔️ Output
3

⭐ Very Simple Example
Input
s = "LLLLRRRR"


After full string:

L = 4

R = 4 → equal → only 1 piece

✔️ Output
1
'''
def balancedStringSplit(s):
    # countL stores number of 'L' seen in the current substring
    # countR stores number of 'R' seen in the current substring
    countL = 0
    countR = 0

    # balanced_count stores total number of balanced substrings found
    balanced_count = 0

    # go through each character in the string one-by-one
    for ch in s:
        # if the character is 'L', increase countL
        if ch == 'L':
            countL += 1
        else:
            # otherwise character must be 'R', so increase countR
            countR += 1

        # if both counts are equal, we got one balanced substring
        if countL == countR:
            balanced_count += 1
            
            # reset for next possible balanced substring
            countL = 0
            countR = 0

    # return total balanced substrings
    return balanced_count
def balancedStringSplit(s):
    balance = 0           # this tracks difference between R and L
    balanced_count = 0    # total balanced substrings found

    for ch in s:          # check each character one-by-one
        
        # If R comes, add +1. If L comes, subtract -1.
        if ch == 'R':
            balance += 1
        else:
            balance -= 1
        
        # When balance becomes 0, it means L and R equal
        if balance == 0:
            balanced_count += 1

    return balanced_count
print(balancedStringSplit("RLRRLLRLRL"))  # Output: 4
print(balancedStringSplit("LRLRLR"))      # Output: 3
print(balancedStringSplit("LLLLRRRR"))    # Output: 1
'''Brute Force

TC: O(n) — we scan the string once.
SC: O(1) — only two counters used.

✅ Optimal Approach

TC: O(n) — one pass through the string.
SC: O(1) — only one variable (balance).
'''