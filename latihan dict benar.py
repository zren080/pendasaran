import datetime
import random
import string
import os # fungsi os adalah untuk langsung menjalankan perintah di terminal,contoh:

# template data nama
data2 = {
    'nama':'nama',
    'asal':'asal',
    'nik':0,
    'lahir':datetime.datetime(1111,1,11)
}

os.system('clear')

data_warga = {} # dict perguna untuk while 

while True:
    print(f"{'masukan data anda':^25}")
    
    # dict.fromkey adalah metode untuk membuat dictionary baru dengan menggunakan template yang sudah ada
    data = dict.fromkeys(data2.keys()) # dict (buat dic baru).fromkeys(dari keys)data2 nya keys. contoh di samping <--
    data['nama'] = input('Nama :')
    data['asal'] = input('Asal :')
    data['nik'] = int(input('Nik :'))
    TAHUN = int(input('Tahun Lahir :'))
    BULAN = int(input('Bulan Lahir :'))
    TANGGAL = int(input('Tanggal Lahir :'))
    data['lahir']= datetime.datetime(TAHUN,BULAN,TANGGAL)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6))) # 6 itu adalah random string nya ada 6 huruf
    data_warga.update({KEY:data})
    data_warga.update({KEY:data})

    print(f"{'key':<15} {'nama':<15} {'asal':<15} {'nik':<15} {'lahir':<15}")
    print('_'*75)
    
    for data in (data_warga):
        KEY = data
        
        NAMA = data_warga[KEY]['nama']
        ASASL = data_warga[KEY]['asal']
        NIK = data_warga[KEY]['nik']
        LAHIR = data_warga[KEY]['lahir'].strftime('%x')
        
        print(f"{KEY:<10} {NAMA:<10} {ASASL:<10} {NIK:<10} {LAHIR:<10}")
        
    print('\n')

    lanjut = input('masih mau lanjut?(y/n)')
        
    if lanjut == 'n':

            break
            
print('Terima Kasih Telah Mengisi Data')
        
    
    
    
    





