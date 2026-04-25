#seleccion
Num = [2,8,5,1,3,9,4,6,7] 
def OrdenarSeleccion(list): 
    l = len(list) 
    for mano in range(l): 
        posMin = mano 
        print(f"Actualmento mano vale: {mano}") 
        for vista in range(mano + 1, l): 
            if list[vista] < list[posMin]: 
                posMin = vista 
        print(f"Actualmente vista vale: {vista}") 
        list[mano], list[posMin]=list[posMin], list[mano] 
     

OrdenarSeleccion(Num) 
print(f"Lista:{Num}")