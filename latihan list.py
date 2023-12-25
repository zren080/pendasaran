## --PROGRAM BUKU--

list_baru = []
while True:
    print('Silahkan Masukan Buku')
    judul = input('judul buku\t:')
    author = input('penulis buku\t:')

    buku_baru = [judul,author]
    list_baru.append(buku_baru)
    #print(list_baru)
    
    print('\nNo.\t| buku\t | penulis')
    print(30*'_')
    for index,buku in enumerate(list_baru):
        print(f'{index+1}\t|{buku[0]}\t |{buku[1]}\t')

    islanjut = input('apakah mau lanjut ?(y/n):')

    if islanjut == 'n':
        break

print('Terima Kasih')
