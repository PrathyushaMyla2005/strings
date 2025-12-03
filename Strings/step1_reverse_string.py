'''Problem statement

Given an array of characters s, reverse the characters in-place and return nothing.
ex xample: "Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''
def reverse_string_bruteforce(s: list[str]) -> None:
    """
    Brute force: create reversed list then copy back to s (in-place modification).
    Time: O(n), Space: O(n)
    """
    n = len(s)
    res = []
    # build reversed list
    for i in range(n - 1, -1, -1):
        res.append(s[i])
    # copy back to original array to satisfy "in-place" requirement
    for i in range(n):
        s[i] = res[i]

# Example usage
s = ["h","e","l","l","o"]
reverse_string_bruteforce(s)
print(s)  # ['o', 'l', 'l', 'e', 'h']
def reverse_string_optimal(s: list[str]) -> None:
    """
    Optimal in-place reverse using two pointers.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    while left < right:
        # swap s[left] and s[right]
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Example usage
s = ["h","e","l","l","o"]
reverse_string_optimal(s)
print(s)  # ['o', 'l', 'l', 'e', 'h']
''' rute Force

Time Complexity: O(n) → We loop through all characters twice (build reversed list + copy back).
Space Complexity: O(n) → We create an extra list res of size n.

Optimal (Two Pointers)

Time Complexity: O(n) → Each character is swapped once, so we touch each element only once.
Space Complexity: O(1) → Only two pointers are used, no extra array created.'''