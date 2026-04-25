Num = [2,8,5,1,3,9,4,6,7] 
for i in range(1, len(Num)): 
    for j in range(0, len(Num)-1): 
        if Num[j] > Num[i]: 
            Num[j], Num[i] = Num[i], Num[j] 

print(Num)