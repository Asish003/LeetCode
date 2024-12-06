class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        # if start.replace('_', '') != target.replace('_', ''):
        #     return False

        i = 0
        j = 0
        count = 0

        s = list(start)
        t = list(target)

        while True:
            if s[i] == s[j]:
                if count>0 and target[i] == 'L':
                    i += 1
                    j += 1
                    count = 0
            elif t[j] == 'L' and s[i] == '_':
                i += 1
                count = count + 1
            elif t[j] == 'R' and s[i] == '_':
                i += 1
                count = count + 1
            
# start = "___L__R__R_"
# target = "L________RR"

# start = "R_L_"
# target = "__LR"

start ="_LL__R__R_"
target ="L___L___RR"

sol = Solution()
ans = sol.canChange(start,target)
print(ans)