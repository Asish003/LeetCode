n = 2
x = 7

i = 1
j = 1
current = 0
arr = []

while j < 10:  
    if i & j == x:  
        print(f"Found match: i={i}, j={j}")
        if len(arr) < n:
            arr.append(j)
            print(f"Array after append: {arr}")
    
    if len(arr) == n:
        t = arr[-1]
        print(f"Checking t={t} against current={current}")
        if current < t:
            print(f"Final result: {current}")
            break
        else:
            current = t
            arr = []
            
    i += 1
    if i > 10:  
        i = 1
        j += 1