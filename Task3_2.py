numbers = [2, 5, 13, 7, 6, 4]
size = 6
sum = 0
avg = 0
index = 0
for i in range(0, size):
    sum += numbers[index]
    index += 1
avg = sum/size
print ("Cреднее арифметическое среди всех элементов массива "'"nambers"'" = ", avg)