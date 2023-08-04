"""Định nghĩa hàng hóa"""
class HangHoa:
    def __init__(self, ma, ten, gia, so_luong, loai):
        self.ma_hh = ma
        self.ten_hh = ten
        self.gia_ban = gia
        self.so_luong = so_luong
        self.loai = loai
    
    def __str__(self):
        return f"{self.ma_hh}, {self.ten_hh} ({self.loai}: {self.gia_ban})"