"""
Xây dựng ứng dụng quản lý sinh viên với các chức năng cơ bản sau:
1/ Xem danh mục sinh viên
2/ Thêm sinh viên mới vào danh mục
3/ Cập nhật thông tin của sinh viên trong danh mục
4/ Xóa thông tin sinh viên khỏi danh mục
5/ Tìm kiếm thông tin sinh viên trong danh mục theo từ khóa
6/ Sắp xếp thông tin sinh viên trong danh mục

Thông tin sinh viên gồm: các thuộc tính như mã sinh viên, họ tên, 
    năm sinh, quê quán, chuyên ngành học, lớp
"""
class SinhVien:
    # Thuộc tính (Property)
    ma_sinh_vien: str = ""
    ho_ten: str = ""
    nam_sinh: int = 1900
    gioi_tinh: bool = True # True: Nữ, False: Name
    nganh_hoc: str = None
    diem: float = 0
        
    def __init__(self, ma_sinh_vien, ho_ten, nam_sinh, gioi_tinh, nganh_hoc, diem):
        self.ma_sinh_vien = ma_sinh_vien
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.nganh_hoc = nganh_hoc
        self.diem = diem
        
    def __str__(self): # dùng khi print(obj)
        return f"SV {self.ho_ten}, {self.ma_sinh_vien}, sinh {self.nam_sinh}, {self.diem}"
    
# Demo
# sv1 = SinhVien('1001', 'Test 1', 1990, True, 'CNTT', 29)
# sv2 = SinhVien('1002', 'Test 2', 1999, False, 'KT', 29.9)
# print(sv1)
# print(sv2)

# Định nghĩa lớp danh sách sinh viên
class MangSinhVien:
    danh_sach: list[SinhVien] = []
        
    def xem_danh_sach(self):
        print("____________DANH SÁCH SINH VIÊN___________")
        for sv in self.danh_sach:
            print(sv)
    
    def them_sinh_vien(self):
        print("____________THÊM SINH VIÊN___________")
        ma_so = input("Nhập mã số: ")
        ten = input("Nhập họ tên: ")
        nam = int(input("Năm sinh: "))
        gioi_tinh = True if input("Giới tính: ").lower() == "nữ" else False
        nganh = input("Ngành học:")
        diem = float(input("Nhập điểm: "))
        
        sv_temp = SinhVien(
            ma_sinh_vien=ma_so, ho_ten=ten, nam_sinh=nam, 
            gioi_tinh=gioi_tinh, nganh_hoc=nganh, diem=diem
        )
        self.danh_sach.append(sv_temp)

# Demo listStudent
dssv = MangSinhVien()
dssv.xem_danh_sach()
dssv.them_sinh_vien()
dssv.xem_danh_sach()


def lua_chon():
    chuoi = '''
    1/ Xem danh mục sinh viên
    2/ Thêm sinh viên mới vào danh mục
    3/ Cập nhật thông tin của sinh viên trong danh mục
    4/ Xóa thông tin sinh viên khỏi danh mục
    5/ Tìm kiếm thông tin sinh viên trong danh mục theo từ khóa
    6/ Sắp xếp thông tin sinh viên trong danh mục.    
    '''
    print(chuoi)
    try:
        chon = int(input("""Bạn chọn:"""))
        
        return chon if 1 <= chon <= 6 else 0
    except:
        return 0

# Tạo mảng danh sách sinh viên
# main
# dssv = []
# while lua_chon() != 0:
#     print("TODO")
    
# print("BYE BYE")
