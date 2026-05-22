import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock By Frosty")
root.geometry("600x280")
root.resizable(False,False)
root.config(bg='black')

# digital_ clock function
def digital_clock():
    current_time = strftime('%H:%M:%S:%p')
    current_date = strftime("%A, %d %B, %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    time_label.after(1000,digital_clock)

title_label = tk.Label(
    root,
    bg='black',
    fg='gold',
    font=('courier',40,'bold'),
    text='Time Dekho Babu'
)
title_label.pack(anchor='center',pady=10)

# time label
time_label = tk.Label(
    root,
    bg='black',
    fg='cyan',
    font=('courier',40,'bold'),
)
time_label.pack(anchor='center', pady=30)

#date + day label
date_label = tk.Label(
    root,
    font=("courier",20,'bold'),
    bg='black',
    fg='cyan'
)
date_label.pack(anchor='center',pady=10)

digital_clock()
root.mainloop()
