#  Input user

#  CARA: 1
 
#nama data yang akan di buat

nama = input ("nama: ") 
umur = input ("umur: ")
berat = input ("berat: ")
tinggi = input ("tinggi: ")
nikah = input ("nikah: ")

# casting data

umur = int(umur)
berat= float(berat)
nikah = bool(int(nikah)) #boolean harus di casting dulu dari integer

#menampilkan data
print("data = ",nama,",type =",type(nama)) 
print("data = ",umur,",type =",type(umur))
print("data = ",berat,",type =",type(berat))
print("data = ",tinggi,",type =",type(tinggi))
print("data = ",nikah,",type =",type(nikah))

#   CARA: 2

namakomputer= input ("nama kompu: ")

namakomputer = int(namakomputer)

print("data = ",namakomputer,",type =",type(namakomputer))
