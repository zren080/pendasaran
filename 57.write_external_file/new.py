with open('data_4.txt','r+',encoding='utf-8') as file: # 2
    file.write('baris-4')
    file.write('baris-5')

with open('data_4.txt','r+',encoding='utf-8') as file: # 2
    data = file.read()
    print(data)

with open('data_4.txt','r+',encoding='utf-8') as file: # 2
    file.write('bebek')

