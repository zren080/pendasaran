'''fungsi dengan argument (input)'''

# contoh 1
def dunia(nama):
    '''fungsi dunia menerima input dengan variabel nama'''
    print(f'selamat datang {nama}')

# dunia(input:('masukan nama'))
dunia('refi')

# contoh 2 program tambah 
def tambah(angka_1,angka_2):
    '''fungsi angka menambahkan dengan variabel angka1&2'''
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')

tambah(4,7)

# contoh 3  fungsi dan for loop
def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'monggo kanjeng {peserta}')
        

anggota = ['zren','refi','heni']

say_hi(anggota)



    





