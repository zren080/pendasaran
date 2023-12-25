## __main__ adalah top code leverl environment


# __name__ == "__main__" -> jika di print di program utama

## __name__ pada file program utama 
print(f'nila __name__ pada file program utama = {__name__}')

## __name__ import
'''kalau si (__name__) di import dari program lain,dan di jalankan di program utama
maka hasil yang akan di print/di tampilakan adalah nama dari si modulnya. contoh:'''

#from module_1 import *
from module_1 import fungsi,biji
#import module_1

#print(module_1.__jeli__)

## penggunaan __name__
'''
if __name__ == '__main__' :
    angka1 = 5
    angka2 = 18
    hasil = angka1 + angka2
    print(hasil)
'''

# cara menampilkan dari modul lain
if fungsi() == 'module_1' :
    print("thats'right")

    




