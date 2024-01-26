# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# alphabet = " B, C, A, L, P "
# print(str(sorted(alphabet)))
#
#
# lst = [1, 2, 3, 4,]
# for i in lst:
#     print(i)
#
#
# lst = [1,2,3,4]
# itr_list = iter(lst)
# print(next(itr_list))
# print(next(itr_list))
# print(next(itr_list))
#
# print(type(lst))
#
#
# lst = [1, 2, 3, 4]
#
# def count_generator():
#     n = 0
#     while True:
#         yield n
#         n += 1
#
# count = count_generator()
# print(next(count))
#
# lst = [i for i in range(10+1)]
# print(lst)
#
# # list_a = [-2, -1, 0, 1, 2, 3, 4, 5,]
# # list_b = [x if x < 0 else x**2 for x in list_a]
# print(*list_b)

# def decor():
#     def wrapper(func):
#         print('---')
#         func()
#         print('---')
#     return wrapper
#


# @decor
# def hello():
#     print('hello')
#
# # hello()
#
# def decor(func):
#     def wrapper(j):
#         print()
#



# lst = [-3, -2, -1, 0, 1, 2, 3]
# listb = [x if x**2  < 0 else x**3 for x in lst]
# print (*listb)

#
# a = [x for x in range(0, 10)]
# def decor():
#     def avarage():
#         print(..... )
#         sum()
#         print(..... )
#         return wrapper
#
#     @decor
#     def sum(*args):
#         pass
#19.01.2024
# import datetime as dataa
#
# d = dataa.date(2012, 11, 1)
# print(d)
#
# print(d.year)
# print(d.day)
#
# print(d.month)
#
# import datetime
# date = datetime.datetime.today()
# print(date.strftime('%d-%m-%y%h:%M'))
#
# myfile = open("hello.txt", "w")
# myfile.close()
#
# with open("hello.txt", "w") as file:
#     file.write("hello world")
#     file.write("/ngood by, world")
#
# #
# readline():
# read():
# readlines():
# #
# import os
# print(os.environ)
# import os
# os.mkdir(r"D:\folder")

# import os
# os.makedirs(r"D:\folder\first\second\third")
#
# import os
# os.rmdir(r"D:\folder")
#

#
#Exel
### Создание и запись

# import openpyxl
#
# workbook = openpyxl.Workbook()
# sheet = workbook.active
#
# data = [
#     ('Alisa', 25, 'New-York'),
#     ('Bob', 30, 'London'),
#     ('Karol', 22, 'Paris')
# ]
#
# for row in data:
#     sheet.append(row)
#
# workbook.save('test1.xlsx')

#sheet.cell(row=1, column=1, value='hello')
#sheet.cell(row=2, column=2, value='hello')
#sheet.cell(row=3, column=3, value='hello')
#sheet['A1'] = 'World'
#
# for i, char in enumerate(range(ord('a'), ord('z') + 1), start=1):
#     sheet.cell(room=2, column=i, value=chr(char))
#
# workbook.save('test1.xlsx')


# import openpyxl
#
# workbook = openpyxl.open('123.xls', read_only=True)
# sheet = workbook.active
#
# for row in range(1,3+1):
#     name = sheet[row][row][0].value
#     surname = sheet[row][1].value
#     age = sheet[row][2].value
#     print(name, surname, age, end='/n')

# import json
# data = {'Name': 'Shoxa',
#          'Surname': 'Xolmuxamedov',
#          'age': 21,}
# with open('json_test.json', 'w') as file:
#     json.dump(data,file)

# import json
# conten = {}
#
# with open('json_test.json', 'r') as file:
#     conten = json.load(file)
#
# print(conten)

# import doctest
#
# doc = doctest.Document('example.docx')
#
# # количество абзацев в документе
# print(len(doc.paragraphs))
#
# # текст первого абзаца в документе
# print(doc.paragraphs[0].text)
#
# # текст второго абзаца в документе
# print(doc.paragraphs[1].text)
#
# # текст первого Run второго абзаца
# print(doc.paragraphs[1].runs[0].text)
#
# import docx
#
# doc = docx.Document('example.docx')
#
# # изменяем стили для всех параграфов
# for paragraph in doc.paragraphs:
#     paragraph.style = 'Normal'
#
# doc.save('restyled.docx')

#
# import docx
#
# os.chdir('C:\\example')
#
# doc1 = docx.Document('example.docx')
# doc2 = docx.Document('restyled.docx')
#
# # получаем из первого документа стили всех абзацев
# styles = []
# for paragraph in doc1.paragraphs:
#     styles.append(paragraph.style)
#
# # применяем стили ко всем абзацам второго документа
# for i in range(len(doc2.paragraphs)):
#     doc2.paragraphs[i].style = styles[i]
#
# doc2.save('restored.docx')
#
# import docx
# doc = docx.Document()
# doc.add_paragraph('hello')
# doc.save('hello.docx')

### Чтение DOCX
# file_path = ' hello.docx'
# doc = docx.Document(file_path)
# text = ""
# for paragraph in doc.paragraphs:
#     text += paragraph.text + "/n"
# print(text)
#
# import json
# conten = {}
#
# with open('ls.json', 'r') as file:
#     conten = json.load(file)
#     print(conten)


