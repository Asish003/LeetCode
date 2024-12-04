class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        if len(str1)<len(str2):
            return False
        
        req = len(str2)
        s1 = list(str1)
        s2 = list(str2)

        count = 0 

        while len(s1)!= 0 and len(s2)!= 0:
            print(s1)
            print(s2)
            if s2[-1] == s1[-1] or ord(s2[-1]) == ord(s1[-1])+1 or (s1[-1] == 'z' and s2[-1] == 'a'):
                count = count + 1
                s1.pop()
                s2.pop()
            else:
                s1.pop()
            
        print(count) 

        if count == req:
            return True
        return False
    

str1 = "zc"
str2 = "ad"

sol = Solution()
ans = sol.canMakeSubsequence(str1,str2)
print(ans)