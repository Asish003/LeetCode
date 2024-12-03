class Solution:
    def minLength(self, s: str) -> int:
        list_s = list(s) 
        i = 0

        while i < len(list_s) - 1:
            if list_s[i] + list_s[i + 1] == "AB" or list_s[i] + list_s[i + 1] == "CD":
                list_s.pop(i)
                list_s.pop(i)
                i = max(i - 1, 0)
            else:
                i += 1

        return len(list_s)

sol = Solution()
string = "ACBBD"
print(sol.minLength(string))  
