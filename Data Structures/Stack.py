"""
1) Valid Parentheses

Problem Statement:
Given a string s containing only the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

A string is valid if:

Open brackets are closed by the same type of brackets.

Open brackets are closed in the correct order.

Input:

A string s (1 ≤ len(s) ≤ 10⁴)

Characters: '(', ')', '{', '}', '[', ']'

Output:

Return True if the string is valid, False otherwise.

Example:

Input: s = "([{}])"
Output: True

Input: s = "([)]"
Output: False

"""
# Taking input for the string
inp = input()

def is_valid_parentheses(s):
    # Tacking a dictionary with closed brackets as keys and open brackets as values
    d = {")":"(", "}": "{", "]": "["}
    # Using list to perform stack
    stack = []
    # Looping through string
    for i in s:
        # Checking if current character in the string is a open bracket . If so, pushing into stack and jumping to next char
        if i in d.values():
            stack.append(i)
            continue
        # Checking if current character in the string is a closed bracket and the top of the stack has the
        # corresponding open bracket. If so, removing the open bracket which was pushed earlier from top of the stack.
        if i in d.keys() and d[i] == stack[-1]:
            stack.remove(d[i])
        # If the top of the stack is not the corresponding open bracket , returning False
        else:
            return False
    #Return true if the brackets are balanced
    return True

print(is_valid_parentheses(inp))