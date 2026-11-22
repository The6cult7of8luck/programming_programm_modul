import time as t
import random
import sys

# ЗАДАНИЕ 1
def measure_time(func, *args, repeats=5):
    times = []
    while repeats > 0:
        repeats -= 1
        t0 = t.perf_counter()
        func(*args)
        times.append(t.perf_counter() - t0)
    return sum(times) / len(times)

def run_experiment(func, sizes, setup=None):
    results = []
    for n in sizes:
        if setup:
            args = setup(n)
        else:
            args = (n,)
        elapsed = measure_time(func, *args, repeats=10)
        results.append((n, elapsed))
    return results


# ЗАДАНИЕ 2
def sum_recursive(arr):
    if not arr:
        return 0
    return arr[0] + sum_recursive(arr[1:])


# ЗАДАНИЕ 3
def binary_search(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binary_search(arr, target, mid + 1, hi)
    else:
        return binary_search(arr, target, lo, mid - 1)


# ЗАДАНИЕ 4
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ЗАДАНИЕ 5
def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# ЗАДАНИЕ 6
moves = 0
def hanoi(n, src='A', dst='C', tmp='B'):
    global moves
    if n == 0:
        return
    hanoi(n - 1, src, tmp, dst)
    moves += 1
    hanoi(n - 1, tmp, dst, src)


# ЗАДАНИЕ 7
def depth(n):
    if n == 0:
        return 0
    return 1 + depth(n - 1)





print("=== ЗАДАНИЕ 7: Переполнение стека ===")
default_limit = sys.getrecursionlimit()
print(f"Системный лимит рекурсии: {default_limit}")
n_test = 1
while True:
    try:
        depth(n_test)
        n_test += 1
    except RecursionError:
        print(f"Переполнение произошло на n = {n_test} (макс. рабочее: {n_test - 1})\n")
        break

# Поднимаем лимит рекурсии
sys.setrecursionlimit(10000)

# Генераторы данных 
setup_list = lambda n: ([random.randint(1, 100) for _ in range(n)],)
setup_binary = lambda n: (sorted(random.sample(range(n * 10), n)), -1)  # -1 — худший случай


print("=== ЗАДАНИЕ 2: sum_recursive O(n) ===")
for n, time_val in run_experiment(sum_recursive, [100, 300, 500, 800], setup=setup_list):
    print(f"n = {n:<6} | время = {time_val:.6f} сек")


print("\n=== ЗАДАНИЕ 3: binary_search O(log n) ===")
for n, time_val in run_experiment(binary_search, [10**3, 10**4, 10**5, 10**6], setup=setup_binary):
    print(f"n = {n:<8} | время = {time_val:.8f} сек")


print("\n=== ЗАДАНИЕ 4а: fib_naive O(phi^n) ===")
fib_naive_res = run_experiment(fib_naive, [10, 15, 20, 25, 30])
for i, (n, time_val) in enumerate(fib_naive_res):
    ratio = time_val / fib_naive_res[i - 1][1] if i > 0 else 0
    print(f"n = {n:<4} | время = {time_val:.6f} сек | T(n)/T(n-5) = {ratio:.2f}")


print("\n=== ЗАДАНИЕ 4б: fib_memo O(n) ===")
for n, time_val in run_experiment(fib_memo, [100, 500, 1000, 5000]):
    print(f"n = {n:<5} | время = {time_val:.6f} сек")


print("\n=== ЗАДАНИЕ 5: merge_sort O(n log n) ===")
ms_res = run_experiment(merge_sort, [1000, 2000, 4000, 8000, 16000], setup=setup_list)
for i, (n, time_val) in enumerate(ms_res):
    ratio = time_val / ms_res[i - 1][1] if i > 0 else 0
    print(f"n = {n:<6} | время = {time_val:.6f} сек | рост = {ratio:.2f}x")

print("\nСравнение сортировок на n = 1000:")
test_arr = [random.randint(0, 10000) for _ in range(1000)]
print(f"sorted() встроенная : {measure_time(sorted, test_arr, repeats=10):.6f} сек")
print(f"merge_sort()        : {measure_time(merge_sort, test_arr, repeats=10):.6f} сек")



print("\n=== ЗАДАНИЕ 6: Ханойские башни O(2^n) ===")
for n in range(5, 21):
    moves = 0

    t_val = measure_time(hanoi, n, repeats=10)
    actual_moves = moves // 10
    expected = 2**n - 1
    print(f"n = {n:<3} | moves = {actual_moves:<8} (2^n-1 = {expected:<8}) | время = {t_val:.6f} сек")
