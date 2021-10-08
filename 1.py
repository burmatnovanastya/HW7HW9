def check(a, b, c):
	if a < b and b < c:
		print('a < b < c')
	elif a > b and b > c:
		print('a > b > c')
	elif a == b or b == c:
		print('Ни одно из двух неравенств не выполняется')
	else:
		print('Ни одно из двух неравенств не выполняется')

try:
	a = int(input('Введите A: '))
	b = int(input('Введите B: '))
	c = int(input('Введите C: '))
	check(a, b, c)
except ValueError:
	print('Ошибка ввода данных')