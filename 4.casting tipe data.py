#meruabah tpe data ke tipe data yang lain
#merubah tipe data :integer,bolean,string,tuple,float
# data_int data_bool data_str data_tuple

print("====INTEGER====")
# INTEGER

data_int = 0
print("data = ", data_int,   "type = ",type(data_int))

data_float= float(data_int)
data_str  = str  (data_int)
data_bool = bool (data_int) #akan false jika nilai int=0
print("data = ", data_float, "type = ",type(data_float))
print("data = ", data_str,   "type = ",type(data_str))
print("data = ", data_bool,  "type = ",type(data_bool))

print("====FLOAT====")
#FLOAT

data_float = 8.9
print("data = ", data_float, "type = ",type(data_float))

data_int  = int  (data_float) #angka akan di bulatkan ke bawah
data_str  = str  (data_float)
data_bool = bool (data_float) #fakse jika nilai float=0
print("data = ", data_int,   "type = ",type(data_int))
print("data = ", data_str,   "type = ",type(data_str))
print("data = ", data_bool,  "type = ",type(data_bool))

print("====BOOLEAN====")
#BOOLEAN

data_bool = False
print("data = ", data_bool, "type = ",type(data_bool))

data_int  = int(data_bool)
data_str  = str  (data_bool)
data_float= float (data_bool)
print("data = ", data_int,   "type = ",type(data_int))
print("data = ", data_str,   "type = ",type(data_str))
print("data = ", data_float,  "type = ",type(data_float))

print("====STRING====")
#STRING

data_str = "joni"
print("data = ", data_str, "type = ",type(data_str))

data_int  = int   (data_str) #string harus angka
data_bool = bool  (data_str) #string harus angka
data_float= float (data_str) #false jika string kosong
print("data = ", data_int,   "type = ",type(data_int))
print("data = ", data_bool,   "type = ",type(data_bool))
print("data = ", data_float,  "type = ",type(data_float))


