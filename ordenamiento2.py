#burbuja
def OrdenarBurbuja(lst): 
    n = len(lst) 
    for pasada in range(n-1): 
        for izqPar in range(0, n - pasada - 1): 
            derPar = izqPar + 1
            if lst[izqPar] > lst[derPar]: 
                lst[izqPar], lst[derPar] = lst[derPar], lst[izqPar] 

num = [3, 4, 6, 1, 2, 9] 
OrdenarBurbuja(num)
print(num)