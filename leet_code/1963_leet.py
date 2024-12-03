class Solution:

    def balanced(self, s):
        stack = []
        
        for char in s:
            if len(stack) != 0 and (stack[-1] == "[" and char == "]"):
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0

    def minSwaps(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        ss = list(s)
        count = 0

        while i < j:
            if self.balanced(ss) == False:  
                if ss[i] == "]" and ss[j] == "[":
                    ss[i], ss[j] = ss[j], ss[i]  
                    count += 1
                    print(i,j)
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else: 
                break

        print(count)
        # return count

s ="[[[]]]][][]][[]]][[["
sol = Solution()
sol.minSwaps(s)

#  -----------------------------------------------------------------------------

# class Solution:
#     def minSwaps(self, s: str) -> int:
        
#         unbalanced = 0
#         to_balance = 0

#         for i in s:
#             if i == '[':
#                 unbalanced -= 1
#             else:
#                 unbalanced += 1

#             to_balance = max(to_balance,unbalanced)

#         return (to_balance+1)//2
