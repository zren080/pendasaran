# data and time

import datetime as dt
#cara melihat tahun,bulan,hari sekarang
#hari_ini = dt.date.today()
#print(hari_ini)
#print(f'harini adalah hari = {hari_ini:%A}')

# memasukan tanggal manual
#tanggal = dt.date(2005,8,21)
#print(tanggal)
#print(f'harini adalah hari = {tanggal:%A}')

# latihan
print("Silahkan masukan tanggal, \n bulan dan tahun lahir anda\n")
tanggal = int(input("Tanggal \t:"))
bulan   = int(input("Bulan \t\t:"))
tahun   = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal) # pemasangan tidak boleh terbalik
print(f'Tanggal lahir anda:{tanggal_lahir}')

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f'Harinya adalah \t:{tanggal_lahir:%A}')
print(f"umur anda adalah : {umur_tahun}tahun, {umur_bulan_sisa}bulan, {umur_hari}")







