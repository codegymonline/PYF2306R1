"""Demo treeview"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

main = Tk()
main.geometry("600x350")

mycolumns = ("ma_nv", "ho_ten", "luong") # tuple
tv = ttk.Treeview(main, columns=mycolumns, show='headings')
tv.heading('ma_nv', text="Mã nhân viên")
tv.heading('ho_ten', text="Họ tên nhân viên")
tv.heading('luong', text="Lương")

tv.pack()

# data nhân viên
data_nhan_vien = [
    ('NV001', 'Nguyễn Văn Tèo', 2000),
    ('NV002', 'Nguyễn Lê Tí', 1990),
    ('NV003', 'Nguyễn Sinh Hùng', 1350),
]
# Thêm từng dòng (item) cho treeview
for nhan_vien in data_nhan_vien:
    tv.insert('', END, values=nhan_vien)
    

# Định nghĩa hàm xử lý sự kiện chọn và gán
def xu_ly_chon(e):
    for i_item in tv.selection():
        selected_item = tv.item(i_item)
        row_value = selected_item["values"]
        
        messagebox.showinfo(message=f"{row_value[0]}, {row_value[1]}, {row_value[2]}")

tv.bind('<<TreeviewSelect>>', xu_ly_chon)

main.mainloop()