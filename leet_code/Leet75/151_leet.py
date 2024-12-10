class Solution:
    def reverseWords(self, s: str) -> str:

        
        a = s.strip().split()
        a = a[::-1]
        size =  len(a)-1

        string =''

        for i in a:
            string = string  + i
            if size>0:
                string = string + " "
                size -= 1

        return string



