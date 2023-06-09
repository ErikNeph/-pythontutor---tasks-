# Пример обработки двумерного массива:

# плохой алгоритм
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
	for j in range(n):
		if i < j:
			a[i][j] = 0
		elif i > j:
			a[i][j] = 2
		else:
			a[i][j] = 1
for row in a:
	print(' '.join([str(elem) for elem in row]))


# Чуть по лучше
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
	for j in range(0, i):
		a[i][j] = 2
	a[i][j] = 1
	for j in range(i + 1, n):
		a[i][j] = 0
for row in a:
	print(' '.join([str(elem) for elem in row] ))
	
	
# еще лучше
n = 4
a = [0]	* n
for i in range(n):
	a[i] = [2] * i + [1] + [0] * (n - i - 1)
for row in a:
	print(' '.join([str(elem) for elem in row]))
	
	
# Лучшее решение
n = 4
a = [0] * n
a = [[2] * i + [1] + [0] * [n - i - 1] for i in range(n)]
for row in a:
	print(' '.join([str(elem) for elem in row]))			
