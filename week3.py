# week3 homework
##############################################################################

# 1st task

# list: ordered, changeable, allow duplicates
# tuple: ordered, allow duplicates
# set: changeable
# dict: ordered, changeable

# 2nd task

# phrase = ["HELLO", "I", "AM", "WRITING", "CODE"]
# phrase.sort()
# print(phrase)

# a = str(input("enter your phrase: "))
# b = sorted(a.split())
# print(b)

# 3rd task

# a = ["Alibek", "Dana", "Beka", "Johhny"]
# print(a[0] + " программист\n", a[1] + " программист\n", a[2] + " программист\n", a[3] + " программист\n")

# 4th task

# with open("word.txt","a") as f:
#     for i in range(1000):
#         f.write("i am developer\n")

# 5th task

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)

# 6th task

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for i in a:
#     if i in c:
#         continue
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)

# 7th task

# a = [2,3,4,7,237,2,2,4]
# for x in a:
#     if x % 2 == 0:
#         print(x)
#     elif x == 237:
#         break

# 8th task

# list = ("asdasdsdd! Asd lsdl!! sd ! Sd")
# x = list.count("!")
# print(x)

# 9th task

# a = input("enter the list 1: ")
# b = a.split()
# c = set(b)
# if len(b) == len(c):
#     print("true")
# else:
#     print("false")

# 10th task

# text = max((input("enter your text: ")).split(), key=len)
# print(text)
# text = input("enter your text: ")
# text = text.split()
# result = dict((i, text.count(i)) for i in text)
# print(max(result, key=result.get))


# 11th task

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

# 12th task

# from random import random
# a = round(random() * 50)
# print(a)
# i = 1
# print("guess random number, u`ve got 3 attempts")
# while i < 4:
#     b = int(input(str(i) + " attempt: "))
#     if a > b:
#         print("lower")
#     elif a < b:
#         print("higher")
#     else:
#         print("successful")
#         break
#     i += 1
# else:
#     print("game over")

# 13th task

# a = input("enter three numbers: ")
# b = a.split()
# c = set(b)
# if len(b) == len(c):
#     print("0")
# elif len(b) - len(c) == 1:
#     print("2")
# else:
#     print("3")

# 14th task

# a = input("enter your text: ")
# b = a.split()
# c = "_".join(b)
# print(c)

# 15th task

# def mylist(m1, m2, amount, l):
#     from random import randint
#     for i in range(amount):
#         l.append(randint(m1, m2))
# def analysis(your_list, your_dict):
#     for i in your_list:
#         if i in your_dict:
#             your_dict[i] += 1
#         else:
#             your_dict[i] = 1
#
#
# lst = []
# dct = {}
#
# mn = int(input('Минимум: '))
# mx = int(input('Максимум: '))
# qty = int(input('Количество элементов: '))
#
# mylist(mn, mx, qty, lst)
# analysis(lst, dct)
#
# for item in sorted(dct):
#     print("'%d':%d" % (item, dct[item]))

# 16th task

# def multiply(n):
#     total = 1
#     for i in range(0, len(n)):
#         total *= n[i]
#     print(total)
#
# multiply([int(x) for x in input("enter list: ").split()])

# def sum(n):
#     total = 0
#     for i in range(0, len(n)):
#         total += n[i]
#     print(total)
# sum([int(x) for x in input("enter list: ").split()])


# def mltpl(n):
#     i = 0
#     total = 1
#     while i < len(n):
#         total *= n[i]
#         i += 1
#     print(total)
# mltpl([int(x) for x in input("enter list: ").split()])

# def mltpl(n):
#     i = 0
#     total = 0
#     while i < len(n):
#         total += n[i]
#         i += 1
#     print(total)
# mltpl([int(x) for x in input("enter list: ").split()])

# 17th task

# a = input("enter first number: ")
# b = input("enter second number: ")
# c = a+b
# d = b+a
# print(max(c, d))

# 18th task

# year = int(input("enter year: "))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("високосный")
#
# else:
#     print("невисокосный")

# 19th task

# import os, sys
# root = "/Users/evgenij/Desktop/python"
# dir = os.listdir(root)
#
# for files in dir:
#     print(files)

# 20th task

# try:
#     filename_parts = (input("enter file name: ").split('.'))
#     print(filename_parts[1])
# except:
#     print("no ext")

# 21st task

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

# algo #3
# a = input("start point: ").split()
# b = input("end point: ").split()
# if a[0] == b[0] or a[1] == b[1]:
#     print("YES")
# else:
#     print("NO")

# algo #4

# n = input("enter your list: ").split()
# a = n[0]
# b = n[1]
# c = n[2]
# d = a+b+c
# e = a+c+b
# f = b+a+c
# g = b+c+a
# h = c+a+b
# j = c+b+a
# print(max(d, e, f, g, h, j))