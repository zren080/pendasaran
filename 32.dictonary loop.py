# looping dictonary

data_dict = {
    'zn':'zren',
    'rn':'rani',
    'hp':'hupi',
    'rf':'refi'
}
print(data_dict)

# looping first try 
for i in data_dict: # yang keluar hanya key
    print(i)

## operator untuk mengambil item / iterabel
# ada 2 cara mengambil value

# 1
keys = data_dict.keys()
print(keys)

for key in data_dict.keys():
    print(data_dict.get(key)) # kalau ngambil key tingal buat print(key)

# 2
values = data_dict.values()
print(values)

for value in data_dict.values():
    print(value)

# kalau menggunakan items kita bisa mengambil keduanya (key) & (values) untuk di for loop atau dll
# ini cara mengambil kedua nya 
items = data_dict.items()
print(items)

for i in data_dict.items():
    print(i)

for key,value in data_dict.items():
    print(f'key = {key},value = {value}')




