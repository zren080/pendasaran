'''Fungsi dengan kembalian'''

# template fungsi
# def nama_fungsi(argument):
#   badan fungsi
#   return fungsi    

#fungsi kudrat 

def kuadrat(angka):
    '''fungsi kudrat'''
    output_angka = angka**2
    return output_angka

a = kuadrat(4)
print(a)

print(kuadrat(5))

b = 10 + kuadrat(6)
print(b)

# fungsi tambah

def fungsi_tambah(angka_1,angka_2):
    '''fungsi return multi input'''
    return angka_1 + angka_2

c = fungsi_tambah(6,9)
print(c)
print(fungsi_tambah(5,8))

# fungsi dengan return banyak

def operation_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi

print(operation_matematika(9,8))

d,e,f,g = operation_matematika(9,7)

for i in d,e,f,g:
    print(f'hasilnya {i}')

print(f'hasilnya tambah {d}')
print(f'hasilnya kurang {e}')
print(f'hasilnya kali {f}')
print(f'hasilnya bagi {g}')





