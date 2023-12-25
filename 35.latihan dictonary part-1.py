import datetime
import os # fungsi os adalah untuk langsung menjalankan perintah di terminal,contoh:

os.system('clear')

# template data nama
data2 = {
    'nama':'nama',
    'asal':'asal',
    'nik':9845,
    'lahir':datetime.datetime(1111,1,11)
}

#data_nama = {}

print('-'*15+'Masukan Data-Data Anda'+'-'*15)

# membuat dict baru tanpa membuat dic kosong serti di atas,
data_warga =  dict.fromkeys(data2.keys()) # dict (buat dic baru).fromkeys(dari keys)data2 nya keys. contoh di samping <-- 

data_warga['nama'] = input('Masukan Nama :')
data_warga['asal'] = input('Masukan Asal :')
data_warga['nik'] = int(input('Masukan Nik :'))
TAHUN_LAHIR = int(input('Tahun lahir (yyyy):'))
BULAN_LAHIR = int(input('Bulan lahir (1-12):'))
TANGGAL_LAHIR = int(input('Tanggal lahir (1-12):'))
data_warga['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

print(data_warga)
