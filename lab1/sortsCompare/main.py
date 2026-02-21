import numpy as np
import random
from plot_data import plot_data


def genArr(size, genType="random"):
    """
    Функція генерації масивів для подальшого сортування.
    Параметри:
    n (int) - кількість елементів масиву
    gen_type (string) - тип згенерованих даних:
    "best" - відсортований масив (мінімальний час для сортування)
    "worst" - найгірший варіант для сортування
    "random" - послідовність елементів генерується випадкова
    (значення за замовчуванням)
    Повертає:
    Масив (list) довжиною n з елементами від 1 до n
    """
    if genType == "best":
        a = [i for i in range(1, size)]
    elif genType == "worst":
        a = [i for i in reversed(range(1, size))]
    else:
        a = [i for i in range(1, size)]
        random.shuffle(a)

    return a


def bubble_sort(seq):
    """
    Алгоритм сортування бульбашкою
    Параметри:
    seq - послідовність для сортування
    По закінченню роботи масив seq містить відсортовану послідовність
    На вихід функція повертає кількість порівнянь (op_count) під час роботи
    алгоритму
    ЗАВДАННЯ:
    Вашим завданням є написання тіла функції, яка реалізує алгоритм
    сортування методом бульбашкою.
    При чому під час роботи алгоритму повинні підраховуватись порівняння
    елементів, які виконує даний метод.
    """
    op_count = 0
    # Тут повинен бути ваш код

    # Для перевірки можна вивести відсортований масив
    # print seq
    return op_count


def bubble_impr_sort(seq):
    """
    Покращений алгоритм сортування бульбашкою
    """
    op_count = 0
    # Тут повинен бути ваш код

    # Для перевірки можна вивести відсортований масив
    # print seq
    return op_count


def ВАШ_АЛГОРИТМ(seq):
    """
    ВАШ АЛГОРИТМ
    Параметри:
    seq - послідовність для сортування
    По закінченню роботи масив seq містить відсортовану послідовність
    На вихід функція повертає кількість порівнянь (op_count) під час роботи
    алгоритму
    ЗАВДАННЯ:
    Вашим завданням є написання тіла функції, яка реалізує алгоритм
    Внутрішнього сортування за наведеним варіантом.
    При чому під час роботи алгоритму повинні підраховуватись порівняння
    елементів, які виконує даний метод.
    """
    op_count = 0
    # Тут повинен бути ваш код

    # Для перевірки можна вивести відсортований масив
    # print seq
    return op_count


"""
ТЕСТУВАННЯ АЛГОРИТМІВ:
тестування проводиться на наборах розімром 10, 100, 1000, 10000 (масив sizes)
але для початкової перевірки роботи рекомендується використовувати тільки
перші дві-три величини
"""

sizes = [10, 100, 1000]
types = ["random", "best", "worst"]

data_plot = {
    'random': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}},
    'best': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}},
    'worst': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}}
}

for n in sizes:
    print ("\nDATA SIZE: ", n)

    for gen_type in types:
        print ("\n\tDATA TYPE:", gen_type)

        data = genArr(n, gen_type)

        data_bubble = np.copy(data)
        bubble_op_count = bubble_sort(data_bubble)
        print ("\tBubble sort operation count:", int(bubble_op_count))
        data_plot[gen_type]['bubble'][n] = bubble_op_count

        # Для тестування покращеного методу бульбашки
        data_bubble_impr = np.copy(data)
        bubble_impr_op_count = bubble_impr_sort(data_bubble_impr)
        print ("\tImproved bubble sort operation count:", int(bubble_impr_op_count))
        data_plot[gen_type]['bubble_impr'][n] = bubble_impr_op_count

        data_insertion = np.copy(data)
        insertion_op_count = insertion_sort(data_insertion)
        print ("\tInsertion sort operation count:", int(insertion_op_count))
        data_plot[gen_type]['insertion'][n] = insertion_op_count
