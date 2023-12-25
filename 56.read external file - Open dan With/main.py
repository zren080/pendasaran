## membaca file eksternal
'''jika kita menggunakan REF apabila kita open txt kita juga harus mengclose nya'''

import os
os.system('clear')

print(5*'=',"Membaca File Eksternal",'='*5)

## cara membaca file menggunakan REF(Read Ekternal File)
file = open('data.txt',mode='r')

print(f'status file dibaca : {file.readable()}')
## cara membaca semua baris
#print(file.read())

## cara membaca per line
#print(file.readline()) # ini line 1
#print(file.readline()) # ini line 2

## cara membaca semua baris mejadi list
#print(file.readlines())

## cara menghilankan enter nya (\n)
print(file.readline(),end="") # si enternya di ganti dengan string kosong

## cara mengclose
print(f'apakah sudah di tutup : {file.closed}')
print(file.close)
print(f'apakah sudah di tutup : {file.closed}')


### with
print('\n',5*'=',"Membaca File Eksternal dengan with",'='*5)
'''perbedaan REF dengan with:
with dapat mengclose automatis sedangkan 
REF dia harus di close manual'''
'''lebih simple si wiht'''


with open('data.txt',mode='r') as file:
    content = file.readline()
    print(content,end='')
    print(f'apakah sudah di tutup : {file.closed}')

print(f'apakah sudah di tutup : {file.closed}')












