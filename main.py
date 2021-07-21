# # 1st week 1 st Task
# """
# print("hello i am programmer")
# name = "Yevgeniy"
# print("My name is "+ name)
# a = "103"
# a = int(a)
# b = 301
# not_found = (a + b)
# not_found = str(not_found)
# print(not_found)
# print("not_found " + not_found)
# """
# # 1st week 2nd Task

# i = "2.1"
# h = "1.04"
# pi = (float(i) + float(h))
# pi = str(pi)
# print("pi = " + pi)
# a = "Hello"
# b = 123
# c = 0
# d = -1
# f = "-1"
# """
# print(bool(a))
# print(bool(b))
# print(bool(c))
# print(bool(d))
# print(bool(f))
# """
# a = bool(a)
# b = bool(b)
# c = bool(c)
# d = bool(d)
# f = bool(f)
# #print(a,b,c,d,f)
# print(a)
# print(b)
# print(c)
# print(d)
# print(f)
# print("I","like","Python", sep="***", end="\n")
# # параметр sep (separator) используется как разделитель, что-то вроде табуляции в MS Office только между задаными частями кода/текста и тд
# # параметр end после всего что написано в гугл, честно говоря ничего не понял, но после того как поюзал на практике получилось что данный параметр объединяет строки в одну, то есть если я пропишу параметр просто с пробелом, то он через пробел объединяет строки
# """
# s = 0 
# k = 30 
# d = k - 5 
# k = 2 * d 
# s = k - 100
# s = -50
# """
# """
# k = int(input("Стоимость Монитора :"))
# l = int(input("Стоимость Системного блока :"))
# m = int(input("Стоимость Клавиатуры :"))
# n = int(input("Стоимость Мыши :"))
# t = 3 * (k + l + m + n)
# print("Стоимость покупки 3 ПК: " + str(t))
# x = int(input("Введите число: "))
# print("Следующее за числом " + str(x) + " число: " + str(x + 1))
# print("Для числа " + str(x) + " предыдущее число: " + str(x - 1))




# #Calculator 

# a = int(input("Введите первое число:\n"))
# operand = input("какое действие необходимо выполнить:\n")
# if operand == "^":
# 	b = int(input("степень корня?:\n"))
# 	res = (a ** (1./b))
# elif operand == "**":
# 	b = int(input("В какую степень возвести?:\n"))
# 	res	= (a ** b)	
# else: 
# 	b = int(input("Введите второе число:\n"))
# 	if	operand == "+":
# 		res = (a + b)
# 	elif operand == "-":
# 		res = (a - b)
# 	elif operand == "*":
# 		res = (a * b)
# 	elif operand == "/":	
# 		if b > a:
# 			res = 0
# 			print("Нацело не делится")
# 		elif b == 0:
# 			try:
# 				res = a / b
# 			except ZeroDivisionError:
# 			    res = 0
# 			print("Делитель равен 0")    
# 		elif a % b == 0:
# 			res = a / b
# 			print("Деление без остатка")
# 		else:
# 			res = a % b
# 			print(f"Делится с остатком. Остаток равен {res}")
# 	else:
# 		print("Введена не корректная операция")
# 		res = "-"
# print(f"Результат вычисления равен: {round(res)}")

# #делится/не делится
# x = int(input("Введите первое число:\n"))
# y = int(input("Введите второе число:\n"))
# if x % y == 0:
# 	print("Деление без остатка (Делится)")
# else:
# 	res = x % y
# 	print(f"Нацело не делится. Остаток равен {res}")
"""

# #пароль
# """
# c = str(input("Пароль:\n"))
# d = str(input("Подтверждение пароля:\n"))
# if c == d:
# 	print("Пароль принят")
# else:
# 	print("Пароль не принят")

# """

# #дележ яблок
# """
# n = int(input("Количество Школьников:\n"))
# k = int(input("Количество Яблок:\n"))
# res = k / n
# print(f"В корзине находится {round(res)} яблок.\n")
# if k % n == 1:
# 	print(f"Остаток: {k % n} яблоко")
# elif k % n > 1:
# 	print(f"Остаток: {k % n} яблока")
# elif k % n == 0:
# 	print(f"Остаток: {k % n} яблок")
# """

# #гонка за спасения мира
# """
# n = int(input("Скорость Зума: \n"))
# k = int(input("Скорость Флеша: \n"))
# if n > k:
# 	print("\nNO")
# elif n < k:
# 	print("\nYES")
# else:
# 	print("\nDON`T KNOW")
# # """

# #наименьшее из четырех чисел
# """
# a = int(input("Введите первое число: \n"))
# b = int(input("Введите второе число: \n"))
# c = int(input("Введите третье число: \n"))
# d = int(input("Введите четвертое число: \n"))
# res = min(a, b, c, d)
# print(f"Наименьшее число из четырех: {res}")
# """

# #церемония взвешивания
# """
# x = int(input("Введите вес спортсмена: \n"))
# if x < 60:
# 	print("Весовая категория спортсмена: Легкий вес")
# elif x < 64:
# 	print("Весовая категория спортсмена: Первый полусредний вес")	
# elif x < 69:
# 	print("Весовая категория спортсмена: Полусредний вес")
# else:
# 	print("Вес спортсмена больше допустимого при взвешивании")
# """

# #ночной клуб
# """
# x = str(input("Укажите пол (f или m): \n"))
# while True:
# 	if x == "f" or x == "m":
# 		y = int(input("Укажите возраст: \n"))
# 		if x == "f" and y >= 18:
# 			print("WELCOME")
# 		elif x == "m" and y >= 21:
# 			print("WELCOME")
# 		else:
# 			print("ACESS DENIED")
# 		break
# 	else:	
# 		print("Неккоректно введен пол")
# 		break
# """					

# #генератор чисел
# """
# from random import randint
# x = randint(100,999)
# print(f"Случайно сгенирированное число: {x}")
# num = int(x)
# sum = 0
# while (num !=0):
# 	sum = sum + num % 10
# 	num = num // 10
# print("Сумма чисел равна: ", sum)	
# num = int(x)
# mult = 1
# while (num !=0):
# 	mult = mult * (num % 10)
# 	num = num // 10
# print("Произвдение чисел равно: ", mult)
# """

# #рулетка
# """
a = "черный"
b = "красный"
c = "зеленый"
x = int(input("Введите число: "))
if x == 0:
	print(c)
elif 28 < x < 37: 
	if x % 2 == 0:
		print(b)
	else:
		print(a)	
elif 18 < x < 29:
	if x % 2 == 0:
		print(a)	
	else:
		print(b)
elif 10 < x < 19:
	if x % 2 == 0:
		print(b)
	else:
		print(a)		
elif 0 < x < 11:
	if x % 2 == 0:
		print(a)
	else:
		print(b)
else:
    print("ошибка ввода")
# """	
	
# #algorithm tasks

# #1

# """
# a = 15
# b = 55
# import random
# list = [a, b]
# random.shuffle(list)
# print(list)
# """

# #2
# """
# h, m = input("Введите время: ").split()
# h = int(h)
# m = int(m)
# y = 60 - m
# if h == 6:
# 	x = 6
# # elif h == 0:
# # 	x = 10
# if m == 00:
# 	y = 00
# if 0 <= h <= 11:
# 	x = 12 - h 
# # elif 7 <= h <= 11:
# # 	x = 10 - h
# print(x, y)
# """