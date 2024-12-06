class Solution:
    def maxCount(self, banned, n: int, maxSum: int) -> int:
        
        def var(num):
            if num in book:
                return 0
            else:
                return num
            

        book = {}
        for i in banned:
            book[i] = i

        i = 0
        count = 0
        check = 0
        while i<=n:
            temp = var(i) 
            check = check + temp
            print(f"{check}={check}+{temp}")

            if check>maxSum:
                break
            if temp != 0:
                count = count + 1

            i+= 1

        return count

banned = [1,2,3,4,5,6,7]
n = 7+1
maxSum = 1
sol = Solution()
ans = sol.maxCount(banned ,n, maxSum)
print(ans)