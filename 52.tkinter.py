#### GUI --> Graphical User Interface
'''PIP -> Package Installer for Python'''
'''objek itu sama dengan target'''
'''(x-> itu adalah lebar dan y-> itu adalah tinggi)'''
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg='white')
window.geometry('300x200') # geomtery cuman mengatur default nya pixelnya/ukuran
window.resizable(False,False)
window.title('menyapa')

## variable dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    pesan = f'welcome {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()},my name is zren.saya akan pergi main'
    showinfo(title='Selamat Datang',message=pesan)


### input frame
input_frame = ttk.Frame(window)
## penempatan ada 3-> (Grid,Pack,Place)
input_frame.pack(padx=10,pady=10,fill='x',expand=True)

## komponen-komponen

##1. label nama
# nama depan
nama_depan_label = ttk.Label(input_frame,text='Nama Depan:')
nama_depan_label.pack(padx=10,fill='x',expand=True)
# nama belakang
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,pady=5,fill='x',expand=True)

## 2.entry nama
# nama depan
nama_belakang_label = ttk.Label(input_frame,text='Nama Belakang:')
nama_belakang_label.pack(padx=10,fill='x',expand=True)
# nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,pady=5,fill='x',expand=True)

## 3.tombol
pencet = ttk.Button(input_frame,text='Pencet',command=tombol_click)
pencet.pack(fill='x',expand=True,pady=5,padx=10)

## main loop
window.mainloop()