# Задача 7. Вариант 13.
#  Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.
 
# Kashaykin I. G.
# 27.05.2016


import random
satellite=["Фобос","Деймос"]
s=random.choice(satellite)
print("Привет! Угадай название одного из двух спутников Марса")
print("Чем меньше попыток вы используете, тем больше баллов заработаете!")
a = ''
p=0
while a!=s:
	p=p+1
	a=input("Введите основную физическую переменную - ")
	if a!=s:
		print("Вы не угадали! Попробуйте еще раз!")
d=11-p
print("Вы угадали! Правильная переменная - ", s)
print("Вы заработали - ", d,' баллов')
input("Если хотите выйти из игры нажмите enter")