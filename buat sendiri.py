sisi = (10)

# cara mencari ganjil
count = 1
spasi = int(sisi/2) 
while True:
    print(' '*spasi,'+'*count)
    spasi -= 1
    count += 1
    #print(spasi)
    #print(f'bintang sekarang ->{count}')
    if count%2:            
        continue

    count += 1
        
    
    if count > sisi:
        break



#print(5*'='+'kerucut'+'='*5)
# kebawah
count = count - 4
spasi = 2
while True:
    #print(spasi)
    # print jika ganjil
    if count%2:    
        print(' '*spasi,'+'*count)
        #print(f'bintang sekarang ->{count}')
        spasi += 1
        count -= 1 # tidak bisa di kurangkan sekaligus ( harus satu persatu)
    else: # harus membuat kondisi baru kalau ingin mengurangi count
        count -= 1
        continue
        #akan naik ke atas jika ganjil
        
    if count == 0:
        break



