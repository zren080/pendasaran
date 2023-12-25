# kalau pakai from tidak perlu memakai module langsung tambahkan saja fucntion. contoh:
# matematika.tambah() menjadi tambah()
# bintang adalah mengimport semua function dari matematika
from matematika import tambah,kali,pangkat # disarankan memakai inin karna lebih jelas asalnya
from matematika import *


hasil_tambah = tambah(4,3,4,9)
print(f'ini adalah tambah = {hasil_tambah}')

hasil_kali = kali(8,2,4)
print(f'ini adalah kali = {hasil_kali}')

hasi_pangkat = pangkat(2)
print(f'ini adalah pangkat = {hasi_pangkat(4)}')