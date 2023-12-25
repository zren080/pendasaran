## OPERASI

# index:0(-3)   1(-2)  2(-1)
data = ['zren','green','zray']

# mengambil data dari list
data_0 = data[0]
print(data_0)
data_2 = data[-2]
print(data_2)
data_2 = data[2]
print(data_2)

# mengambil panjang info data
data_panjang = len(data) # panjang per pekalimat
print(f'panjang dari data = {data_panjang}')

## manipulasi data list

# menambahkan item pada list sesuai posisi
print(f'data sebelum =\n{data}')

data.insert(2,'zeni') # (posisi,item)
print(f'data sesudah =\n{data}')

# menambahkan di akhir list
data.append('resi')
print(f'data sesudah =\n{data}')

# menambahkan list sekaligus ke dalam list
data_baru = ['rina','zeni','yeni']
data.extend(data_baru)
print(f'data digabungkan =\n{data}')

# merubah data
data[-4] = 'refi'
print(f'data rubah =\n{data}')

# meremove data
data.remove('zeni') # akan eror kalau remove nya tidak sesuai
print(f'data remove =\n{data}')

# meremove data paling belakang
data.pop()
print(f'data remove =\n{data}')
# akan menampikan data yang akan di remove
# hanya di pop
data_remove = data.pop()
print(data_remove)



