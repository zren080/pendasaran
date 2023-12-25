# TIPE DATA

# Tipe data: angka satuan yang nggak ada titiknya (integer)

data_integer = 13   
print("data    : ", data_integer)
print("-bertipe: ", type(data_integer))

#Tipe data: angka dengan titik (float) 

data_float = 1.3
print("data    : ", data_float)
print("-bertipe: ", type(data_float))

#Tipe data angka dengan koma (tuple)

data_tuple = 1,3
print("data    : ", data_tuple)
print("-bertipe: ", type(data_tuple))

#Tipe data: kumpulan karakter (string)

data_string = "joni 13"
print("data    : ", data_string)
print("-bertipe: ", type(data_string))

#Tipe data: biner true/false (boolean)

data_bool = False
print("data    : ", data_bool)
print("-bertipe: ", type(data_bool))

## TIPE DATA KHUSUS

#Tipe data complex

data_complex = complex(1,   3)
print("data    : ", data_complex)
print("-bertipe: ", type(data_complex))

# Tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(1.3)
print("data    : ", data_c_double)
print("-bertipe: ", type(data_c_double))