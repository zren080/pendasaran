data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string 

'''
   1.dengan menggunakan single quote: '...'
   2.dengan menggunakan double quote "..."
'''
#1.
data = 'menggunakan single quote'
print(data)

#2
data = "menggunakan double quote"
print(data)

print('"haloo yo"')

#3 menggunakan tanda (\)
print('hari juma\'at')
print('g\'day, isn\'t it?')

#4 backlash
print('c:\\user\\zren') # harus double backlash

#5 tab 
print('zren\tlain') # \t akan membuat spasi makin jauh

#6 backspace

print('zren\blain') # akan membuat spasi makin dekat

#7 newline
print('akan membuat\nline baru') # LF => line feed => linux, mac os unix
print('akan membuat\rline baru') # CR => carriage return => commodore, acorn, lisp
print('akan membuat\r\nline baru') # CRLF => line feed carriage return => dipakai oleh windows

#8 string literal atau raw

# hati-hati
print('c:\new folder')

#menggukan raw string
print(r'c:\new folder') # menghilangkan semua konfeksi dalam sintax string

#9 multiline literal string

print('''
NAMA : Zren
LOKASI: di sini
''')

# multiline literal string dan raw
print(r'''
NAMA   : Zren
LOKASI : di \sini
WEBSITE: WW.zren.com/newid
''')
      