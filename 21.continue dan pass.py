# continue dan pass

# pass -> dia berfungsi sebagai dummy atau tidak di eksekusi 

#angka = 0

#while angka < 5:
#    angka += 1

  #  if angka == 3:
 #       pass # ini tidak akan di eksekusi

#print('thanks cok')

# continue

angka = 0
print(f'angka sekarang -> {angka}')

while angka < 5:
    angka += 1
    print(f'angka sekarang -> {angka}') # aksi 1

    if angka == 3:
        print('heiii!')
        continue # akan meloncat ke loop selanjutnya

    print('yoii') # aksi 2
         
         
print('selesai')