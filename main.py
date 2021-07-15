# 1st week 1 st Task
"""
print("hello i am programmer")
name = "Yevgeniy"
print("My name is "+ name)
a = "103"
a = int(a)
b = 301
not_found = (a + b)
not_found = str(not_found)
print(not_found)
print("not_found " + not_found)
"""
# 1st week 2nd Task

i = "2.1"
h = "1.04"
pi = (float(i) + float(h))
pi = str(pi)
print("pi = " + pi)
a = "Hello"
b = 123
c = 0
d = -1
f = "-1"
"""
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(f))
"""
a = bool(a)
b = bool(b)
c = bool(c)
d = bool(d)
f = bool(f)
#print(a,b,c,d,f)
print(a)
print(b)
print(c)
print(d)
print(f)
print("I","like","Python", sep="***", end="\n")
# параметр sep (separator) используется как разделитель, что то вроде табуляции в MS Office только между задаными частями кода/текста и тд
# параметр end после всего что написано в гугл, честно говоря ничего не понял, но после того как поюзал на практике получилось что данный параметр объединяет строки в одну, то есть если я пропишу параметр просто с пробелом, то он через пробел объединяет строки
"""
s = 0 
k = 30 
d = k - 5 
k = 2 * d 
s = k - 100
s = -50
"""
k = int(input("Стоимость Монитора :"))
l = int(input("Стоимость Системного блока :"))
m = int(input("Стоимость Клавиатуры :"))
n = int(input("Стоимость Мыши :"))
t = 3 * (k + l + m + n)
print("Стоимость покупки 3 ПК: " + str(t))
x = int(input("Введите число: "))
print("Следующее за числом " + str(x) + " число: " + str(x + 1))
print("Для числа " + str(x) + " предыдущее число: " + str(x - 1))