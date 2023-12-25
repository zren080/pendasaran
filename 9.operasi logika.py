# OPERASI LOGIKA ATAUA BOOLEAN

# not, or, and, xor(^)

# fungis not: mengubah hasil yang seharsunya true menjadi false/kebalikannya
print('====NOT====') 
a = True
c = not a # menghasilkan kebalikan dari a
print('data a','=',a)
print('--------------NOT')
print('data c','=',c)

# OR # semua hasilnya akan true, kecuali nilai keduanya false 
print('====OR====') # akan false jika keduanya false
a = False
b = False
c = a or b
print(a,'or',b,'=',c,)
a = False
b = True
c = a or b
print(a,'or',b,' =',c,)
a = True
b = False
c = a or b
print(a,' or',b,'=',c,)
a = True
b = True
c = a or b
print(a,' or',b,' =',c,)

# AND # semuan hasilnya akan false, kecuali bilangan keduanya true
print('====AND====') # akan true jika keduanya true
a = False
b = False
c = a and b
print(a,'and',b,'=',c,)
a = False
b = True
c = a and b
print(a,'and',b,' =',c,)
a = True
b = False
c = a and b
print(a,' and',b,'=',c,)
a = True
b = True
c = a and b
print(a,' and',b,' =',c,)

# XOR # akan true jika salah satu true
print('====XOR====') # sisanya false
a = False
b = False
c = a ^ b
print(a,'^',b,'=',c,)
a = False
b = True
c = a ^ b
print(a,'^',b,' =',c,)
a = True
b = False
c = a ^ b
print(a,'^',b,'=',c,)
a = True
b = True
c = a ^ b
print(a,'^',b,' =',c,)
