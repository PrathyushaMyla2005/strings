'''problem statement:
You are given two binary strings a and b.
Your task is to return their sum as a binary string.
📝 Example
Input:
a = "11", b = "1"
Output:"100"
💡 Why do we do this?
Adding binary strings is a common operation in computer science, especially in low-level programming and digital circuit design.
'''#brute force
def addBinary(a, b):
    # Step 1: Convert binary strings to integers
    num1 = int(a, 2)   # convert string 'a' to integer (base 2)
    num2 = int(b, 2)   # convert string 'b' to integer (base 2)

    # Step 2: Add the two integers
    total = num1 + num2

    # Step 3: Convert the integer back to binary string
    result = bin(total)[2:]   # bin() gives '0bxxxx', so remove '0b'

    return result
print(addBinary("11", "1"))        # Output: "100"
print(addBinary("1010", "1011"))   # Output: "10101"
#optimal
def addBinary(a, b):
    result = []          # To store the result bits
    carry = 0           # Initialize carry to 0
    i, j = len(a) - 1, len(b) - 1  # Pointers for a and b

    # Loop until both strings are processed or there's a carry
    while i >= 0 or j >= 0 or carry:
        sum = carry     # Start with the carry

        if i >= 0:      # If there are still bits in a
            sum += int(a[i])  # Add bit from a
            i -= 1

        if j >= 0:      # If there are still bits in b
            sum += int(b[j])  # Add bit from b
            j -= 1

        result.append(str(sum % 2))  # Append the bit (0 or 1)
        carry = sum // 2              # Update carry (0 or 1)

    return ''.join(reversed(result))  # Reverse and join to form final 
print(addBinary("11", "1"))        # Output: "100"
print(addBinary("1010", "1011"))   # Output: "10101"
"""tc O(max(n, m)) → we traverse both strings once.
sc O(max(n, m)) → result can be at most max(n, m) + 1 bits long.
✅ Optimal (bit-by-bit addition)
brute force
)"""