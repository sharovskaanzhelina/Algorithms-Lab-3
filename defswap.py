def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return 3 

def sink(arr, i, n):
    comps = 0
    assigs = 0
    
    k = i
    assigs += 1
    
    print(f"Починаємо занурювати елемент: {arr[k]} з індексу {k}")
    
    while True:
        j = 2 * k + 1 
        assigs += 1
        
        comps += 1 
        if j >= n:
            print(f"Елемент {arr[k]} на індексі {k} досяг кінця купи. Завершуємо.\n")
            break
            
        print(f" Обираємо лівий дочірній елемент: {arr[j]} на індексі {j}")
        
        comps += 1 
        if j + 1 < n:
            comps += 1 
            if arr[j + 1] > arr[j]:
                j += 1
                assigs += 1
                
        comps += 1 
        if arr[k] >= arr[j]:
            print(f" {arr[k]} (батько) >= {arr[j]} (найбільший дочірній). Елемент на своєму місці.\n")
            break
            
        print(f" Міняємо місцями {arr[k]} (батько) та {arr[j]} (дочірній)")
        assigs += swap(arr, k, j)
        k = j
        assigs += 1
        
        print(f" Масив після обміну: {arr}")
        
    return comps, assigs

def heapsort(arr):
    n = len(arr)
    total_comps = 0
    total_assigs = 0
    
    print(f"Початковий масив: {arr}\n")
    
    print("Фаза 1: Побудова максимальної купи")
    for i in range(n // 2 - 1, -1, -1):
        c, a = sink(arr, i, n)
        total_comps += c
        total_assigs += a
        
    print(f"Масив після побудови купи: {arr}\n")
    
    print("Фаза 2: Сортування")
    for i in range(n - 1, 0, -1):
        print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        total_assigs += swap(arr, 0, i)
        print(f"Розмір купи зменшився до {i}. Відновлюємо властивості купи.")
        
        c, a = sink(arr, 0, i)
        total_comps += c
        total_assigs += a
        
        print(f"Масив на поточному кроці: {arr}\n")
        
    return arr, total_comps, total_assigs

my_list = [80, 27, 37, 36, 91, 53, 86, 66, 98]

sorted_list, comps, assigs = heapsort(my_list)

print("Фінальні результати")
print("Відсортований масив:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigs}")
