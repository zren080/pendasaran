fahrenheit = float(input('Masukkan Suhu dalam Fahrenheit: '))
celcius = ((5/9) * fahrenheit) - 32
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin)


kelvin = float(input('Masukkan suhu dalam kelvin: '))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit:", fahrenheit)

print("========================")

fahrenheit = float(input("masukan suhu dalam fahrenheit:"))
reamur = ((4/9) * fahrenheit) -32
kelvin = ((5/4) * reamur) +273
print("masukan suhu dalam kelvin:",kelvin,"Kelvin", "type =",type(kelvin))

kelvin = float(input("masukan suhu dalam kelvin:"))
reamur = ((4/5) * kelvin) -273
fahrenheit = ((9/4) * reamur) +32
print("masukan suhu dalam kelvin:",fahrenheit, "Fahrenheit", "type =",type(fahrenheit))