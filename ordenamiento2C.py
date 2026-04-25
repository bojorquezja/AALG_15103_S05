def buble_sort(lista): 
    # recorre la lista n veces 
    for i in range(1,len(lista)-1): 
        # va por cada elemento 
        for j in range(0,len(lista)): # intercambio 
            if (lista[j] > lista[j+1]): 
                lista[j], lista[j+1] = lista[j+1] , lista[j] 