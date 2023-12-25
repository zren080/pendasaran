import datetime
import os # fungsi os adalah untuk langsung menjalankan perintah di terminal,contoh:
import random
import string

# template data nama
data2 = {
    'nama':'nama',
    'asal':'asal',
    'nik':0,
    'lahir':datetime.datetime(1111,1,11)
}

os.system('clear')

data_nama = {} # dict kosong perguna untuk while

while True:
    
    print('-'*15+'Masukan Data-Data Anda'+'-'*15)
    
    # dict.fromkey adalah metode untuk membuat dictionary baru dengan menggunakan template yang sudah ada
    data_warga = dict.fromkeys(data2.keys()) # dict (buat dic baru).fromkeys(dari keys)data2 nya keys. contoh di samping <--  
    data_warga['nama'] = input('Masukan Nama :')
    data_warga['asal'] = input('Masukan Asal :')
    data_warga['nik'] = int(input('Masukan Nik :'))
    TAHUN_LAHIR = int(input('Tahun lahir (yyyy):'))    
    BULAN_LAHIR = int(input('Bulan lahir (1-12):'))    
    TANGGAL_LAHIR = int(input('Tanggal lahir (1-12):'))    
    data_warga['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)    
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    data_nama.update({KEY: data_warga})
    
    print(f"{'key':<15}{'nama':<15} {'asal':<15} {'nik':<15} {'status':<15}")
    print('_'*75)    
    
    for i in data_nama:
        KEY = i
        
        NAMA = data_nama[KEY]['nama']
        ASAL = data_nama[KEY]['asal']
        NIK = data_nama[KEY]['nik']       
        LAHIR = data_nama[KEY]['lahir'].strftime('%x')

    print(f"{KEY:<15} {NAMA:<15} {ASAL:<15} {NIK:<15} {LAHIR:<15}")

    print('\n')

    islanjut = input('Lanjut atau Berhenti(y/n):')

    if islanjut == 'n':
        break

print('Terima Kasih')













