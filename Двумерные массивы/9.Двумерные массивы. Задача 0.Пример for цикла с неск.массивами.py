# Однажды мы уже пытались объяснить, что переменная цикла for в Питоне может перебирать не только диапазон,
# создаваемый с помощью функции range(), но и вообще перебирать любые элементы любой
# последовательности. Последовательностями в Питоне являются списки, строки, а также некоторые другие
# объекты, с которыми мы пока не встречались. Продемонстрируем, как выводить двумерный массив, используя это
# удобное свойство цикла for:


a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
	for elem in row:
		print(elem, end = ' ')
	print()


A = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
	for q in range(len(a[i])):
		s += a[i][q]
print(s)
