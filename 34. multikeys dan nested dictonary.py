import datetime

data_1 = {
    'nama':'zren',
    'asal':'kp.lalang',
    'nik':'1924438312',
    'pelajar':False,
    'lahir':datetime.datetime(2005,8,21)
}

data_2 = {
    'nama':'reni',
    'asal':'durian tarung',
    'nik':'34541212',
    'pelajar':True,
    'lahir':datetime.datetime(2003,5,12)
}

data_3 = {
    'nama':'jefri',
    'asal':'ampang',
    'nik':'98351585',
    'pelajar':False,
    'lahir':datetime.datetime(1999,9,11)
}

data_nama = {
    '001':data_1,
    '002':data_2,
    '003':data_3
}
# tanda kutip string tidak boleh sama dengan tanda kutip di dalam dictonary
# contoh di bawah
print(f"{'no.p':<15} {'nama':<15} {'asal':<15} {'nik':<15} {'pelajar':<15} {'lahir':<15}")
print('_'*75)

for i in data_nama:
    key = i

    nama = data_nama[i] ['nama']
    asal = data_nama[i] ['asal']
    nik = data_nama[i] ['nik']
    pelajar = data_nama[i] ['pelajar']
    lahir = data_nama[i] ['lahir'].strftime('%x')

    print(f"{key:<15} {nama:<15} {asal:<15} {nik:<15} {pelajar:<15} {lahir:<15}")

# fungsi geser
# :> artinya (stirng bergeser sesuai nilai,dan spasi nya itu adalah string)
# yang artinya semua total spasi dan string sesuai dengan nilai geser, contoh:
#data = ('lllll') di sini l nya ada 5
#print(f'{data:>15}') nanti akan bergeser ke kanan sebanyak 10, karna 5 nya sudah di ambil oleh data
#data = ('llllllllll')




















