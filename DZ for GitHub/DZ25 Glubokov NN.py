import os.path
import os
from math import *
from random import *
import re
import time

liner = '---------------'
print(liner * 7)
print('Задание №1')
read_file1, read_file2, write_file = 'ReadFile1.txt', 'ReadFile2.txt', 'WriteFile.txt'
with  open(read_file1, 'w') as rw1, open(read_file2, 'w') as rw2:
    rw1.write('''Я дева мать, дочь своего же сына,
Смиренней и возвышенней всего,
Предъизбранная промыслом вершина,
В тебе явилось наше естество
Столь благородным, что его творящий
Не пренебрег твореньем стать его.
В твоей утробе стала вновь горящей
Любовь, чьим жаром; райский цвет возник,
Раскрывшийся в тиши непреходящей.
Здесь ты для нас — любви полдневный миг;
А в дельном мире, смертных напояя,
Ты — упования живой родник.
Ты так властна, и мощь твоя такая,
Что было бы стремить без крыл полет —
Ждать милости, к тебе не прибегая.''')
    rw2.write('''Не только тем, кто просит, подает
Твоя забота помощь и спасенье,
Но просьбы исполняет наперед.
Ты — состраданье, ты — благоволенье,
Ты — всяческая щедрость, ты одна —
Всех совершенств душевных совмещенье!
Он, человек, который ото дна
Вселенной вплоть досюда, часть за частью,
Селенья духов обозрел сполна,
К тебе зовет о наделенье властью
Столь мощною очей его земных,
Чтоб их вознесть к Верховнейшему Счастью.''')

with open(write_file, 'w') as wf, open(read_file1, 'r') as rf1, open(read_file2, 'r') as rf2:
    for line in rf1:
        wf.write(line)
    for line in rf2:
        wf.write(line)

print(liner * 7)
print('Задание №2')

with open(write_file, 'r') as wf:
    for i in wf:
        print(i)
        print(len(re.findall(r'[а-яА-Я0-9ёЁa-zA-Z]+', i)), 'слов', len(i), 'символов')

print(liner * 7)
print('Задание №3')
cdm = os.getcwd()
soa = os.listdir()
for i in soa:
    strit=os.path.join(cdm, i)
    if os.path.isfile(strit):
        print(i, ' - file- ', os.path.getsize(strit),'bytes')
    if os.path.isdir(strit):
        print(i, ' - directory ')
