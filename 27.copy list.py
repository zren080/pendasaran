## Teknik Menduplikat List

a = ['reni','zren','julip','pepi']
print(f'a = {a}\n')

# ini bukan mempuludikat
# yang ini hanya menampilkan list a dengan nama yang beda, addres yang sama
b = a # pass by reference
print(f'b = {b}\n')

## kita akan merubah member dari a

# ini akan merubah kedua list
print(5*'='+'RUBAH'+5*'=')
a[1] = ('yop')
b.sort()
print(f'setelah di ubah A = \n{a}')
print(f'a = {hex(id(a))}')
print(f'setelah di ubah B = \n{b}')
print(f'b = {hex(id(b))}')

# cara menduplikat list dengan benar
# full duplicat
print(5*'='+'COPY'+5*'=')
c = a.copy()
print(f'addres new B= {hex(id(c))}')
