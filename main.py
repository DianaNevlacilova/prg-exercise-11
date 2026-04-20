import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)
print(values)

def selection_sort(numbers):
    numbers = numbers[:]
    for safe_position in range(len(numbers)):
        min_idx = safe_position
        for traversed_position in range(safe_position +1, len(numbers)):
            if numbers[traversed_position] < numbers[min_idx]:
                min_idx = traversed_position

        numbers[safe_position], numbers[min_idx] = numbers[min_idx], numbers[safe_position]
    return numbers

numbers = [5, 1, 4, 2, 8]
print("Původní seznam:", numbers)
print("Sařazený seznam:", selection_sort(numbers))

