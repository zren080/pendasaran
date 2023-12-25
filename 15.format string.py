### format string

## contoh generic

#stirng
nama = 'zren'
str = nama
print(str)

nama = 'zren'
format_str = f"hoik {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka 
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15 # nilainya tidak boleh float
format_str = f"bilangan bulat = {angka:d}" # tidak ada format (:d) kalau pakai float
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" #fungsi (.nilaif): untuk menghilangkan angka setelah nya
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.2f}"
print(format_str)

# menampilkan tanda + atau _
angka_minus = -10
angka_plus = 10.4543
format_minus = f"minus = {angka_minus:d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persentase = f"persen = {persentase:.2%}"
print(format_persentase)

# melakukan opearsi aritmatika di dalam placeolder
harga = 10000
jumlah = 5
fomrat_string = f"harga total = Rp.{harga*jumlah}"
print(fomrat_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)







