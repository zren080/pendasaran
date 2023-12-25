'''**kwargs'''
# kwargs = key word as
# kwargs adalah keyworld arguments

def fungsi(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    umur = kwargs['umur']
    print(f'{nama} tinggi={tinggi} umur={umur}')

fungsi(nama='zren',tinggi=170,umur=18)
'''Pengurangan dengan penamabahan tidak bisa di gabungkan'''
## MENAMBAH DAN MENGURANG
def math(*args,**kwargs):
    output = 0
    num1 = args[0]
    num2 = args[1]
    kurang = num1-num2 
    if kwargs['option'] == 'tambah':
        for i in args:
            output += i
        return output
    elif kwargs['option'] == 'kurang':
        for i in args:
            num2 = i
        return kurang
    
    else:
        print('tidak ada operasi')
    

hasil = math(1,2,3,4,5,option='tambah')
print(f'hasil tambahan ={hasil}')

hasil = math(10,4,option='kurang')
print(f'hasil kurang ={hasil}')

## MENAMBAH DAN PENGALIAN
def math(*args,**kwargs):
    if kwargs['option'] == 'tambah':
        output = 0 
        for i in args:
            output += i
    elif kwargs['option'] == 'kali':
        output = 1
        for i in args:
            output = i
    
    else:
        print('tidak ada operasi')
    
    return output

hasil = math(1,2,3,4,5,option='tambah')
print(f'hasil tambahan ={hasil}')

hasil = math(20,4,option='kali')
print(f'hasil kali ={hasil}')

