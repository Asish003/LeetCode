import math

class Solution:
    def maxKelements(self, nums, k: int) -> int:
        
        score = 0
        arr = []

        for i in range(k):
            nums.sort(reverse=True)
            score = score + nums[0]
            print(nums[0])
            nums[0] = math.ceil(nums[0]/3)
        
        print(score)
        return score


nums = [1,10,3,3,3]
k = 3
obj = Solution()
ans = obj.maxKelements(nums,k)
print(ans)

