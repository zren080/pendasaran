#1. CARA MENCARI SAMPAI 5 SISI

sisi = (10)

# cara mencari ganjil
count = 1
spasi = int(sisi/2) 
while True:
    print(' '*spasi,'+'*count)
    print(spasi)
    spasi -= 1
    count += 1
    #print(f'bintang sekarang ->{count}')
    if count%2:            
        continue

    else:
        count += 1
        
    
    if count > sisi:
        break

# 2. CARA MENCARI SAMPAI 6 SISI

sisi = 10
count = 1

spasi = int(sisi/2)

while True:
    if count % 2:
        # print jika ganjil
        print(" "*spasi,"+"*count)
        print(spasi)
        #print(f'bintang sekarang ->{count}')
        spasi -= 1
        count += 1

    else:   # akan kembali ke atas jika ganjil
        count += 1

        continue
    # akan break jika count melebihi sisi

    if count > sisi:

        break

