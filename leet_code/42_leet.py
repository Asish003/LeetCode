height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
# height =[4,2,3]

left_max = 0
right_max = 0

left = []
right = []

max_water = 0

for i in range(len(height)):
    if i == 0:
        left.append(0)

    elif height[i-1]>left_max: 
        left.append(height[i-1])
        left_max = height[i-1]
    else:
        left.append(left_max)

for i in range(len(height)-1,-1,-1):
            
    if i == len(height)-1:
        right.append(0)

    elif height[i+1]>right_max: 
        right.insert(0,height[i+1])
        right_max = height[i+1]
    else:
        right.insert(0,right_max)

print(left)
print(right)

for i in range(len(left)):
    if min(left[i],right[i]) - height[i] > 0:
        max_water = max_water + min(left[i],right[i]) - height[i]
    else: 
        max_water = max_water + 0

print(max_water)

# --------My temporary solution---------#
# error is height =[4,2,3] couldn't calculate when height in ascending and already a bigger value is present earlier#

# i = 0
# j = 0
# prev = i
# water = 0
# store = 0

# while j < len(height):
    
#     if j == len(height)-1 and i != j and height[j] < height[i]:
#         prev = i 
#         store = 0
#         i += 1
#         j = i
    
#     else:
#         if height[j] < height[i]: 
#             store = store + height[i] - height[j]
#             print(store)
#             j+=1
#         elif height[j] >= height[i]: 
#             water = water + store
#             print("finally -->",water)
#             store = 0
#             i = j
#             j+=1
#         else: 
#             i += 1
#             j = i


# print(water)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# left_max = 0
# right_max = 0

# left = []
# right = []

# max_water = 0

# for i in range(len(height)):
#     if i == 0:
#         left.append(0)

#     elif height[i-1]>left_max: 
#         left.append(height[i-1])
#         left_max = height[i-1]
#     else:
#         left.append(left_max)

# for i in range(len(height)-1,-1,-1):
    
#     if i == len(height)-1:
#         right.append(0)

#     elif height[i+1]>right_max: 
#         right.insert(0,height[i+1])
#         right_max = height[i+1]
#     else:
#         right.insert(0,right_max)

# print(left)
# print(right)

# for i in range(len(left)):
#     if min(left[i],right[i]) - height[i] > 0:
#         max_water = max_water + min(left[i],right[i]) - height[i]
#     else: 
#          max_water = max_water + 0

# print(max_water)
        