'''macam-macam erorr:
#SyntaxError : kesalahan syntax

# runtime erorr:
1.NameErorr : kesalahan name
2.TypeErorr : kesalan ketik/typo
3.IndexErorr: kesalahan mengambil index
4.AttributeError: kesalahan memakai atribut. atribut itu -> data(join) si join adalah attribute
5.tidak ada yang error tapi pas di tampilkan itu mengeluarkan hasil yang berbeda tidak sesuai diprediksi
6.ZeroDivisionError: kesalan karna menggunakan nol tidak tepat,cara agar tida error ada di bawah
7.FileNotFound: tidak di temukan file
masih banyak lagi macam-macam error
'''

'''
from math import nan

data_input = int(input('masukan angka yang akan di bagi :'))
hasil = nan # atau pakai angka 0

try:
    hasil = 10/data_input

except:
    print(f'hasil tidak boleh 0')

print(f'hasil = {hasil}')
'''

## contoh penggunaan try except 
import os

os.system("clear")

#1.
while(True):
    data_input = int(input('masukan angka yang akan di bagi: '))
    try:
        hasil = 10/data_input
        print(f'hasil pembagian = {hasil}')
        is_done = input('apakah mau lanjut (y/n)?')
        if is_done == 'n':
            break

    except:
        print('hasil yang di masukkan tidak boleh 0')


print('akhir dari program 1')

# 2.

try:
    with open('data.txt','r') as file:
        print(file.read())

except:
    print('data.txt tidak ada, membuat file baru')
    with open('data.txt','w',encoding='utf-8') as file:
        file.write('welcomeee')

print('akhir dari program 2')






