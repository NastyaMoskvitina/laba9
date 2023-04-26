import os
import glob
from PIL import ImageFilter, Image
os.chdir("9.1")
a=os.getcwd() #копируем путь
if not os.path.isdir("new"):
    os.mkdir("new")
for img in glob.glob('*.jpg'):
     with Image.open(img) as im:
         im.load()
         lart = im.filter(ImageFilter.FIND_EDGES)
         os.chdir("new")
         lart.save("new_" + img)
         os.chdir(a)


def zadacha3():
    import csv
    otvet='Нужно купить:\n'
    summa=0
    with open('/Users/nastya/Desktop/laba9/file9.csv', newline='', encoding='utf-8 ') as per:
        reader= csv.reader(per)
        zagolovok = next(per)
        for row in reader:
            otvet = otvet+row[0]+' - '+row[1]+ ' шт. за '+ row[2] + ' руб.\n'
            summa+=int(row[2])
    print(otvet+'Итоговая сумма = ', summa, ' руб' )

zadacha3()


#ghn