import numpy as np
'''isi dari numpy kebanyakan matriks/ list nested/ list 2 dimensi
yang berati akan erorr jika hanya membri satu objek harus di nested kan contoh seperti bawah:'''


#contoh list biasa
list_a  = [1,2,3,4,5]

# vector array vertikal(m)
vector_a = np.array([1,2,3,4,5])

'''perbedaan nya:
list tidak bisa di artimatika kan, dan vector sebaliknya
dan hasil print dari vector lebih bersih dari pada list'''
#print(f'list_a :{list_a**2}') <- ini akan gagal
print(f'vector_a : {vector_a**2}')

# vector array vertikal(n)
vertikal_n = [[2],
            [4],
            [9],
            [10]]

vertikal_array = np.array(vertikal_n)
print(vertikal_array)


'''matrix itu sama dengan vector horizontal perbedaan nya si matrix memakai tuple di dalamnya, sedangkan si vector tidak pakai'''
matrix_b = np.array([(4,2),(5,3)]) 
print(f'matrix_b :{matrix_b}')
print(f'matrix_b^2 :{matrix_b*2}')


# mengubah menjadi 0
zeros_c = np.zeros((2,2))
print(f'zeros_c :{zeros_c}')

# mengubah menjadi 1
ones_d = np.ones((2,2))
print(f'ones_d :{ones_d}')


jumlah = matrix_b + matrix_b*2 - ones_d
print(f'hasil penjnumlahan = {jumlah}')