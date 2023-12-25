## --LIST--
# list itu adalah kumpulan data

# kumpulan numbers

data_list = [1,2,3,4,5,6,7,] # angka nya bisa acakan
print(data_list)

# kumpulan string

data_str = ['zren','green','gray']
print(data_str)

# kumpulan boolean
data_boolean = [True,False,True,True,False]
print(data_boolean)

# kumpulan campuran

data_campuran = ['zren',2,True,'green',4,False]
print(data_campuran)

## cara membuat list alternatif

# range(start,stop,step)
data_range = list(range(0,10,3,)) #list nya bisa di casting
print(data_range)

# membuat list dengan for loop, list comprenshinon
for_list = [a for a in range(0,10)]
print(for_list)
# menambahkan operator/operasi assaigment
for_list = [a**2 for a in range(0,10)]
print(for_list)

# membuat list pake for pake if
list_for_if = [i for i in range(0,10) if i != 5] # menghilangkan angka yang kita pilih
print(list_for_if)

# mencari genap dan ganjil
# bisa juga di pakai operator assaigment
list_for_if = [i for i in range(0,10) if i%2 == 0] # genap(1),ganjil(0) atau pakai (!=)
print(list_for_if)






