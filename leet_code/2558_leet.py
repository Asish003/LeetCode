import math 

class Solution:
    def pickGifts(self, gifts, k: int) -> int:
        
        def find_max_index(arr):
            max_index = 0
            for i in range(1, len(arr)):
                if arr[i] > arr[max_index]:
                    max_index = i
            return max_index

        for i in range(k):
            max_index = find_max_index(gifts)
            gifts[max_index] = math.floor(math.sqrt(gifts[max_index]))

        return sum(gifts)
            
            
gifts = [25,64,9,4,100]
k = 4
sol = Solution()
ans = sol.pickGifts(gifts,k)
print(ans)