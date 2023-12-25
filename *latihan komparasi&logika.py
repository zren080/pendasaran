# membuat gabungan aera rentang dari angka

# ++++++3-------10++++++++

inputuser = float(input('masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:'))

# +++++++3------------
# memeriksa angka kurang dari 3
isKurangDari = (inputuser < 3)
print('isKurangDari 3=',isKurangDari)

# ---------10+++++++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputuser > 10)
print('isLebihDari 10=',isLebihDari)

# ++++++3-------10++++++++
isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukan:', isCorrect)

#-------3+++++++++10---------
# kasusu irisan
print('\n',10*'=','\n')
inputuser = float(input('masukan angka \n lebih dari 3 \n dan \n kurang dari 10; '))

# ------3+++++++++++++++++++++
# lebih dari 3
isLebihDari = inputuser > 3
print('isLebiDari 3 =', isLebihDari)

#+++++++++++10---------------

isKurangDari = inputuser < 10
print('isKurangaDari =',isKurangDari)

#-------3+++++++++10---------
isCorrect = isLebihDari and isKurangDari
print('angka yang anda masukan: ', isCorrect)
