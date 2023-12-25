peserta_0 = ['zren',18,'laki-laki']
peserta_1 = ['green',20,'laki-laki']
peserta_2 = ['zeni',18,'perempuan']

combaind_peserta = [peserta_0,peserta_1,peserta_2]
print(combaind_peserta)

list_copy = combaind_peserta.copy()
print(f'peserta={list_copy}')
peserta_0[0] = 'geni'
print(f'peserta={list_copy}')
print(f'peserta = {peserta_0}')