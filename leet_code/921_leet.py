s = ')))((('
# s = "((("

i = 0
j = len(s)-1
count = 0

a = list(s)

while i<=j: 
    if a[i] == '(' and a[j] == '(' :
        count = count + 1
        print(a[j])
        j -=1
    elif a[i] == ')' and a[j] == ')':
        count = count + 1
        j -=1
    elif a[i] == ')' and a[j] == '(':
        count = count + 1
        j -=1
    else:
        i +=1
        j -=1

print(count)
    