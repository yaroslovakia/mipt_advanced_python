import csv

with open("/home/yassya/Рабочий стол/table.csv", "r") as file:
    reader = csv.reader(file)
    lst = list()
    for x in reader:
        lst.append(x)
lst.insert(5, [0, 0, 0, 0, 0, 0])
for i in range(len(lst)):
    lst[i].insert(4, 0)
with open("newfile.csv", "w") as file:
    writer = csv.writer(file)            #На основе открытого файла получаем объект из библиотеки csv
    for el in lst:
        writer.writerow(el) 

