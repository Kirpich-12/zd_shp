from random import randint

mas = [] #создаем пустой список для сортировки пузырьком
sc1 = 1
sc1_1 = 0
sc2 = 0
sc2_1 = 0

for i in range (0, 100): #цикл для добавления элементов в список
    a = randint(1, 1_000_000) #выбираем число
    mas.append(a) #добавляем его в список
mas.sort() # сортировка списка

print(f'Список: {mas}')
print('Введите искомый элемент')
isk = int(input())

print('Линейный поиск:')
if isk in mas:
    for i in range(len(mas)):
        if mas[i] == isk:
            break
        else:
            sc1 += 1
            sc1_1 += 1 
    print(f"Искомый элемент под индексом: {sc1_1} \n Кол-во операций:{sc1}")
else:
    print("Такого элемента нет в данном списке")

print("Бинарный поиск:")

left = 0
right = len(mas) - 1

while left <= right:
    center = (left + right) // 2
    if isk == mas[center]:
        print(f'Номер искомого элемента: {center} \n Количество операций {sc2_1}')
        break
    if isk > mas[center]:
        left = center + 1
    else:
        right = center - 1
    sc2_1 += 1
else:
    print('No value')