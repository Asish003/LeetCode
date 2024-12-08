import math

class Solution:
    def minimumSize(self, nums, maxOperations) -> int:

        a = sorted(nums,reverse=True)
        print(a)

        for i in range(maxOperations):
            if sorted(a) != a:
                a.sort(reverse=True)
            if a[0] == max(a):
                if a[0]/2 != int:
                    ins1 = math.ceil(a[0]/2)
                    ins2 = math.floor(a[0]/2)
                else:
                    ins1 = ins2 = a[0]//2

                a.pop(0)
                a.insert(0,ins1)
                a.insert(1,ins2)

        return a
            

nums = [2,4,8,2]
maxOperations = 4
sol = Solution()
ans = sol.minimumSize(nums,maxOperations)
print(ans)