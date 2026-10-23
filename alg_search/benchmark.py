import random
import time
import math

def linear_search(arr, target):
    """Возвращает индекс target в arr или -1. O(n)."""
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


def binary_search(arr, target):
    """Итеративный бинарный поиск. arr должен быть отсортирован. O(log n)."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """Рекурсивный бинарный поиск. O(log n)."""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    return binary_search_recursive(arr, target, left, mid - 1)


def interpolation_search(arr, target):
    """Интерполяционный поиск. O(log log n) в среднем, O(n) в худшем."""
    low, high = 0, len(arr) - 1
    while (low <= high and arr[low] <= target <= arr[high]):
        if arr[high] == arr[low]:
            return low if arr[low] == target else -1
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1


def measure(func, *args, repeat=5):
    """Минимальное время выполнения за repeat прогонов."""
    best = float("inf")
    for _ in range(repeat):
        t0 = time.perf_counter()
        func(*args)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return best


# === Интеграция Задания 4: Аппроксимация эмпирической сложности ===
def estimate_growth(sizes, times):
    """Оценка показателя роста по последним точкам: p = log(t2/t1)/log(n2/n1)."""
    n1, n2 = sizes[-2], sizes[-1]
    t1, t2 = times[-2], times[-1]
    if t1 == 0 or n1 == 0 or t2 == 0:
        return float('nan')
    return math.log(t2 / t1) / math.log(n2 / n1)


# === Интеграция Задания 5: Три случая для каждого алгоритма ===
def run_benchmark():
    sizes = [100, 1_000, 10_000, 100_000, 1_000_000]
    cases = ["Лучший", "Средний", "Худший"]
    
    # Сложная структура для хранения результатов под каждый случай
    # Инициализируем пустые списки для каждого размера n
    results = {
        case: {
            "linear": [],
            "binary_iter": [],
            "binary_rec": [],
            "interp": [],
            "dict": [],
        } for case in cases
    }

    print("Запуск комплексного бенчмарка...\n")

    for case in cases:
        print(f"--- Тестирование: {case} случай ---")
        for n in sizes:
            # Генерируем упорядоченный базовый массив
            data = sorted(random.sample(range(n * 10), n))
            d = {x: i for i, x in enumerate(data)}

            # Логика формирования target в соответствии с Заданием 5
            if case == "Лучший":
                t_linear_target = data[0]         # Первый для линейного
                t_binary_target = data[len(data) // 2]  # Центральный для бинарного
                t_dict_target = data[0]
            elif case == "Средний":
                # Берем случайный существующий элемент
                t_linear_target = t_binary_target = t_dict_target = random.choice(data)
            else:  # Худший случай
                # Последний элемент или значение, которого нет в массиве
                t_linear_target = t_binary_target = t_dict_target = data[-1]

            # Замеряем время индивидуально с учетом специфики целей лучшего случая
            t_lin = measure(linear_search, data, t_linear_target)
            t_bin_iter = measure(binary_search, data, t_binary_target)
            t_bin_rec = measure(binary_search_recursive, data, t_binary_target)
            t_interp = measure(interpolation_search, data, t_binary_target)
            t_dict = measure(lambda arr, t: d.get(t, -1), data, t_dict_target)

            # Сохраняем результаты в соответствующую категорию
            results[case]["linear"].append(t_lin)
            results[case]["binary_iter"].append(t_bin_iter)
            results[case]["binary_rec"].append(t_bin_rec)
            results[case]["interp"].append(t_interp)
            results[case]["dict"].append(t_dict)

            # Вывод текущей строки
            res_c = results[case]
            formatted_row = (
                f"linear={res_c['linear'][-1]*1000:7.4f}ms, "
                f"bin_iter={res_c['binary_iter'][-1]*1000:7.4f}ms, "
                f"bin_rec={res_c['binary_rec'][-1]*1000:7.4f}ms, "
                f"interp={res_c['interp'][-1]*1000:7.4f}ms, "
                f"dict={res_c['dict'][-1]*1000:7.4f}ms"
            )
            print(f"n = {n:>9}: {formatted_row}")
        print()

    # === Вывод результатов Задания 4 (Показатель степени p) ===
    print("=== Результаты аппроксимации эмпирической сложности (значения p) ===")
    print(f"{'Алгоритм':<15} | {'Лучший p':<10} | {'Средний p':<10} | {'Худший p':<10}")
    print("-" * 55)
    
    algos = ["linear", "binary_iter", "binary_rec", "interp", "dict"]
    for algo in algos:
        p_best = estimate_growth(sizes, results["Лучший"][algo])
        p_avg = estimate_growth(sizes, results["Средний"][algo])
        p_worst = estimate_growth(sizes, results["Худший"][algo])
        
        print(f"{algo:<15} | {p_best:<10.4f} | {p_avg:<10.4f} | {p_worst:<10.4f}")

    return sizes, results

# Запускаем бенчмарк один раз
sizes, results = run_benchmark()