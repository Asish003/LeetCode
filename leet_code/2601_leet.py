# import time 

# class Solution:
#     def primeSubOperation(self, nums) -> bool: 

#         def nearest_prime(num,prev_diff,val):
#             if num<2:
#                 return False
#             else:
#                 for i in range(num//2+1,2,-1):
#                     if num%i == 0:
#                         return nearest_prime(num-1,prev_diff) if num>3 else False
#                     return num if val - num > prev_diff else nearest_prime(num-1,prev_diff,val)
                    
        
#         def arr_order(arr):
#             print(arr)
#             for i in range(len(arr)-1):
#                 if arr[i+1] <= arr[i]:
#                     return False    
#             return True
        

#         sorted_array = sorted(nums)
#         if sorted_array == nums and arr_order(nums) == True:
#             return True

#         arr = nums
#         prev_diff = 0
#         np = 0
#         for i in range(len(nums)):
#             # prev_diff = np
#             val = nums[i]
#             print(prev_diff)
#             np = nearest_prime(nums[i]-1,prev_diff,val)
#             if arr_order(arr) == True:
#                 return True
#             elif np == False:
#                 return False
#             elif np>i:
#                 prev_diff = nums[i] - np
#                 arr[i] = nums[i] - np
#         return False


# start_time = time.time() 

# nums = [15,20,17,7,16]
# # nums = [4,9,6,10]
# new_sol = Solution()
# ans = new_sol.primeSubOperation(nums)
# print(ans)
# end_time = time.time()

# # Calculate the execution time
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")

import time

class Solution:
    def primeSubOperation(self, nums) -> bool:

        def nearest_prime(num, prev_diff, val):
            if num < 2:
                return False
            for i in range(num // 2 + 1, 2, -1):
                if num % i == 0:
                    return nearest_prime(num - 1, prev_diff, val) if num > 3 else False
            return num if val - num > prev_diff else nearest_prime(num - 1, prev_diff, val)

        def arr_order(arr):
            print(arr)
            for i in range(len(arr) - 1):
                if arr[i + 1] <= arr[i]:
                    return False
            return True

        sorted_array = sorted(nums)
        if sorted_array == nums and arr_order(nums):
            return True

        arr = nums[:]
        prev_diff = 0
        np = 0
        for i in range(len(nums)):
            val = nums[i]
            np = nearest_prime(nums[i] - 1, prev_diff, val)
            
            if np is False: 
                return False
            elif np is not None and np > i:  
                prev_diff = nums[i] - np
                arr[i] = nums[i] - np
                
                if arr_order(arr):
                    return True
        return False


start_time = time.time()

# Wrong Answer
# 643 / 654 testcases passed

# Editorial
# Input
# nums = [5,13,4,13]

# Use Testcase
# Output
# true
# Expected
# false
# nums = [15, 20, 17, 7, 16]
# nums = [4,9,6,10]

nums = [5,13,4,13]
new_sol = Solution()
ans = new_sol.primeSubOperation(nums)
print(ans)

end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time
execution_time = execution_time * 1000
print(f"Execution time: {execution_time} ms")

