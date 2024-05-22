'''
file = open('text.txt', 'a+', encoding='utf-8')
print(file.read())

# print(file.readline())

#вывести посимвольно текст( в столбик)
# for row in file:
#     for letter in row:
#         print(letter)


# s = file.readlines()
# # print(s) #['Python\n', 'Two\n', 'String\n', 'Питон'] с помощью среза можно проигнорировать два последние элемента
# for string in s:
#     print(string[:-1]) #убрали \n


# #для записи
# file.write('hello\n') # надо указать в параметрах, что файл записываемый 'r'рид, 'w'райт, 'a'-добавление в конец файла
# #файл перезаписался на одну запись hello и это уже не исправить
#
# #чтобы добавить в конец файла - добавляем режим а или а+ - он поддерживает и запись и чтение
# file.write('hi\n')
# file.write('python\n')
# file.write('good evening\n')

#после того как закончили работу с файлом - нужно почистить его
file.close()
'''


# lst = []
#
# for i in range(1000):
#     lst.append(open('text.txt').close())


#контекстный менеджер - автоматические вызывает close

# with open('text.txt', 'a+') as f:  # f - название через которое будем обращаться, псевдоним
#     f.write('hello')
#     f.seek(0) #переводит курсор в самое начало
#     print(f.read())

#практика 1

# with open('text.txt', 'a+') as f, open('text2.txt', 'a+') as f2:
#     f.seek(0)
#     s = f.readlines()
#     for i in s:
#         if len(i)>7:
#             f2.write(i)

#практика 2




def fio(name, fam, sal):
    with open('works.txt', 'a+') as f:
        f.seek(0)
        f.write(f'{name},{fam},{sal}\n')
def avg():
    employees = []
    total_salary = 0
    cnt = 0

    with open('works.txt', 'r') as f:
        for i in f.readlines():
            name, fam, sal = i.strip().split(',')
            employees.append([name, fam])
            total_salary += float(sal)
            cnt += 1
    if cnt == 0:
        av_sal = 0
    else:
        av_sal = total_salary / cnt

    print(f'Средняя зп: {av_sal}')
    print('Список сотрудников:')
    for name, fam in employees:
        print(f'{name} {fam}')
avg()

# fio('Иван', 'Иванов', 10000)
# fio('Петр','Петров', 20000)
# fio('Артем','Артемов', 30000)