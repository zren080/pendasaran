'''Type Hints Pada Fungsi'''

'''
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("zren")
fungsi(True)
'''
'''any itu adalah menentukan kalau itu adalah int atau str dll'''
# penggunaan type hints
import string

def hints(argument:int) -> int:
    output_int = 10**argument
    return output_int
    
hasil = hints(2)
print(hasil)

# no return
print(f'type data = {type(hasil)}')

def display(parameter:string):
    print(parameter)

display('zren')

import os

hasil = os.system('sudo') # bisa di gunakan untuk mencek nilai bytes suatu command
print(hasil)



