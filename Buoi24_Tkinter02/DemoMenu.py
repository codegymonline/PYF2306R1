"""Demo Menu"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


####################tách file####################
def man_hinh_con(mh_cha):
    mh_con = Toplevel(mh_cha)
    mh_con.geometry("200x200")
    
    Label(mh_con, text="Màn hình con").pack()
    
    mh_con.mainloop()
####################tách file####################

root = Tk()

# Menu tổng
menu_bar = Menu(root)
#nhúng menubar vào màn hình chính
root.config(menu=menu_bar)

# Menu con
menu_file = Menu(menu_bar, tearoff=0)
menu_file.add_command(label='Mở màn hình con', command= lambda: man_hinh_con(root))
menu_file.add_command(label='Open')
menu_file.add_command(label='Save')
menu_file.add_command(label='Close')
menu_file.add_separator()
menu_file.add_command(label='Exit', command=root.destroy)

menu_bar.add_cascade(label="File", menu=menu_file)


root.mainloop()