class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) % 2 == 1:
            return False
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                if len(stack) > 0 and ((char == '}' and stack[-1] == '{') or (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[')):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0