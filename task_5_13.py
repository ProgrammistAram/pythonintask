# Задача 5. Вариант 13.
# Напишите программу, которая бы при запуске случайным образом отображала имя одного из двенадцати апостолов.
 
# Kashaykin I.G.
# 27.05.2016

print("\nОдним из двенадцати апостоловявляется:")

import random
apostle=("Андрей","Пётр","Иоанн","Иаков","Филипп","Варфаломей","Матфей","Фома","Иаков Алфеев","Фаддей","Симон","Иуда",)
a=random.choice(apostle)
print(a)

input("\nНажмите enter для завершения")