## Global dan Local scope
# variabel global dia bisa di oerasikan
# global
nama_global = 'zren' # <- ini variabel global

# akses variabel global dalam fungsi
def fungsi():

    print(f'fungsi menampilakn = {nama_global}')

fungsi()

# akses variabel global dalam for loop
for i in range(0,5):
    print(f'loop {i} - {nama_global}')

# pecabangan
if True:
    print(f'if menampilkan {nama_global}')

## varibel local
# variabel local dia berada dan hanya berputar di dalam function. tidak bisa di operasikan
def fungsi2():
    nama_local = 'heni' # <- ini variabel lokal scope

fungsi2()
#print(nama_local)

## penggunaan
# contoh 1: akses varaiavel global
# variabel global tak masalah beradi di bawah asalkan si pemanggil function harus di bawah variabel global
def fungsi3():
    print(f'hello {nama}')

nama = 'geti'
fungsi3()

# contoh 2:merubah variabel global
angka = 0
name = 'unom'

def rubah_angka(nilai_baru,nama_baru):
    global angka # fungsi ini mendapatkan akses global
    global name
    angka = nilai_baru
    name = nama_baru

print(f'sebelum di ubah ={angka,name}')
rubah_angka(6,'venom')
print(f'setelah di ubah ={angka,name}')

# contoh 3:
# variabel global dan local hanya berlaku di fungsi/def
angka9 = 0 

for i in range(0,5): # range tidak sampai pada angka yang di tentukan. contoh hanya sampai pada 4
    angka9 += i
    angka_dummy = 0 

print(angka9)
print(angka_dummy)

if True:
    angka7 = 8
    angka_dummy2 = 6

print(angka7)
print(angka_dummy2)

# berlaku juga untuk while
