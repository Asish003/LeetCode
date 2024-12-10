class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        stack1 = list(s[::-1])
        stack2 = list(t[::-1])
        # prefix = []
        while stack1 and stack2:
            if stack1[-1] == stack2[-1]:
                # prefix.append(stack1.pop())
                stack2.pop()
            else:
                stack2.pop()
        # prefix.reverse()
        
        if stack1:
            return False
        else:
            return True
