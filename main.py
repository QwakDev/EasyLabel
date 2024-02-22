import tkinter as tk

window = tk.Tk()
window.title("EasyLoop App")
window.geometry('800x600')

##BUTTONS ACTIONS
def click_btn_okey():
    print("OKEY!")
#WINDOW INIT
ok_btn=tk.Button(window,text='OKEY', command=click_btn_okey)
ok_btn.place(x=10, y=10)

var1 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=True, offvalue=False)
c1.pack()
canvas = tk.Canvas(window, bg='black', height=600, width=600)




canvas.pack()
window.mainloop()