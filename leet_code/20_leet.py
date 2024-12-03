class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for i in s: 
            stack.append(i) 
            if len(stack) > 1: 
                if stack[-1] == ')' and stack[-2] == '(' or stack[-1] == '}' and stack[-2] == '{' or stack[-1] == ']' and stack[-2] == '[':
                        stack.pop()
                        stack.pop()
        if len(stack) == 0: 
            return True
        else: 
            return False