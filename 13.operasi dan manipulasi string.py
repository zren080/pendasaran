# operasi dan manipulasi string

# 1.menyambung string (concatenate)
nama_pertama = 'zren'
nama_tengah = 'L'
nama_akhir  = 'heay'

nama_lengkap = nama_pertama+' '+nama_tengah+' '+nama_akhir # kalau mau berjarak harus di kasih tanda kutip dulu, lalu di dalam tanda kutip kasih spasi
print(nama_lengkap)

# 2. menghitung panjang string/menghitung ada berapa huruf yang di hasilkan
panjang = len(nama_lengkap)
print('panjang dari '+ nama_lengkap +' = '+ str(panjang))

# 3. operator untuk string

# mengecek apakah ada character atau string di
d = 'z'
status = d in nama_lengkap
print(d+' ada di '+ nama_lengkap +' = '+ str(status))

d = 'y'
status = d in nama_lengkap
print(d+' ada di '+ nama_lengkap +' = '+ str(status))

d = 'S'
status = d not in nama_lengkap # kebalikan dari in
print(d+' ada di '+ nama_lengkap +' = '+ str(status))

# 5. mengulang string
print('lop'*10)
print(10*'lop')

#6. indexing
print('index ke-0 :' + nama_lengkap[0])
print('index ke-1 :' + nama_lengkap[1])
print('index ke-7 :' + nama_lengkap[7])
print('index ke-(-9) :' + nama_lengkap[-9])
print('index ke-(-3) :' + nama_lengkap[-3])
print('index ke-[0:5] :'+ nama_lengkap [0:6])
print('index ke-[2,5] :'+ nama_lengkap [2:6])
print('index ke-[0,2,4,6,8,10] :'+ nama_lengkap [0:10:2]) # di locantan 2 string

#7. item paling kecil
print('paling kecil :'+ min(nama_lengkap))
#8. item paling besar
print('paling kecil :'+ max(nama_lengkap))

#9. ascii_code 
ascii_code = ord(' ')
print('ASCII code untuk spasi adalah:'+ str(ascii_code))
data = 117
print('char untuk ASCII 117 adalah:'+ chr(data))

#10.operator dalam bentuk method

data = "akun gue kena hackkk!!"
jumlah = data.count('u')
print('jumlah data pada u :'+ data +' = '+ str(jumlah))
