class Solution:
    def maximumBeauty(self, items, queries):
        book = {}
        for key, value in items:
            if key not in book:
                book[key] = value
            else:
                book[key] = max(book[key], value)

        print("Book Dictionary:", book)

        arr = []
        max_so_far = 0
        sorted_keys = sorted(book.keys())  
        for query in queries:
            for key in sorted_keys:
                if key <= query:
                    closest_max = max(closest_max, book[key])
                else:
                    break
            arr.append(closest_max)

        print("Result Array:", arr)  #
        return arr
    
nums = [[5000,5000]]
queries =[5001]
new_sol = Solution()
ans = new_sol.maximumBeauty(nums,queries)
print(ans)

    
