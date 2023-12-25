# operasi kompalasi

# setiap hasil dari opearsi komperasi adalah boolean

# lebih besar(>),lebih kecil(<),lebih besar sama dengan(>=),lebih kecil sama dengan (<=),sama dengan (=),tidak sama dengan (!=), is, is not

# (==) namanya membandingkan

a = 4   # ini namanya asaigment (=)
b = 2
 
# lebih besar dari >
print("==lebih-besar(>)==")

hasil = a > 3
print(a,">",3,"=", hasil)
hasil = b > 3
print(b,">",3,"=", hasil)
hasil = b > 2 #minimal asisgment nya 2.1 , tidak boleh sama
print(b,">",2,"=", hasil) # atau pakai (>=)

# lebih kecil (<)
print("==lebih-kecil(<)==")

hasil = a < 3
print(a,"<",3,"=", hasil)
hasil = b < 3
print(b,"<",3,"=", hasil)
hasil = b < 2 #minimal asisgment nya 2.1 , tidak boleh sama
print(b,"<",2,"=", hasil) # atau pakai (>=)

# lebih kecil (>=)
print("==lebih-besar sama dengan(>=)==")

hasil = a >= 3
print(a,">=",3,"=", hasil)
hasil = b >= 3
print(b,">=",3,"=", hasil)
hasil = b >= 2
print(b,">=",2,"=", hasil) 

# lebih kecil (<=)
print("==lebih-kecil sama dengan(<=)==")

hasil = a <= 3
print(a,"<=",3,"=", hasil)
hasil = b <= 3
print(b,"<=",3,"=", hasil)
hasil = b <= 2
print(b,"<=",2,"=", hasil) 

# lebih kecil (==)
print("==sama-dengan(==)==")

hasil = a == 3 
print(a,"==",3,"=", hasil)
hasil = b == 3
print(b,"==",3,"=", hasil)
hasil = b == 2
print(b,"==",2,"=", hasil) 

# tidak sama dengan(!=)
print("==tidak-sama-dengan(!=)==")

hasil = a != 3
print(a,"!=",3,"=", hasil)
hasil = b != 3
print(b,"!=",3,"=", hasil)
hasil = b != 2
print(b,"!=",2,"=", hasil) 

# 'is' sebagai komparasi objek indentity
print("==objek-identity(is)==")

x = 5 # ini adalah assigment membuat objek
y = 5
print("nilai x =",x,",id =",hex(id(x)))
print("nilai y =",y,",id =",hex(id(y)))
hasil = x is y # akan ada warning "is" with literal
print("x is y,=",hasil) # di sarankan saja hanya membandingkan yang ada nilai

print("==nilai-nya-sama(is)==")

x = 5 # ini adalah assigment membuat objek
y = 5
print("nilai x =",x,",id =",hex(id(x)))
print("nilai y =",y,",id =",hex(id(y)))
hasil = x is y # akan ada warning "is" with literal
print("x is y =",hasil) # di sarankan saja hanya membandingkan yang ada nilai

print("==nilai-nya-yang-beda(is not)==")

x = 5 # ini adalah assigment membuat objek
y = 5
print("nilai x =",x,",id =",hex(id(x)))
print("nilai y =",y,",id =",hex(id(y)))
hasil = x is not y # akan ada warning "is" with literal
print("x is not y =",hasil) # di sarankan saja hanya membandingkan yang ada nilai



