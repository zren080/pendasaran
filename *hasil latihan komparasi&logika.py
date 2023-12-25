# -----0++++++5------8++++++11------

inputuser = float(input('masukan angka yang bernilai\nlebih dari 0\ndan\nkurang dari 5\natau\nlebih dari 8\ndan\nkurang dari 11\n:'))

isLebihDari = (inputuser > 0)
print('isLebihDari 0=',isLebihDari)

isKurangDari = (inputuser < 5)
print('isKurangDari 5=',isKurangDari)

isLebihDari = (inputuser > 8)
print('isLebihDari 8=',isLebihDari)

isKurangDari = (inputuser < 11)
print('isKurangDari 11=',isKurangDari)

isCorrect = isLebihDari and isKurangDari or isLebihDari and isKurangDari
print('angka yang anda masukan:',isCorrect)


# ++++0-----5++++++8------11+++++
print('\n',20*'=','\n')

inputuser = float(input('masukan angka yang bernilai\nkurang dari 0\natau\nlebih dari 5\ndan\nkurang dari 8\atau\nlebih dari 11\n:'))

isKurangDari = (inputuser < 0)
print('isKurangDari 0=',isKurangDari)

isLebihDari = (inputuser > 5)
print('isLebihDari 5=',isLebihDari)

isKurangDari = (inputuser < 8)
print('isKurangDari 8=',isKurangDari)

isLebihDari = (inputuser > 11)
print('isLebihDari =',isLebihDari)

isCorrect = isKurangDari or isLebihDari and isKurangDari or isLebihDari
print('angka yang anda masukan:',isCorrect)
