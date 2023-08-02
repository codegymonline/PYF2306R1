"""Demo ttk combobox"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

main = Tk()
main.geometry("300x250")

ttk.Label(text="Nơi sinh (tỉnh/thành phố)").pack(fill=X)

gia_tri_chon = StringVar()
tinh_thanhpho = ttk.Combobox(main, textvariable=gia_tri_chon)
tinh_thanhpho.pack(fill=X, padx=5, pady=5)
tinh_thanhpho['values'] = ["Hà Nội", "Hồ Chí Minh", "Nha Trang"]

#Định nghĩa hàm xử lý sự liện thay đổi giá trị chọn
def xu_ly_thay_doi(e):
    messagebox.showinfo(message=f"Vừa chọn: {gia_tri_chon.get()}")
    
# Gắn sự kiện cho combox
tinh_thanhpho.bind('<<ComboboxSelected>>', xu_ly_thay_doi)

main.mainloop()