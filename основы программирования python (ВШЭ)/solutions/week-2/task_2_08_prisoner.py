'''
Узник замка Иф

За многие годы заточения узник замка Иф проделал в стене прямоугольное
отверстие размером D×E. Замок Иф сложен из кирпичей, размером A×B×C.

Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие
(очевидно, стороны кирпича должны быть параллельны сторонам отверстия).

Формат ввода: Программа получает на вход числа A, B, C, D, E.
Формат вывода: Программа должна вывести слово YES или NO.
'''

a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

result1 = (a <= d and (b <= e or c <= e)) or (a <= e and (b <= d or c <= d))
result2 = (b <= d and (a <= e or c <= e)) or (b <= e and (a <= d or c <= d))
result3 = (c <= d and (a <= e or b <= e)) or (c <= e and (a <= d or b <= d))

result = result1 + result2 + result3

print('YES' if result else 'NO')
