## witdh and multiline

# Data
nama = "zren zray"
umur = 14
tinggi = 169.4
nomor = 13

# string standard
data_string = f"nama = {nama}, umur = {umur}, tinggi = {tinggi}, nomor = {nomor}"
print(5*'='+'String Standard'+5*'=')
print(data_string)

# string multiline (dengan menggunakan enter, newline ,\n)
data_string = f"nama = {nama}, umur = {umur}, tinggi = {tinggi}, nomor = {nomor}"
print('\n'+5*'='+'String Multiline'+5*'=')
print(data_string)

# mengatur lebar
nama = 'zren'
data_string = f'''
nama   = {nama:>5}
umur   = {umur:>5}
tinggi = {tinggi:>5}
nomor  = {nomor:>5}
'''
print('\n'+5*'='+'String Mengatur Lebar'+5*'=')
print(data_string)
