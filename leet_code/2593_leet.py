# error not working : variable access error{smallest}

class Solution:
    def findScore(self, nums) -> int:
        
        smallest = float('inf')
        def conditioned_min(marked,nums):
            for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:
                    smallest = nums[i] if nums[i] not in marked else smallest

            return smallest

        def check_tie(smallest):
            smallest_index_num = min(book[smallest])
            return smallest_index_num
        
        def check_markings(marked,smallest_index_num,score):
            
            print(nums[smallest_index_num])

            # if smallest_index_num == 0:
            #     marked.append(nums[smallest_index_num]) if nums[smallest_index_num] not in marked else None
            #     marked.append(nums[smallest_index_num+1])   if nums[smallest_index_num+1] not in marked else None

            #     score = score + nums[smallest_index_num] if nums[smallest_index_num] != None else 0
            # elif smallest_index_num == len(nums):
            #     marked.append(nums[smallest_index_num]) if nums[smallest_index_num] not in marked else None
            #     marked.append(nums[smallest_index_num-1])   if nums[smallest_index_num-1] not in marked else None

            #     score = score + nums[smallest_index_num] if nums[smallest_index_num] != None else 0
            # else:
            #     marked.append(nums[smallest_index_num+1])   if nums[smallest_index_num+1] not in marked else None
            #     marked.append(nums[smallest_index_num]) if nums[smallest_index_num] not in marked else None
            #     marked.append(nums[smallest_index_num-1])   if nums[smallest_index_num-1] not in marked else None

            #     score = score + nums[smallest_index_num] if nums[smallest_index_num] != None else 0
            
            if smallest_index_num == 0:
                if nums[smallest_index_num] not in marked:
                    marked.append(nums[smallest_index_num])
                if nums[smallest_index_num + 1] not in marked:
                    marked.append(nums[smallest_index_num + 1])
                score += nums[smallest_index_num]
            elif smallest_index_num == len(nums) - 1:
                if nums[smallest_index_num] not in marked:
                    marked.append(nums[smallest_index_num])
                if nums[smallest_index_num - 1] not in marked:
                    marked.append(nums[smallest_index_num - 1])
                score += nums[smallest_index_num]
            else:
                if nums[smallest_index_num - 1] not in marked:
                    marked.append(nums[smallest_index_num - 1])
                if nums[smallest_index_num] not in marked:
                    marked.append(nums[smallest_index_num])
                if nums[smallest_index_num + 1] not in marked:
                    marked.append(nums[smallest_index_num + 1])
                score += nums[smallest_index_num]

            return score
            
        score,smallest,smallest_index_num = 0,0,None
        marked = []
        book = {}
        for i in range(len(nums)):
            if nums[i] not in book:
                book[nums[i]] = [i]
            else:
                book[nums[i]].append(i)

        while marked != nums:

            smallest = conditioned_min(marked,nums)
            smallest_index_num = check_tie(smallest)
            score = check_markings(marked,smallest_index_num,score)

        return score


nums = [2,1,3,4,5,2]
sol = Solution()
ans = sol.findScore(nums)
print(ans)