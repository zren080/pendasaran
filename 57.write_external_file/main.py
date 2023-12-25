''' Baca link di bawah untuk memahami apa itu "utf-8"
https://www-freecodecamp-org.translate.goog/news/what-is-utf-8-character-encoding/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc
'''

## 1. mode write
'''jika menggunakan mode=write, harus menggunakan encoding='utf-8
agar teks yang di tampilkan sempurna'''
'''override-->menimpa'''
'''jika menggunakan write dia akan menghapus teks yang sebelumnya,
dan akan menuliskan teks baru dari with open yang terakhir '''
with open('data_1.txt','w',encoding='utf-8') as file:
    file.write('halloooo zrennn\n')

with open('data_1.txt','w',encoding='utf-8') as file:
    file.write('grefi ganteng')
    file.write('naniiiiii!!!!!!!')


## 2. mode append
'''mode append hanya menambahkan di belakang saja'''
with open('data_2.txt','a',encoding='utf-8') as file:
    file.write('zren')

with open('data_2.txt','a',encoding='utf-8') as file:
    file.write('yhuuuuuuuuuuuuuuuuu')

with open('data_2.txt','a',encoding='utf-8') as file:
    file.write('memei')


## 3. mode r+
# mode r+ tidak bisa membuat file.txt langsung
'''r+ akan mengganti with open pertama, dan akan mengeprint with open terkahir di line pertamanya
contoh :'''
with open('data_3.txt','w',encoding='utf-8') as file: # 1
    file.write('baris-1')

with open('data_3.txt','r+',encoding='utf-8') as file: # 2
    file.write('baris-2')
    file.write('baris-3')
    file.write('baris-4')
    file.write('baris-5')
    file.write('baris-6')

with open('data_3.txt','r+',encoding='utf-8') as file: # 3 
    file.write('zren') # <- barisan/line ini akan menggantikan teks dari line pertama ->                        
    file.write('baris-7') # -> di with open pertama 
    file.write('baris-8')

with open('data_3.txt','r+',encoding='utf-8') as file: # 3 
    data = file.read()
    print(data)
 
# setelah with open 3 habis di print maka dia akan ke atas ->
# -> dan akan menampilkan with open ke-2 dari line pertama ->
# -> sampai semua line dari with open ke-2 habis 
    
# with open pertama hanya sebagai di timpa oleh with open 2 dan 3

# r+ menggantikan semua satu line





