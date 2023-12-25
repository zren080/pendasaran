data_angka = [1,2,4,4,9,3,6,4,7,8,1]
print(f'data list =\n{data_angka}')

# count data
count_data = data_angka.count(4)
print(f'data 4 =>{count_data}')
count_data = data_angka.count(1)
print(f'data 1 =>{count_data}')

# ambil posisi data (index)
data_str = ('fesnil','zren','green','leni')
print(f'data nama =>{data_str}')

index_data_leni = data_str.index('leni')
print(f'posisi leni ={index_data_leni}')
index_data_green = data_str.index('green')
print(f'posisi green ={index_data_green}')

# mengurutkan list 
print(f'angka sebelum di sort = \n{data_angka}')
data_angka.sort()
print(f'data angka setelah di sort = \n{data_angka}')

print(f'data ={data_str}')
data_str.sort()
print(f'data sort ={data_str}')

# reserver/membalikan data
data_angka.reverse()
print(data_angka)

data_str.reverse()
print(data_str)





















