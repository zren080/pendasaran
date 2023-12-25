# --dictonary--

data_dict = {
    'zn':'zren',
    'rn':'rani',
    'hp':'hupi'
}

panjang_dict = len(data_dict)
print(f'panjang dict ={panjang_dict}')

# mengecek key exist atau tidak
key = 'hp'
chek_key = key in data_dict
print(f'apakah {key} ada di dalam:{chek_key}')

## mengakses value (read) menggunakan get
# kalau menggunakan get hasil yang di masukan jika tidak ada/salah maka get akan membuat itu none
# jika pakai yang biasa maka akan eror
print(data_dict['rn'])
#print(data_dict['qw'])
print(data_dict.get('hp'))
#print(data_dict.get('la'))

## mengupdate data
data_dict['zn'] = 'zreni'
print(data_dict)
data_dict['jl'] = 'jefri'
print(data_dict)
# jika data/key tidak ada maka si update akan di add/di tambahkan
# jika data/key ada maka dia akan mengganti value nya
data_dict.update({'rn':'refi'})
print(data_dict)
data_dict.update({'qer':'qerimol'})
print(data_dict)

# mendelete data dictonary
del data_dict['hp']
print(data_dict)
