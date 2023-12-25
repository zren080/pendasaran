# dictonary

nama2 = {
    'zr':'zren',
    'rf':'refi',
    'rn':'rani',
    'jf':'jefri'
}
#print(nama2)

# cara mengcopy yang salah
# cara copy dictonary itu sam dengan list
nama2['zr'] = 'zeni'
print(nama2)

nama_copy = nama2.copy()
print(f'copy = {nama_copy}')

# pop diconary berdasarkan (key)
# pop itu mentransfer dictonary yang berdasarkan (key)
data_refi = nama_copy.pop('rf') 
print(f'data refi = {data_refi}\n')
print(f'nama sekarang = {nama_copy}\n')

# pop berdasrkan items (key) & (value)
# popitem itu mentransfer yang terakhir
data_pop_items = nama_copy.popitem()
print(f'data pop = {data_pop_items}\n')
print(f'nama sekarang = {nama_copy}\n')




