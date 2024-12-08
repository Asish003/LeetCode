class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        c_max = max(candies)
        final = []

        for i in candies:
            if i + extraCandies >= c_max:
                final.append(True)
            else:
                final.append(False)

        return final