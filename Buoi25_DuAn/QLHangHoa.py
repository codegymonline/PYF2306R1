from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json

DATA_FILE = "data_hanghoa.json"
root = Tk()
root.title("Quản lý Hàng hóa")
root.geometry("1000x400")


# Chia FRAME
list_hh_frame = ttk.Frame(root)
list_button_frame = ttk.Frame(root)
input_hh_frame = ttk.Frame(root)
list_hh_frame.grid(row=0, column=0)
list_button_frame.grid(row=1, column=0)
input_hh_frame.grid(row=2, column=0)

# Chèn treeview
# Ds cột (key)
columns=('ma_hh', 'ten_hh', 'gia_ban', 'so_luong', 'loai')
tree = ttk.Treeview(list_hh_frame, columns=columns, show='headings')
tree.heading('ma_hh', text='Mã hàng hóa')
tree.heading('ten_hh', text='Tên hàng hóa')
tree.heading('gia_ban', text='Đơn giá bán')
tree.heading('so_luong', text='Số lượng')
tree.heading('loai', text='Chủng loại')
tree.pack()

def doc_du_lieu():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as myfile:
            return json.load(myfile)
    except:
        return []

def lay_danh_sach_hang_hoa_tu_file(mytreeview, data=None):
    clear_tree_view(tree)
    if data is None:
        data = doc_du_lieu()        
    for item in data:
        mytreeview.insert(
            parent='', index='end',
            values=(item['ma_hh'], item['ten_hh'], item['gia_ban'], item['so_luong'], item['loai'])
        )
            
def clear_tree_view(mytree):
    for item in mytree.get_children():
        mytree.delete(item)


def them_hang_hoa():
    obj = {
        "ma_hh": int(mahh.get()),
        "ten_hh": tenhh.get(),
        "gia_ban": int(dongia.get()),
        "so_luong": int(soluong.get()),
        "loai": loai.get()
    }
    print(obj)
    #Đọc file ==> data dạng dict
    data = doc_du_lieu()       
    # TODO: Kiểm tra xem mã hàng hóa đã có hay chưa?
    # Nếu chưa thêm ==> cập nhật treeview
    data.append(obj)
    # Save file
    # Cập nhật treeview
    lay_danh_sach_hang_hoa_tu_file(tree, data)


# Dinh nghia widget cho list_button_frame
Button(list_button_frame, text="Xóa danh sách",
    command= lambda: clear_tree_view(tree)
).grid(row=0, column=0, padx=5, pady=5)

Button(list_button_frame, text="Lấy danh sách",
       command= lambda: lay_danh_sach_hang_hoa_tu_file(tree)
).grid(row=0, column=1, padx=5, pady=5)

Button(list_button_frame, text="Thêm", command=them_hang_hoa).grid(row=0, column=2, padx=5, pady=5)
Button(list_button_frame, text="Xóa").grid(row=0, column=3, padx=5, pady=5)
Button(list_button_frame, text="Cập nhật").grid(row=0, column=4, padx=5, pady=5)

# Lấy danh sách hàng hóa lúc form chạy
lay_danh_sach_hang_hoa_tu_file(tree)


# Thêm widget cho vùng input
Label(input_hh_frame, text="Mã hàng hóa").grid(row=0, column=0)
mahh = Entry(input_hh_frame)
mahh.grid(row=0, column=1)

Label(input_hh_frame, text="Tên hàng hóa").grid(row=1, column=0)
tenhh = Entry(input_hh_frame)
tenhh.grid(row=1, column=1)

Label(input_hh_frame, text="Loại").grid(row=2, column=0)
loai = Entry(input_hh_frame)
loai.grid(row=2, column=1)

Label(input_hh_frame, text="Đơn giá").grid(row=3, column=0)
dongia = Entry(input_hh_frame)
dongia.grid(row=3, column=1)

Label(input_hh_frame, text="Số lượng").grid(row=4, column=0)
soluong = Entry(input_hh_frame)
soluong.grid(row=4, column=1)


root.mainloop()