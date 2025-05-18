def find_min_max(arr):
    # Базовий випадок: якщо масив порожній, повертаємо None
    if not arr:
        return None, None

    # Базовий випадок: якщо масив містить один елемент, повертаємо його як мінімум і максимум
    if len(arr) == 1:
        return arr[0], arr[0]

    # Розділяємо масив на дві половини
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Повертаємо мінімум і максимум з обох половин
    return min(left_min, right_min), max(left_max, right_max)


# Приклад використання
if __name__ == "__main__":
    arr = [3, 5, 1, 8, 2, 7]
    min_val, max_val = find_min_max(arr)
    print(f"Мінімальне значення: {min_val}, Максимальне значення: {max_val}")
