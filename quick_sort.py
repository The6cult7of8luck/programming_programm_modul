from random import randint
from timeit import repeat


def bubble_sort(data):
    a = data.copy()
    comparisons = 0

    for i in range(len(a) - 1):
        swapped = False

        for j in range(len(a) - 1 - i):
            comparisons += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if not swapped:
            break

    return a, comparisons


def insertion_sort(data):
    a = data.copy()
    comparisons = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break

        a[j + 1] = key

    return a, comparisons


def merge_sort(data):
    comparisons = 0

    def sort(a):
        nonlocal comparisons

        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = sort(a[:mid])
        right = sort(a[mid:])

        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    return sort(data.copy()), comparisons







# быстрая сортировка тут!!!
def quick_sort(data):
    comparisons = 0

    def sort(arr):
        nonlocal comparisons
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = []
        middle = []
        right = []

        for x in arr:
            comparisons += 1  
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                middle.append(x)

        return sort(left) + middle + sort(right)

    return sort(data.copy()), comparisons










numbers = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(numbers)) # [11, 12, 22, 25, 34, 64, 90]

def measure(func, data):
    times = repeat(lambda: func(data), repeat=5, number=1)
    return min(times)


algorithms = {
    "Пузырьковая": bubble_sort,
    "Вставками": insertion_sort,
    "Слиянием": merge_sort,
    "Быстрая": quick_sort,
}

sizes = [100, 500, 1000, 5000]

for n in sizes:
    random_data = [randint(0, 100000) for _ in range(n)]

    print(f"\nРазмер массива: {n}")

    for name, func in algorithms.items():
        _, comparisons = func(random_data)
        t = measure(func, random_data)

        print(
            f"{name:12} | "
            f"сравнений: {comparisons:8} | "
            f"время: {t:.6f} с"
        )