# Повторение списки
#Описание: Напишите функцию, которая принимает список чисел, удаляет все дубликаты и
# возвращает отсортированный список уникальных чисел.

#1 вар
# def list1(s):
#     return list(set(s))
# print(list1('123454321'))

#2 вар
# def spisok(s):
#     n = []
#     for i in s:
#         if i not in n:
#             n.append(i)
#     return n
# print(spisok([[123, 123], [123, 123], 3, 3, 4, 'раз', 'раз']))



# lst = [2, 6, 7, 9]
# lst2 = [3,2,1]
# print(lst[1])
# lst[2] = 4
# #методы
#
# lst.append(7)
# lst.insert(1, 10)
# lst.extend(lst2)
# print(lst)
# lst.remove(2)
# print(lst)
# l = lst.pop(1) #
# lst.clear()
# index = lst.index(2)
# cnt = lst.count(25)

# #Напишите функцию, которая принимает два списка чисел, объединяет их и возвращает один отсортированный список.
#
def spisok(list1, list2):
    list1.extend(list2)
    return sorted(list1)
l1 = [1,2,3,4]
l2 = [4,3,6,7]
print(spisok(l1,l2))
#
# #Напишите функцию, которая принимает список и элемент, и удаляет все вхождения этого элемента из списка.
#
def spisok(s, el):
    while el in s:
        s.remove(el)
    return s
l1 = [1,3,3,2,3,4,3,3]
el = 3
print(spisok(l1, el))
#
# #Напишите функцию, которая принимает список и переставляет его элементы в обратном порядке.
#
def spis(lst):
    return list(reversed(lst))
l = [1,3,3,2,3,4,3,3]
print(spis(l))

# #Напишите функцию, которая принимает список и элемент, и возвращает список индексов
# # всех вхождений этого элемента в исходном списке.
#
def spisok(s, el):
    a = []
    for i in range(len(s)):
        if s[i] == el:
            a.append(i)
    return a
l = [1,3,3,2,3,4,3,3] #1, 2, 4, 6, 7
print(spisok(l, 3))

#Напишите функцию, которая принимает два списка и возвращает новый список,
# содержащий все элементы из обоих списков без дублирования.

def spisok(list1, list2):
    list1.extend(list2)
    return list(set(sorted(list1)))
l1 = [1,2,3,4]
l2 = [4,3,6,7]
print(spisok(l1,l2))

#Напишите функцию, которая принимает список чисел и возвращает среднее значение

def spis(lst):
    return sum(lst) / len(lst)
l = [1, 3, 3, 2, 3, 4, 3, 3]
print(spis(l))