# ; Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# ; не превосходящие числа N.
N=int(input("Число которое не нужно превосходить: "))
i=2
while i<N:
    i=i*2
    print (i)