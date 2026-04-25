lista = [6,2,1,7,3,5,4] 
def seleccion_sort(lista): 
    n = len(lista) 
    for j in range(n - 1): 
        iMin = j 
        for i in range(j + 1, n): 
            if lista[i] < lista[iMin]: 
                iMin = i 
        if iMin != j: # intercambio 
            lista[j], lista[iMin] = lista[iMin], lista[j] 
            
seleccion_sort(lista)
print(lista)
