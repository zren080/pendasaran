## NESTED LIST

data_1 = [0,1,2,3]
data_2 = [4,5,6,7]

combaind = [data_1,data_2]
print(f'\ncombain = {combaind}')

# contoh penggunaan nested list
peserta_0 = ['zren',18,'laki-laki']
peserta_1 = ['green',20,'laki-laki']
peserta_2 = ['zeni',18,'perempuan']

combaind_peserta = [peserta_0,peserta_1,peserta_2]

for peserta in combaind_peserta:
    print(f'\nnama\t: {peserta[0]}')
    print(f'umur\t: {peserta[1]}')
    print(f'gender\t: {peserta[2]}\n')

# dengan reference

list_copy = combaind_peserta.copy()
print(f'peserta={list_copy}')
peserta_0[0] = 'geni'
print(f'peserta = {peserta_0}')
print(f'peserta = {combaind_peserta}')