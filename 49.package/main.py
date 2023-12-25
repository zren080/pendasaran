# __pyacache__ adalah yang berfungsi untuk mempercepat mengimport program
import time

t_star = time.time()

# 1
import package.matematika
# 2
from package import matematika
# menggunakan as
from package.matematika import kali as perkalian


hasil_tambah = package.matematika.tambah(4,5,5,7)
print(f"hasil dari package tambah = {hasil_tambah}")

hasil_pangkat = matematika.pangkat(2)
print(f"hasil dari package pangkat = {hasil_pangkat(10)}")

hasil_kali = perkalian(4)
print(f"hasil dari perkalian = {hasil_kali}")

t_end = time.time()
print(f"hasil kecepatan = {t_star - t_end}")