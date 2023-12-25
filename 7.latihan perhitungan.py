# PROGRAM LATIHAN PERHITUNGAN 

# program perpindahan celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPRATUR\n")

celcius = float(input("Masukan Suhu Dalam Celcius: "))
print("suhu dalam celcius",celcius,"Celcius", "type =",type(celcius))

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur",reamur,"Reamur","type =",type(reamur)) 

# fahrenheit
fahrenheit = ((9/5)) * celcius + 32
print("suhu dalam fahrenheit", fahrenheit, "Fahrenheit" "type =", type(fahrenheit))

# kelvin
kelvin = celcius + 273  
print("suhu dalam kelvin",kelvin,"Kelvin", "type =", type(kelvin))