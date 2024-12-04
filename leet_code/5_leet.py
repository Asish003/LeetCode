class Solution:
    def longestPalindrome(self, s: str) -> str:

        i = 0
        j = len(s)-1

        while i<=j:

            if s[i] == s[j]:
                print(1)
                if s[i:] == s[:j]:
                    return s

            elif s[i+1] == s[j]:
                print(2)
                if s[i+1:] == s[:j]:
                    return s
    
            elif s[i] == s[j-1]:
                print(3)
                if s[i:] == s[:j-1]:
                    return s
            
            i += 1
            j -= 1
                

s = "babad"
sol = Solution()
ans = sol.longestPalindrome(s)
print(ans)