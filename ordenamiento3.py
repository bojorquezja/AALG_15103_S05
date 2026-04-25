#insercion
def Ordenarinsercion(lst): 
    n = len(lst) 
    for pasada in range(1, n): 
        nuePos = pasada
        while nuePos > 0 and lst[nuePos-1] > lst[nuePos]:
            lst[nuePos-1], lst[nuePos] = lst[nuePos], lst[nuePos-1]
            nuePos -= 1 

num = [3, 4, 6, 1, 2, 9] 
Ordenarinsercion(num)
print(num)