from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json

DATA_FILE = "data_hanghoa.json"
mang_hang_hoa = [] #tương ứng với nội dung file data_hanghoa.json


def mh_quan_ly_hang_hoa(mh_cha):
    mh_con = Toplevel(mh_cha)
    mh_con.title("Quản lý Hàng hóa")
    mh_con.geometry("1000x400")
    
    # Chia FRAME
    list_hh_frame = ttk.Frame(mh_con)
    list_button_frame = ttk.Frame(mh_con)
    input_hh_frame = ttk.Frame(mh_con)
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
        '''Đọc dữ liệu từ file data_hanghoa.json và gán cho biến mảng các hàng hóa dạng list []'''
        global mang_hang_hoa
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as myfile:            
                mang_hang_hoa = json.load(myfile)
        except:
            messagebox.showwarning(title="Lỗi", message="Lỗi đọc file")
            mang_hang_hoa = []

            
    def luu_du_lieu():
        '''Lưu dữ liệu hàng hóa từ biến mảng các hàng hóa xuống file data_hanghoa.json'''
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as myfile:
                json.dump(mang_hang_hoa, myfile, indent = 4)
        except:
            messagebox.showwarning(title="Lỗi", message="Lỗi lưu file")

            
    def tim_hang_hoa_theo_ma(id):
        """Tìm hàng hóa dựa vào mã hàng hóa, trả về hàng hóa tìm được dạng dict hoặc None."""
        for item in mang_hang_hoa:
            if item["ma_hh"] == id:
                return item
        
        return None


    def hien_thi_danh_sach_hang_hoa():
        """Cập nhật lưới"""
        clear_tree_view(tree)
        if len(mang_hang_hoa) == 0:
            doc_du_lieu()        
        for item in mang_hang_hoa:
            tree.insert(
                parent='', index='end',
                values=(item['ma_hh'], item['ten_hh'], item['gia_ban'], item['so_luong'], item['loai'])
            )
                
    def clear_tree_view(mytree):
        for item in mytree.get_children():
            mytree.delete(item)


    def them_hang_hoa():
        #TODO: Check nhập liệu hợp lệ
        obj = {
            "ma_hh": mahh_value.get(),
            "ten_hh": tenhh_value.get(),
            "gia_ban": dongia_value.get(),
            "so_luong": so_luong_value.get(),
            "loai": gia_tri_chon_loai.get()
        }
        global mang_hang_hoa
        
        # Kiểm tra xem mã hàng hóa đã có hay chưa?
        hang_hoa_tim = tim_hang_hoa_theo_ma(obj['ma_hh'])
        
        if hang_hoa_tim is not None:
            messagebox.showwarning(message=f"Đã có hàng hóa mã: {obj['ma_hh']}")
        else:    
            # Nếu chưa thêm ==> cập nhật treeview
            mang_hang_hoa.append(obj)
            # Save file
            luu_du_lieu()
            # Cập nhật treeview
            hien_thi_danh_sach_hang_hoa()
            messagebox.showinfo(message="Thêm mới thành công!")

    # Định nghĩa hàm xử lý sự kiện chọn và gán
    def xu_ly_chon_hang_hoa(e):
        for i_item in tree.selection():
            selected_item = tree.item(i_item)
            row_value = selected_item["values"]
            
            # Cập nhật thông tin xuống dưới (vùng thông tin)
            mahh_value.set(int(row_value[0]))
            tenhh_value.set(row_value[1])
            dongia_value.set(row_value[2])
            so_luong_value.set(row_value[3])
            gia_tri_chon_loai.set(row_value[4])

            
    def xoa_hang_hoa(mahh):
        # 1.Tìm hàng hóa theo mahh
        hang_hoa_tim_thay = tim_hang_hoa_theo_ma(mahh)
        if hang_hoa_tim_thay is not None:
            # 2. Nếu có thì
            # 2.1 xóa khỏi mang_hang_hoa
            global mang_hang_hoa
            mang_hang_hoa.remove(hang_hoa_tim_thay)
            # 2.2 update treeview
            hien_thi_danh_sach_hang_hoa()
            # 2.3 lưu xuống file
            luu_du_lieu()
        
            
    def rightClickMenu(event):
        # create a popup menu
        rowID = tree.identify('item', event.x, event.y)
        if rowID:
            tree.selection_set(rowID)
            tree.focus_set()
            tree.focus(rowID)
            menu = Menu(tree, tearoff=0)
            menu.add_command(label="Delete", command=lambda: xoa_hang_hoa(mahh_value.get()))
            menu.add_command(label="Clear All", command= lambda: clear_tree_view(tree))
            menu.post(event.x_root, event.y_root)
        else:
            pass

    tree.bind('<<TreeviewSelect>>', xu_ly_chon_hang_hoa)
    tree.bind('<3>', rightClickMenu)


    def xoa_thong_tin_hang_hoa():
        mahh_value.set(0)
        tenhh_value.set('')
        dongia_value.set(0)
        so_luong_value.set(0)
        gia_tri_chon_loai.set('')


    # Dinh nghia widget cho list_button_frame
    Button(list_button_frame, text="Xóa danh sách",
        command= lambda: clear_tree_view(tree)
    ).grid(row=0, column=0, padx=5, pady=5)

    Button(list_button_frame, text="Cập nhật danh sách",
        command= lambda: hien_thi_danh_sach_hang_hoa()
    ).grid(row=0, column=1, padx=5, pady=5)

    Button(list_button_frame, text="Thêm", command=them_hang_hoa).grid(row=0, column=2, padx=5, pady=5)
    Button(list_button_frame, text="Xóa", command=xoa_thong_tin_hang_hoa).grid(row=0, column=3, padx=5, pady=5)
    Button(list_button_frame, text="Cập nhật").grid(row=0, column=4, padx=5, pady=5)

    # Lấy danh sách hàng hóa lúc form chạy
    doc_du_lieu()
    hien_thi_danh_sach_hang_hoa()


    # Thêm widget cho vùng input
    Label(input_hh_frame, text="Mã hàng hóa").grid(row=0, column=0)
    mahh_value = IntVar()
    mahh = Entry(input_hh_frame, textvariable=mahh_value)
    mahh.grid(row=0, column=1)

    Label(input_hh_frame, text="Tên hàng hóa").grid(row=1, column=0)
    tenhh_value = StringVar()
    tenhh = Entry(input_hh_frame, textvariable=tenhh_value)
    tenhh.grid(row=1, column=1)

    Label(input_hh_frame, text="Loại").grid(row=2, column=0)
    gia_tri_chon_loai = StringVar()
    loai = ttk.Combobox(input_hh_frame, textvariable=gia_tri_chon_loai)
    loai.grid(row=2, column=1)
    loai['values'] = ["Laptop", "Điện thoại", "Máy tính bảng", "Tivi", "Tủ lạnh"]


    Label(input_hh_frame, text="Đơn giá").grid(row=3, column=0)
    dongia_value = IntVar()
    dongia = Entry(input_hh_frame, textvariable=dongia_value)
    dongia.grid(row=3, column=1)

    Label(input_hh_frame, text="Số lượng").grid(row=4, column=0)
    so_luong_value = IntVar()
    soluong = Entry(input_hh_frame, textvariable=so_luong_value)
    soluong.grid(row=4, column=1)
    
    mh_con.mainloop()