'''problem statement:
You are given two binary strings a and b.
Your task is to return their sum as a binary string.
📝 Example
Input:
a = "11", b = "1"
Output:"100"
💡 Why do we do this?
Adding binary strings is a common operation in computer science, especially in low-level programming and digital circuit design.
🚀 O)'''
#brute
def addStrings(num1, num2):
    # convert both strings to integers
    n1 = int(num1)
    n2 = int(num2)

    # add the integers
    total = n1 + n2

    # convert back to string
    return str(total)
def addStrings(num1, num2):
    i = len(num1) - 1  # pointer for num1 (rightmost digit)
    j = len(num2) - 1  # pointer for num2 (rightmost digit)
    carry = 0
    result = []

    # Add until both numbers and carry are processed
    while i >= 0 or j >= 0 or carry:
        n1 = int(num1[i]) if i >= 0 else 0   # digit from num1
        n2 = int(num2[j]) if j >= 0 else 0   # digit from num2

        total = n1 + n2 + carry             # sum of digits
        result.append(str(total % 10))       # store last digit
        carry = total // 10                  # update carry

        i -= 1
        j -= 1

    # reverse the result because we built it from right to left
    return ''.join(result[::-1])
print(addStrings("11", "1"))        # Output: "12"
print(addStrings("456", "77"))      # Output: "533"
'''tc O(max(n, m)) → we traverse both strings once.
sc O(max(n, m)) → result can be at most max(n, m) + 1 digits long.
✅ Optimal (digit-by-digit addition)
brute force
tc` O(n) — we scan the string once.
sc O(1) — only two counters used.
'''