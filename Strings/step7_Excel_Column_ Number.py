'''problem statement: Given a column title as appear in an Excel sheet, return its corresponding column number.
example: Input: "AB"
Output: 28  how came 28 means A=1 B=2 ... Z=26 then AA=27 AB=28 AC=29 and so onBB =54
'''
def excel_column_number_bruteforce(column_title):
    result = 0
    length = len(column_title)
    
    # Loop through each character in the column title
    for i in range(length):
        # Calculate the value of the current character
        char_value = ord(column_title[i]) - ord('A') + 1
        
        # Calculate its positional value and add to result
        result += char_value * (26 ** (length - i - 1))
    
    return result
#optimal approach
def excel_column_number_optimal(column_title):
    result = 0
    
    # Loop through each character in the column title
    for char in column_title:
        # Calculate the value of the current character
        char_value = ord(char) - ord('A') + 1
        
        # Update result by shifting previous result and adding current char value
        result = result * 26 + char_value
    
    return result
print(excel_column_number_bruteforce("A"))    # 1
print(excel_column_number_bruteforce("AB"))   # 28
print(excel_column_number_bruteforce("ZY"))   # 701
print(excel_column_number_optimal("A"))      # 1
print(excel_column_number_optimal("AB"))     # 28
print(excel_column_number_optimal("ZY"))     # 701
'''
Time Complexity:
Brute Force Approach: O(n) where n is the length of the column title.
Optimal Approach: O(n) since we traverse the column title once.
Space Complexity:
Brute Force Approach: O(1) as we use only a constant amount of extra space.
Optimal Approach: O(1) as we use only a constant amount of extra space.
'''
