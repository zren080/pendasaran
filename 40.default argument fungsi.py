'''Default Argument Fungsi'''

# def fungsi(argumnet)
# def fungsi(argument = nilai defaultnya)

# contoh 1

def shay_hello(nama = 'welcome'):
    '''fungsi dengan default argument'''
    print(f'hello {nama}')

shay_hello('zren')
shay_hello()

# contoh 2

def tentang(nama,pesan = 'haii'):
    print(f'{nama} {pesan}')

tentang('haiii','zren')
tentang('refi')

# contoh 3

def kuadrat(angka,pangkat = 2):
    hasil = angka**pangkat # kalau terbalik maka hasilnya akan beda
    return hasil

print(kuadrat(3))

# contoh 4

def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10)) #cara 1: mengubah suatu argument default
print(fungsi(3,4,input3=10)) #cara 2: mengubah suatu argument default


















