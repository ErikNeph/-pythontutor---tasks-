# Условие.
# Определите сумму всех элементов последовательности, завершающейся числом 0.
# В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.

ele = int(input())
sum = 0
while ele != 0:
	sum += ele
	ele = int(input())
print(sum)
