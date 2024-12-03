s = "llkcegedae"
# s = "aba"
# s = "aa"
# s = "wwwzfvedwfvhsww"

arr = list(s)
print(arr)

req_arr = []
duplicates = []
temp = ""

# for i in range(len(arr)):
#     if len(temp) > 1 and temp not in req_arr:
#         req_arr.append(temp)
#         temp = ""
#     if len(temp)<1 and arr[i] not in req_arr:
#         req_arr.append(arr[i])
#     else:
#         temp += arr[i]
#         print(temp)
#         if i == len(arr)-1:
#             if temp not in req_arr:
#                 req_arr.append(temp)
#             else:
#                 req_arr[-1] = req_arr[-1] + temp 

# print(req_arr)
# print(s)
# print("".join(req_arr))
# print(len(req_arr))

for i in range(len(arr)):
    if arr[i] not in req_arr:
        req_arr.append(arr[i])
    else:
        duplicates.append(arr[i])

print(req_arr)
print(duplicates)

for i in range(len(duplicates)):
    if len(temp) > 1 and temp not in req_arr:
        print(temp)
        req_arr.append(temp)
        temp = ""
    if duplicates[i] in req_arr:
        print(duplicates[i])
        temp = temp + duplicates[i]
    if i == len(duplicates)-1:
        if len(temp) > 1 and temp not in req_arr:
            req_arr.append(temp)
        else:
            req_arr[-1] = req_arr[-1] + temp

print(req_arr)
print(len(req_arr))