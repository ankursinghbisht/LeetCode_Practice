class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # taking a list as a stack to keep track of the order of the brackets
        bracket_pairs = {')': '(', '}': '{',
                         ']': '['}  # mapping closing brackets to their corresponding opening brackets

        for char in s:
            if char in bracket_pairs.values():  # if the current character is an opening bracket
                stack.append(char)  # push it onto the stack
            else:  # if the current character is a closing bracket
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False  # mismatched brackets or stack is empty

        return not stack  # return True if the stack is empty, indicating all brackets are matched

