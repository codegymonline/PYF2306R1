from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json

DATA_FILE = "data_hanghoa.json"
root = Tk()
root.title("Quản lý Hàng hóa")
root.geometry("1000x350")

# Chèn treeview
# Ds cột (key)
columns=('ma_hh', 'ten_hh', 'gia_ban', 'so_luong', 'loai')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('ma_hh', text='Mã hàng hóa')
tree.heading('ten_hh', text='Tên hàng hóa')
tree.heading('gia_ban', text='Đơn giá bán')
tree.heading('so_luong', text='Số lượng')
tree.heading('loai', text='Chủng loại')
tree.pack()

def lay_danh_sach_hang_hoa_tu_file(mytreeview):
    with open(DATA_FILE, "r", encoding="utf-8") as myfile:
        data = json.load(myfile)
        
        for item in data:
            tree.insert(
                parent='', index='end',
                values=(item['ma_hh'], item['ten_hh'], item['gia_ban'], item['so_luong'], item['loai'])
            )

# Lấy danh sách hàng hóa lúc form chạy
lay_danh_sach_hang_hoa_tu_file(tree)
root.mainloop()