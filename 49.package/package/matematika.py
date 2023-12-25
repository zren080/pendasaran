def tambah(*args):
    angka = 0
    for i in args:
        angka += i
    return angka

def pangkat(n:int):
    return lambda xe:xe**n

def kali(*args:int):
    angka = 2
    for i in args:
        angka *= i
    return angka