# monotonicstack implementation

class Solution:
    def maxWidthRamp(self, nums) -> int:

        stack = []
        max_width = 0

        for i in range(len(nums)): 
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
            
        print(stack)

        for j in range(len(nums)-1,-1,-1): 
            while stack and nums[j]>=nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width,j-i)

        print(max_width)
        return max_width