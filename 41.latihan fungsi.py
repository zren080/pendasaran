'''Latihan Fungsi'''

# def itu satu tujuan

import os

os.system('clear')

def header():
    '''Fungsi Header'''
    print(f'{"PROGRAM PENGHITUNG LUAS":^40}')
    print(f'{"DAN KELILING PERSEGI PANJANG":^40}')
    print(f'{"-"*40:^40}')

def input_user():
    '''Fungsi Input User'''
    #mengambil input user
    LEBAR = int(input('masukan nilai lebar :'))
    PANJANG = int(input('masukan nilai panjang :'))

    return LEBAR,PANJANG

def hitung_luas(lebar,panjang):
    '''Fungsi Luas'''

    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''Fungsi Keliling'''
    return 2*(lebar+panjang)

def display(message,value):
    '''Fungsi Display'''
    print(f'hasil perhitungan {message} = {value}')

while True:
    
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)
    
    display('luas',LUAS)
    display('keliling',KELILING)

    isContinue = input('mau lanjut (y/n)?')

    if isContinue == 'n':
        break

print('Terima Kasih')





