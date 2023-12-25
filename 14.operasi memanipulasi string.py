# operator dalam bentuk method

# merubah case dari string

# merubah semua ke upper case
data = 'yooppppppppp'
print('normal ='+ data)
besar = data.upper()
print('upper ='+ besar)

# merubah semua ke lower case
data = 'yooDASDADpppppppp'
print('normal ='+ data)
kecil = data.lower()
print('lower ='+ kecil)

# pnegecekan dengan isX method

# contoh pengecekan lower case
data = 'lop'
data_lower = data.islower() # hasilnya bool
print(data + 'is lower =' + str(data_lower))
data_lower = data.isupper() # hasilnya bool
print(data + 'is upper =' + str(data_lower))

# isalpha() <--- untuk mengecek semuanya huruf
# isalnum() <--- huruf dan angka
# isdecimal() <--- angka saja
# isspace() <--- spasi, tab, newline \n
# istitle() <--- semua kata dimulai dengan huruf besar

# 1. isalpha
nama = 'zren' 
cek_nama = nama.isalpha()
print(nama +' is alpha? '+str(cek_nama))

# 2. isalnum
password = 'zren123' # kalau ada selain huruf dan angka hasilnya akan false
cek_password = password.isalnum()
print(password +' is alnum? '+str(cek_password))
 
# 3. isdecimal
tanggal = '98' # akan false jika ada selain angka
cek_tgl = tanggal.isdecimal()
print(tanggal +' is decimal? '+ str(cek_tgl))

# 4. ispace
spasi = 'kapan pergi'
cek_spasi = spasi.isspace()
print(spasi +' is space? '+ str(cek_spasi))

# 5. istitle
judul = 'It Is Okay Not To Be Orkay' # jika salah satunya kecil akan false
cek_judul = judul.istitle() # hasilnya bool
print(judul +'.is tite?'+ str(cek_judul))

# ngecek komponen startswith() endswith()
cek_start = "ZrenGreenday".startswith('Zren') # dari awal sampai akhir yang di masukkan harus benar
print('start ='+ str(cek_start)) 

cek_end = "zrenn kamhji".endswith('ji') # dair akhir ke awal harus benar
print('end ='+ str(cek_end)) 

# penggabungan komponen join() split()
pisah = ['rumah','saya','pergi']
gabungan = ''.join(pisah)
print(gabungan)

gabungan = 'rumahlolsayalolpergi'
print(gabungan.split(' '))

# alokasi karakter rjust(), ljust(), center()
print(7*'='+ 'data' +'='*7)

kanan = 'kanan'.rjust(10)
panjang = len(kanan)
print('panjang kanan ='+str(panjang))
print("'"+kanan+"'")

kiri = 'kiri'.ljust(10,)
print("'"+kiri+"'")
panjang = len(kiri)
print('panjang kiri ='+str(panjang))

tengah = 'tengah'.center(20,':')
print("'"+tengah+"'")
panjang = len(tengah)
print('panjang tengah ='+str(panjang))

# kebalikannya -> strip()
tengah = tengah.strip(':') # menghilangkan tanda (:)
print("'"+tengah+"'")
