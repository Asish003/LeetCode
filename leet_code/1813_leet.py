# sentence1 ="CwFfRo regR"
# sentence2 ="CwFfRo H regR"

sentence1 = "My name is Haley"
sentence2 = "My Haley"


sen1 = list(sentence1.split())
sen2 = list(sentence2.split())

print(sen1)
print(sen2)

count = 0
count2 = 0
i = 0
j =0

if len(sen2)>len(sen1): 
    print("in 1")

    while j < len(sen2) and i < len(sen1):
        if sen1[i] == sen2[j]: 
            i += 1
            j += 1
            count = count + 1
        else:
            # if count2>1: 
            #     print(False)
            j += 1  
            count2 = count2 + 1

    if count == len(sen1): 
        print(True)
    else: 
        print(False)

else: 
    print("in 2")
    
    while j < len(sen2) and i < len(sen1):
        if sen1[i] == sen2[j]: 
            i += 1
            j += 1
            count = count + 1
        else:
            # if count2>1: 
            #     print(False)  
            i += 1 
            count2 = count2 + 1
            

    if count == len(sen2): 
        print(True )
    else: 
        print(False)