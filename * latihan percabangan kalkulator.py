# LATIHAN KALKULATOR

print(20*'=')
print('KALKULATOR SEDERHANA')
print(20*'=')

angka_1 = float(input('masukan angka :'))
operator = input('operator (/,+,-,*)')
angka_2 = float(input('masukan angka :'))

# PERCABANGAN

if operator == "+":
    hasil = angka_1 + angka_2
    print(f'hasilnya adalah {hasil}') 
elif operator == '/ ':
    hasil = angka_1 / angka_2
    print(f'hasilnya adalah {hasil}') 
elif operator == '*':
    hasil = angka_1 * angka_2
    print(f'hasilnya adalah {hasil}') 
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'hasilnya adalah {hasil}')
else:
    print('salahhh wwwoiiiiiii!!!!')

print('terima saja kembalian nya')