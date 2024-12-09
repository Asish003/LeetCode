class Solution:
    def isArraySpecial(self, nums, queries):

        low = float('inf')
        high = float('-inf')

        for i in range(len(queries)):
            low = min(queries[i]) if min(queries[i]) < low else low
            high = max(queries[i]) if min(queries[i]) > high else high

        print(low,high)



nums = [3,4,1,2,6]
queries = [[0,4]]
sol = Solution()
ans = sol.isArraySpecial(nums,queries)
print(ans)