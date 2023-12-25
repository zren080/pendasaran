# Operasi Aritmatika

a = 10
b = 3

# operasi tambah (+)

hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan(-)

hasil = a - b
print(a,'-',b,'=',hasil)

# operasi pengalian (*)

hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian (/)

hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen/pangkat (**)

hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus(%) hasil sisa pembagian

hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division (//) hasilnya di bulatkan

hasil = a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, operational precedence

# operasi yang di prioritaskan 
'''
  1.()
  2.eksponen **
  3.perkalian * / % //
  4.pertambahan dan pengurangan + - 


'''
    

x = 5
y = 9
z = 8

hasil = x ** y * z + y / x - y % z // x
print(x,'**',y,'*',z,'+',y,'/',x,'-',y,'%',z,'//',x,'=',hasil)

# cara memakai kurung 
# kurung akan mengambil langkah di dulukan
hasil = y + (z * x)
print(y,'+','(',z,'*',x,')=', hasil)