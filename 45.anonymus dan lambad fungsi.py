# lamba function
# contoh objek = {} () []
# contoh elemen = isi di dalam objek -> (2)
## fungsi biasa
import os

os.system('clear')

def f_biasa(angka1):
    return angka1**2

print(f'hasil pangkat = {f_biasa(5)}')

## lamba dengan fungsi
# output/variabel = lambda argument:ekspresison
f_lambda = lambda angka2:angka2**2
print(f'hasil pangkat = {f_lambda(3)}')
#lambda bisa juga di tambahkan beberap input
pangkat = lambda num,pow,lop : num**pow+lop
print(f'hasil pangkat = {pangkat(4,2,7)}')

## sorting untuk list biasa
data_List = ['resefi','gerfi','zren']
data_List.sort()
#print(f'sorted data list = {data_List}')

## sorting pakai panjang 
# key itu akan menjadi parameter kalau di isi selain key akan menjadi function
data_List.sort(key=len)
print(f'sorted data list by len = {data_List}')
# cara fungsi biasa
def panjang_nama(nama):
    return len(nama)
data_List.sort(key=panjang_nama)
print(f'sorted data list by len = {data_List}')

## sort pakai lambda
data_List.sort(key=lambda nama:len(nama))
print(f'sorted data list by len lambda= {data_List}')

## filter
# kegunaan filter adalah untuk menyaring elemen2 yang tidak akan di print
# filter tidak bisa di kali tambah bagi kurang, cuman memfilter
list_data = [1,2,3,4,5,6,7,8,9,10]

def kurang_dari(angka):
    return angka < 5
    
hasil = list(filter(kurang_dari,list_data))
print(hasil)
hasil = list(filter(lambda lop:lop<7 ,list_data))
print(hasil)

# mengambil genap
genap = list(filter(lambda jel:(jel%2==0) ,list_data))
print(f'hasil genap ={genap}')
# mengambil ganjil
ganjil = list(filter(lambda jel:(jel%2!=0) ,list_data))
print(f'hasil ganjil ={ganjil}')
# kelipatan 3
kelipatan3 = list(filter(lambda jel:(jel%3==0) ,list_data))
print(f'hasil kelipatan 3 ={kelipatan3}')

## anonymous function/fungsi
# currying <- Haskell Curry

def pangkat1(argument,value):
    hasil = argument**value
    return hasil

hasil_data = pangkat1(5,2)
print(f'hasil fungsi biasa ={hasil_data}')

# dengan currying menjadi

def pangkat3(n:int):
    return lambda jil:jil**n

pangkat_2 = pangkat3(2)
print(f'hasil currying lambda ={pangkat_2(5)}')
pangkat_3 = pangkat3(3)
print(f'hasil currying lambda ={pangkat_3(5)}')
print(f'pangkat bebas ={pangkat3(3)(6)}') # (3)pangkat , (6)nilai yang akan di pangkatkan



