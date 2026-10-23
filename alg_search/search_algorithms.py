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




