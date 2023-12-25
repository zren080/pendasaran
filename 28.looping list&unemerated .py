## looping dari list

# for loop
print('\nfor loop')
kumpulan_angka = [1,2,4,1,1,8,5]

for angka in kumpulan_angka:
    print(f'angka ={angka}')

peserta = ['zren','reni','lesi','qeri','jefri']

for nama in peserta:
    print(f'peserta ={nama}')

# for loop dan range
print('\nfor loop dan range')

kumpulan_angka = [12,4,5,6,3,4,1]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f'angka = {kumpulan_angka[i]}')

# while
print('\nwhile')

kumpulan_angka = [12,4,5,6,3,4,1]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f'angka = {kumpulan_angka[i]}')
    i += 1

# list comprehension
print('\nlist comprehension')
data = ['zren',5,1,9,'reni']

[print(f'data = {i}')for i in data]

# list assaigment
print('\nlist assaigment')
angka = [12,4,5,6,3,4,1]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate 
print('\nenumereta')
data_0 = ['zren',5,1,9,'reni']

for index,data in enumerate(data_0):
    print(f'index = {index}, data = {data}')
