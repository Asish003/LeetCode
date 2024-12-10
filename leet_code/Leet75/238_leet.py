class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1

        left = []
        right = []
        ans = []

        for i in range(len(nums)-1):
            if i == 0: 
                left.append(prod)

            prod = prod * nums[i]
            left.append(prod)
        
        prod = 1

        for i in range(len(nums)-1,0,-1):
            if i == len(nums)-1: 
                right.append(prod)
            
            prod = prod * nums[i]
            right.insert(0,prod)

        for i in range(len(nums)): 
            ans.append(left[i] * right[i])
        
        return ans
