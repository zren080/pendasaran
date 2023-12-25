## Project Segitiga
angka = int(input('masukan sisi ='))
#angka = int(input('masukan sisi ='))

count = 1
spasi = int(angka/2)
while True:
    print(' '*spasi,'.'*count)
    spasi -= 1
    count += 1
    
    if count%2:
        continue
    
    count += 1
    
    if count > angka:
        break

count = count - 4
spasi = 2
while True:
    if count%2:
        print(' '*spasi,'.'*count)
        spasi += 1
        count -= 1
    
    else:
        count -= 1
        continue
    
    if count == 0:
        break

