class Solution:
    def largestCombination(self, candidates) -> int:
        
        final = []
        temp = []

        # count = 1
        for i in range(len(candidates)):
            for j in range(i,len(candidates)):
                if candidates[i] & candidates[j] >= 8:
                    temp.append(candidates[j])
            final.append(temp)
            temp = []

        print(final)

        for i in final:
            temp.append(len(i))

        return max(temp)
    
candidates = [10,72,58,33,36,70,12,88,9,48,78,97,87,19,78,9,47,73]
new_sol = Solution()
ans = new_sol.largestCombination(candidates)
print(ans)