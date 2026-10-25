def bubble_sort(data, reverse):
    a = data.copy()
    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - 1 - i):
            if reverse == 1:
                if a[j] < a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            elif reverse == 0:
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
        if not swapped:
            break
    return a


# === ОСНОВНОЕ ЗАДАНИЕ 1 ===
def main_task_1(data):
    print("\n--- Основное задание 1 (Сортировка по убыванию) ---")
    print("Исходный массив:", data)
    
    
    result = bubble_sort(data, reverse=1)
    
    print("Выходные данные:", result)


# === ОСНОВНОЕ ЗАДАНИЕ 2 ===
def main_task_2(data):
    print("\n--- Основное задание 2 (Проверка упорядоченности по убыванию) ---")
    print("Исходный массив:", data)
    
    is_ordered = True
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]: 
            is_ordered = False
            break
            
    if is_ordered:
        print("Результат проверки: Массив УЖЕ упорядочен по убыванию.")
        result = data
    else:
        print("Результат проверки: Массив НЕ упорядочен по убыванию. Сортируем...")
        result = bubble_sort(data, reverse=1)
        
    print("Выходные данные:", result)


# === ОСНОВНОЕ ЗАДАНИЕ 3 ===
def main_task_3(data):
    print("\n--- Основное задание 3 (Сортировка только ЧЕТНЫХ элементов) ---")
    print("Исходный массив:", data)
    

    evens = [x for x in data if x % 2 == 0]
    

    sorted_evens = bubble_sort(evens, reverse=0)
    

    result = data.copy()
    even_idx = 0
    for i in range(len(result)):
        if result[i] % 2 == 0:
            result[i] = sorted_evens[even_idx]
            even_idx += 1
            
    print("Выходные данные:", result)



# ДОП ЗАДАНИЕ 1
def task_1(data):
    print("\n--- Дополнительное задание 1 ---")
    print("Исходный массив:", data)
    
    even_positions = []  
    odd_positions = []  
    
    for i in range(len(data)):
        if i % 2 == 0:
            even_positions.append(data[i])
        else:
            odd_positions.append(data[i])
            
    sorted_odd = bubble_sort(odd_positions, 0)
    sorted_even = bubble_sort(even_positions, 1)
    
    result = []
    even_idx, odd_idx = 0, 0
    for i in range(len(data)):
        if i % 2 == 0:
            result.append(sorted_even[even_idx])
            even_idx += 1
        else:
            result.append(sorted_odd[odd_idx])
            odd_idx += 1
            
    print("Выходные данные:", result)


# ДОП ЗАДАНИЕ 2
def task_2(data):
    print("\n--- Дополнительное задание 2 ---")
    print("Исходный массив:", data)
    
    result = []
    for item in data:
        if item not in result:
            result.append(item)
            
    print("Выходные данные:", result)


# ДОП ЗАДАНИЕ 3
def task_3(data_zeros_ones_twos):
    print("\n--- Дополнительное задание 3 ---")
    print("Исходный массив:", data_zeros_ones_twos)
    
    a = data_zeros_ones_twos.copy()
    low = 0
    mid = 0
    high = len(a) - 1
    
    while mid <= high:
        if a[mid] == 1:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 2:
            mid += 1
        elif a[mid] == 0:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
           
            
    print("Выходные данные:", a)


# ЗАПУСК ВСЕХ ЗАДАНИЙ 

data_main = [7, 3, 8, 4, 7, 9, 6, 3, 5, 8, 4, 2, 5, 8, 9]
data_task3 = [2, 0, 1, 2, 0, 1, 1, 0, 2, 1, 0, 2, 1, 1, 0]

data_already_sorted = [20, 15, 10, 8, 5, 3, 1]


main_task_1(data_main)
main_task_2(data_main)
main_task_2(data_already_sorted)
main_task_3(data_main)
task_1(data_main)
task_2(data_main)
task_3(data_task3)