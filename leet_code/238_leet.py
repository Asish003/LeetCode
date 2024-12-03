# nums = [1,2,3,4]
# nums =[0,0]
nums =[-1,1,0,-3,3]
# prod = 1
# final_prod = []

# for i in range(len(nums)):
#     for j in range(len(nums)): 
#         # print(nums[i])
#         # print(nums[j])
#         if i == j: 
#             pass
#         else:
#             prod = prod * nums[j]
#             print(prod)
#     final_prod.append(prod)
#     prod = 1

# print(final_prod)


prod = 1
arr = [] 
        
for i in range(len(nums)):
    if nums[i] == 0:
        pass
    else:
        prod = prod * nums[i]

for i in range(len(nums)):
    if i == 0: 
        arr.append(0)
    else: 
        arr.append(prod//nums[i])

print(arr)