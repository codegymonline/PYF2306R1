from tkinter import *
from tkinter import ttk
from tkinter import messagebox

main = Tk()
main.geometry("300x250")

# Insert code here
ttk.Label(main, text="Chọn size áo").pack(fill=X, padx=5, pady=5)

gia_tri_chon = StringVar()
sizes = {
    'Small' : 'S',
    'Medium': 'M',
    'Large': 'L',
    'Extra Large': 'XL',
    'Extra Extra Large': 'XXL'
}

for (key, value) in sizes.items():
#     messagebox.showinfo(message=f"{key}, {value}")
    ttk.Radiobutton(
        main,
        text=key,
        value=value,
        variable=gia_tri_chon
    ).pack(fill=X, padx=5, pady=5)

def ham_xu_ly_chon():
    messagebox.showinfo(title="Kết quả", message=f"Bạn chọn: {gia_tri_chon.get()}")
    
# nút
ttk.Button(main, text="Kết quả chọn", command=ham_xu_ly_chon).pack()

main.mainloop()