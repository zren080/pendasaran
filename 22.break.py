# BREAK

angka = 0

while angka < 7 :
    angka += 1
    print(f'angka sekarang -> {angka}')

    if angka == 4:
        print('yooo')
        break
    
    print('sepp')

print('akhir')

print(30*'=')

# input
data_int = int(input('hitung sampai=>'))

angka = 0

while True:
    angka += 2
    print(f'angka sekarang -> {angka}')

    if angka == data_int:
        print('yooo')
        break
    
    print('sepp')

print('akhir')