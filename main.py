import tkinter as tk
from tkinter import *

window = tk.Tk()

frame = Frame(window)
frame.pack(side='top', expand=True, fill='both')

lab = Label(frame, text='sdklfjsdjf')


def next():
    print('Test button')
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()



label_title = Label(frame,text="Введите домашний адрес",fg="white",bg="grey",width=50,height=2)
label_title.grid(row=0, column=0, padx=10, pady=5)

label_name = Label(frame,text="Имя:")
label_name.grid(row=1, column=0, padx=10, pady=5)

entry_name = Entry(frame,fg='black',bg='white',width = 50)
entry_name.grid(row=1, column=1, padx=10, pady=5)

label_lastname = Label(frame,text="Фамилия:")
label_lastname.grid(row=2, column=0, padx=10, pady=5)

entry_lastname = Entry(frame,fg='black',bg='white',width = 50)
entry_lastname.grid(row=2, column=1, padx=10, pady=5)

label_adress = Label(frame,text="Адресс:")
label_adress.grid(row=3, column=0, padx=10, pady=5)

entry_adress = Entry(frame,fg='black',bg='white',width = 50)
entry_adress.grid(row=3, column=1, padx=10, pady=5)

label_country = Label(frame,text="Страна:")
label_country.grid(row=4, column=0, padx=10, pady=5)

entry_country = Entry(frame,fg='black',bg='white',width = 50)
entry_country.grid(row=4, column=1, padx=10, pady=5)

frame.but = Button(frame,text='Нажмите для подтверждения',bg='grey',fg='white',command=next)
frame.but.grid(row=5,column=1, padx=10, pady=5)



frame.pack()
window.mainloop()



