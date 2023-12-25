'''Latihan Fungsi'''

# def itu satu tujuan

import os

os.system('clear')

# membuat header program
def header():
    '''Fungsi Header'''
    print(f'{"PROGRAM PENGHITUNG LUAS":^40}')
    print(f'{"DAN KELILING PERSEGI PANJANG":^40}')
    print(f'{"-"*40:^40}')

# mengambil input user
def input_user():
    '''Fungsi Input User'''
    LEBAR = int(input('masukan nilai lebar :'))
    PANJANG = int(input('masukan nilai panjang :'))

    return LEBAR,PANJANG

# program hitung luas
def penghitung(lebar,panjang):
    '''Fungsi Penghitung'''
    
    return lebar*panjang

def keliling(lebar,panjang):
    '''Fungsi Keliling'''

    return 2*(lebar*panjang)

# tampilkan hasil
def display(message,value):
    '''fungsi display'''
    print(f'hasil perhitungan = {message} = {value}')

while True:
    header()
    
    LEBAR,PANJANG = input_user()
    opsi = input('Hitung luas/keliling/keduanya(1/2/3)?:')
    
    if opsi == '1':
        LUAS = penghitung(LEBAR,PANJANG) # (LUAS hanyalah contstan pemanggil dislay)
        display('luas',LUAS)
    elif opsi == '2':
        KELILING = keliling(LEBAR,PANJANG) # sama seperti di atas
        display('keliling',KELILING)
    elif opsi == '3':
        LUAS = penghitung(LEBAR,PANJANG) # (LUAS hanyalah contstan pemanggil dislay)
        display('luas',LUAS)
        KELILING = keliling(LEBAR,PANJANG) # sama seperti di atas
        display('keliling',KELILING)

        


    iscontinue = input('mau lanjut (y/n)?')

    if iscontinue == 'n':
        break