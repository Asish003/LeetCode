class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        new = ""

        try:
            while i < len(word1) or j < len(word2):
                if i < len(word1): 
                    new = new + word1[i]
                if j < len(word2):
                    new = new + word2[i]
                i = i + 1
                j = j + 1
        except: 
            print("Array index out of range")

        print(new)
        return new