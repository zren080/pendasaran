# memahami standar library python
# contoh objek = {} () []
# contoh elemen = isi di dalam objek -> (2)
'''objek itu sama dengan ciri-ciri'''
import datetime

data_waktu = datetime.datetime.now()
print(f'datetime now : {data_waktu}')
print(f'tahun : {data_waktu.year}')
print(f'hari : {data_waktu.strftime("%A")}')

'''biar lebih mudah'''
from collections import Counter

data = ['j','h','a','a','f','e','f','f']
data_count = Counter(data)
print(f'jumlah a = {data_count["a"]}')

'''membaca file_text.txt'''
'''file_text nya harus berbarengan dengan file python kita'''

import io

file = io.open('cara memindahkan file ke cloud drive ubuntu.txt','r')
print(file.read())