def fn(string, k, i):
    if i == k:
        return string
    else:
        next_char = chr(ord(string[-1]) + 1)
        return fn(string + next_char, k, i + 1)

string = "a"
k = 5
i = 1

ans = fn(string, k, i)
print(ans)
