def tambah(*args):
    angka = 0
    for i in args:
        angka += i
    
    return angka

def kali(*args):
    hasil = 1
    for i in args:
        hasil *= i

    return hasil

def pangkat(n:int):
    return lambda lop:lop**n
    

