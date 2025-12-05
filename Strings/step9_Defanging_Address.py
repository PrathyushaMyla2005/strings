"""problem statement:
explain
Problem Summary

You are given a valid IP address as a string.
Your task is to replace every dot (.) in the IP address with [.].

This makes the IP address safe so it cannot be clicked as a link.

📝 Example

Input:

"1.1.1.1"


Output:

"1[.]1[.]1[.]1"

💡 Why do we do this?

Defanging is used to avoid hyperlinks in emails or security logs.
For example,
1.1.1.1 → clickable
1[.]1[.]1[.]1 → NOT clickable (safe)

🚀 Optimal Code (Python)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Replace every '.' with '[.]' to make the IP address safe
        return address.replace(".", "[.]")

🧪 Example Usage
sol = Solution()
print(sol.defangIPaddr("1.1.1.1"))           # Output: 1[.]1[.]1[.]1
print(sol.defangIPaddr("255.100.50.0"))      # Output: 255[.]100[.]50[.]0
"""
def defangIPaddr(address):
    result = ""              # step 1: empty string to store output
    
    for ch in address:       # step 2: loop through each character
        if ch == ".":        # step 3: if the character is a dot
            result += "[.]"  # replace dot with "[.]"
        else:
            result += ch     # otherwise add the same character
    
    return result            # step 4: return final defanged IP
def defangIPaddr(address):
    return address.replace(".", "[.]")
print(defangIPaddr("1.1.1.1"))           # Output: 1[.]1[.]1[.]1
print(defangIPaddr("255.100.50.0"))      # Output: 255[.]100[.]50[.]0
'''Brute Force

TC: O(n) → we check each character once.

SC: O(n) → we build a new output string.

✅ Optimal (replace)

TC: O(n) → replace() scans the whole string once.

SC: O(n) → it returns a new modified string.'''