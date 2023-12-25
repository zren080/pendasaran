sisi = 5 

print(17*'='+'FOR'+17*'=')
count = 1
for i in range(5):
    print('*'*count)
    count += 1

print('akhir dari for \n')

print(15*'='+'WHILE'+15*'=')
count = 1
while True:
    print('*'*count)
    count += 1

    if count > sisi:
        break

print('akhir dari while \n')


print(*'='+'WHILE GANJIL'+13*'=')

print(15*'='+'WHILE'+15*'=')

count = 1
while True:
    if (count%2):
        print('*'*count)
        count += 1
    else:
        count += 1
        continue
    
    if count > sisi:
        break

print('akhir dari while \n')



















