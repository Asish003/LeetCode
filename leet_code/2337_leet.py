class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        if start.replace('_', '') != target.replace('_', ''):
            return False
        i = 0
        j = 0
        temp = 0

        s = list(start)
        t = list(target)
            

        while True:

            if s[i] == t[j]:
                if i == j: #same position, so matches
                    i += 1
                    j += 1
                elif i != j : #matches but different position
                    while i != j and i<len(str):
                        if s[i] == 'L' and s[i- 1] == '_': #checking previous steps
                            s[i],s[i- 1] = s[i-1],s[i] #swapping
                        elif s[i] == 'R' and s[i+ 1] == '_': #checking previous steps
                            s[i],s[i+ 1] = s[i+1],s[i] #swapping
                        else:
                            break
                    if i != j: #Still i is not equal to j after swap, due to interuption
                        return False
                    else: #It means swap is successful so,
                        i += 1
                        j += 1
            elif s[i] != t[j]:
                i += 1




start = "_L__R__R_"
target = "L______RR"
sol = Solution()
ans = sol.canChange(start,target)
print(ans+"done")