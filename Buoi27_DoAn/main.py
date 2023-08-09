"""Demo Menu"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from MHQLHangHoa import mh_quan_ly_hang_hoa

root = Tk()
root.title("Quản lý Hàng hóa")
root.geometry("400x300")

# Menu tổng
menu_bar = Menu(root)
#nhúng menubar vào màn hình chính
root.config(menu=menu_bar)

# Menu con
menu_file = Menu(menu_bar, tearoff=0)
menu_file.add_command(label='Quản lý loại')
menu_file.add_command(label='Quản lý hàng hóa', command= lambda: mh_quan_ly_hang_hoa(root))
menu_file.add_separator()
menu_file.add_command(label='Thoát', command=root.destroy)

menu_bar.add_cascade(label="Chức năng", menu=menu_file)


root.mainloop()