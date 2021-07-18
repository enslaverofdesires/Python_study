#Calculator 
"""
a = int(input("Введите первое число:\n"))
operand = input("какое действие необходимо выполнить:\n")
if operand == "**":
	b = int(input("В какую степень возвести?:\n"))
	res	= (a ** b)
	print(f"Результат вычисления равен: {res}")
if operand == "^":
	b = int(input("степень корня?:\n"))
	res = (a ** (1./b))
	print(f"Результат вычисления равен: {res}")
else: 
	b = int(input("Введите второе число:\n"))
	if	operand == "+":
		res = (a + b)
	elif operand == "-":
		res = (a - b)
	elif operand == "*":
		res = (a * b)
	elif operand == "/":
		if b > a:
			res = 0
			print("Нацело не делится")
		else:
			if a % b == 0:
				print("Деление без остатка")
			else:
				res = a % b
				print(f"Делится с остатком. Остаток равен {res}")
			if b == 0:
				print("Делитель равен 0")
				res = "-"
			else:
				res = (a / b)
	else:
		print("Введена не корректная операция")
		res = "-"
print(f"Результат вычисления равен: {round(res)}")

#делится/не делится

x = int(input("Введите первое число:\n"))
y = int(input("Введите второе число:\n"))
if x % y == 0:
	print("Деление без остатка (Делится)")
else:
	res = x % y
	print(f"Нацело не делится. Остаток равен {res}")
"""

#пароль
"""
c = str(input("Пароль:\n"))
d = str(input("Подтверждение пароля:\n"))
if c == d:
	print("Пароль принят")
else:
	print("Пароль не принят")
"""

#дележ яблок
"""
n = int(input("Количество Школьников:\n"))
k = int(input("Количество Яблок:\n"))
res = k / n
print(f"В корзине находится {round(res)} яблок.\n")
if k % n == 1:
	print(f"Остаток: {k % n} яблоко")
elif k % n > 1:
	print(f"Остаток: {k % n} яблока")
elif k % n == 0:
	print(f"Остаток: {k % n} яблок")
"""

#гонка за спасения мира
"""
n = int(input("Скорость Зума: \n"))
k = int(input("Скорость Флеша: \n"))
if n > k:
	print("\nNO")
elif n < k:
	print("\nYES")
else:
	print("\nDON`T KNOW")
"""

#наименьшее из четырех чисел
"""
a = int(input("Введите первое число: \n"))
b = int(input("Введите второе число: \n"))
c = int(input("Введите третье число: \n"))
d = int(input("Введите четвертое число: \n"))
res = min(a, b, c, d)
print(f"Наименьшее число из четырех: {res}")
"""

#церемония взвешивания
"""
x = int(input("Введите вес спортсмена: \n"))
if x < 60:
	print("Весовая категория спортсмена: Легкий вес")
elif x < 64:
	print("Весовая категория спортсмена: Первый полусредний вес")	
elif x < 69:
	print("Весовая категория спортсмена: Полусредний вес")
else:
	print("Вес спортсмена больше допустимого при взвешивании")
"""

#ночной клуб
"""
x = str(input("Укажите пол (f или m): \n"))
while True:
	if x == "f" or x == "m":
		y = int(input("Укажите возраст: \n"))
		if x == "f" and y >= 18:
			print("WELCOME")
		elif x == "m" and y >= 21:
			print("WELCOME")
		else:
			print("ACESS DENIED")
		break
	else:	
		print("Неккоректно введен пол")
		break
"""					

#генератор чисел
"""
from random import randint
x = randint(100,999)
print(f"Случайно сгенирированное число: {x}")
num = int(x)
sum = 0
while (num !=0):
	sum = sum + num % 10
	num = num // 10
print("Сумма чисел равна: ", sum)	
num = int(x)
mult = 1
while (num !=0):
	mult = mult * (num % 10)
	num = num // 10
print("Произвдение чисел равно: ", mult)
"""

#рулетка
"""
a = "черный"
b = "красный"
c = "зеленый"
x = int(input("Введите число: "))
if x == 0:
	print(c)
if x > 36:
	print("ERROR")	
elif x >= 29 or x <= 36:
	if x % 2 == 0:
		print(b)
	else:
		print(a)	
elif x >= 19 or x <= 28:
	if x % 2 == 0:
		print(a)	
	else:
		print(b)
elif x >= 11 or x <= 18:
	if x % 2 == 0:
		print(b)
	else:
		print(a)		
elif x >= 1 or x <= 10:
	if x % 2 == 0:
		print(a)
	else:
		print(b)
"""	
	
#algorithm tasks

#1

"""
a = 15
b = 55
import random
list = [a, b]
random.shuffle(list)

print(list)
"""

#2

h, m = input("Введите время: ").split()
h = int(h)
m = int(m)
y = 60 - m
if h == 6:
	x = 6
elif h == 0:
	x = 10
if m == 00:
	y = 00
if 1 <= h <= 5:
	x = 12 - h 
elif 7 <= h <= 11:
	x = 10 - h
print(x, y)
	