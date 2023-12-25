# as adalah mengubah nama function terseraah author
# as bisa juga di pakai mengubah module
from matematika import tambah as pertambahan
from matematika import kali as perkalian
from matematika import pangkat as memangkat
#jika mengubah module tidak bisa memakai as yang telah di ubah dari from.contoh:
# math.pertambahan() itu tidak bisa di pakai karna itu dari from. harus sesuai dari asalnya
import matematika as math

hasil_tambah = math.pertambahan(4,3,4,9)
print(f'ini adalah tambah = {hasil_tambah}')

hasil_kali = perkalian(8,2,4)
print(f'ini adalah kali = {hasil_kali}')

hasi_pangkat = memangkat(2)
print(f'ini adalah pangkat = {hasi_pangkat(4)}')