'''
Сортировка

Отсортируйте данный массив, используя встроенную сортировку.

Формат ввода
Первая строка входных данных содержит количество элементов в массиве N,
N ≤ 10⁵. Далее идет N целых чисел, не превосходящих по абсолютной величине 10⁹

Формат вывода
Выведите эти числа в порядке неубывания.
'''

_ = input()
num_list = list(map(int, input().split()))
print(*sorted(num_list))
