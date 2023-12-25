
data_kosong = []
while True:
    print('-'*5+'Masukan Data-Data Anda'+'-'*5)
    data1 = input('Nama :') 
    data2 = input('Asal :') 
    data3 = int(input('Nik :'))
    data4 = input('Anda Masih Sekolah ? (y/n):')
    
    if data4 == 'y':
        print('pelajar')
        break
    if data4 == 'n':
        print('masyarakat')
        break
    
    pass
    
    data_neested = [data1,data2,data3,data4]

    data_kosong.append(data_neested)

    print(f"{'no':<15}{'nama':<15} {'asal':<15} {'nik':<15} {'status':<15}")
    print('_'*75)
    
    

        
    islanjut = input('Lanjut atau Berhenti(y/n):')

    if islanjut == 'n':
        break

print('Terima Kasih')

## capitalize
##dia akan mengubah awalan yang kecil mendajadi besar,contoh:
# nama = "zren"
# print(nama.capitalize())