class Solution:
    def reverseVowels(self, s: str) -> str:
        
        v = set("aeiouAEIOU")
        vowels = {}

        for i in v:
            if i not in vowels:
                vowels[i] = 1

        
        s = list(s) 
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1

        return ''.join(s)