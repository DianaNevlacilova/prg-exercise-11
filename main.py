import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)
print(values)

import matplotlib.pyplot as plt

def selection_sort(numbers):
    numbers = numbers[:]
    for safe_position in range(len(numbers)):
        min = safe_position
        for traversed_position in range(safe_position +1, len(numbers)):
            if numbers[traversed_position] < numbers[min]:
                min = traversed_position

            index_highlight1 = safe_position
            index_highlight2 = traversed_position
            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Blubble Sort")
            plt.pause(0.1)

        numbers[safe_position], numbers[min] = numbers[min], numbers[safe_position]
    plt.ioff()
    plt.show()
    return numbers

numbers = [5, 1, 4, 2, 8]
print("Původní seznam:", numbers)
print("Sařazený seznam:", selection_sort(numbers))


def bubble_sort(numbers):
    numbers = numbers[:]
    for serazeno_do_konce in range(len(numbers)):
        has_changed = False
        print(serazeno_do_konce)
        for comparison in range(len(numbers) - 1 - serazeno_do_konce):
            if numbers[comparison] > numbers[comparison + 1]:
                has_changed = True
                numbers[comparison], numbers[comparison + 1] = numbers[comparison + 1], numbers[comparison]
        if not has_changed:
            break
    return numbers
