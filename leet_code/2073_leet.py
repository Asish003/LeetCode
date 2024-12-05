class Solution:
    def timeRequiredToBuy(self, tickets, k) -> int:
        
        count = 0
        arr = []
        for i in range(len(tickets)):
            arr.append(i)

        while tickets[arr.index(k)] != 0:
            print(arr)
            print(tickets)
            print()

            if tickets[0] != 0:
                tickets[0] = tickets[0] - 1
                a = tickets.pop(0)
                tickets.append(a)
                count = count + 1
            else:
                a = tickets.pop(0)
                tickets.append(a)

            b = arr.pop(0)
            arr.append(b)

        return count




tickets = [5,1,1,1]
k = 0
sol = Solution()
ans = sol.timeRequiredToBuy(tickets,k)
print(ans)