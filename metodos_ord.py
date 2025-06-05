def ordenamiento_burbuja(lista):
    n = len(lista)
    
    for i in range(n - 1):  
        for j in range(n - i - 1): 
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

    return lista

def ordenamiento_seleccion(lista):
    n = len(lista)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        
        if min_index != i:
            temp = lista[i]
            lista[i] = lista[min_index]
            lista[min_index] = temp

    return lista

def ordenamiento_insercion(lista):
    n = len(lista)
    
    for i in range(1, n):
        key = lista[i]  
        j = i - 1
        
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = key

    return lista

def ordenamiento_quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        return ordenamiento_quick_sort(left) + middle + ordenamiento_quick_sort(right)
    
def ordenamiento_mezcla(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda_ordenada = ordenamiento_mezcla(izquierda)
    derecha_ordenada = ordenamiento_mezcla(derecha)

    return mezclar(izquierda_ordenada, derecha_ordenada)

def mezclar(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado
