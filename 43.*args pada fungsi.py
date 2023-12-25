'''*args'''

# memasukan data/arguments

def fungsi(nama,tinggi,umur):
     
    print(f'{nama} tinggi:{tinggi} umur:{umur}')

fungsi('zren',170,18)

def fungsi(data):
    data_list = data.copy()
    nama = data_list[0]
    tinggi = data_list[1]
    umur = data_list[2]
    print(f'{nama} tinggi:{tinggi} umur:{umur}')

fungsi(['refi',160,17])

# args itu bisa sembarang asal didahulunya ada bintang
def tambah(*data):
    # data tipenya tuple dan bisa di iterable
    output = 0
    for i in data:
        output += i

    return output

hasil = tambah(1,2,3)
print(f'hasil {hasil}')

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    umur = args[2]
    print(f'{nama} tinggi:{tinggi} umur:{umur}')



fungsi('teli',164,20)







