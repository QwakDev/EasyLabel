import tkinter as tk
from source.pen import DrawingCanvas

window = tk.Tk()
window.title("EasyLoop App")
window.geometry('800x600')

##BUTTONS ACTIONS
def click_btn_okey():
    print("OEY!")
#WINDOW INITK
ok_btn=tk.Button(window,text='OKEY', command=click_btn_okey, height=1,width=5)
ok_btn.place(x=10, y=10)
btn_next = tk.Button(window, text='NEXT')

var1 = tk.IntVar()
text_path = tk.Text(window, height=1, width=50)
text_name = tk.Text(window, height=1, width=25)
text_label= tk.Text(window, height=1, width=25)

Lb1 = tk.Listbox(windowl)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")

c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=True, offvalue=False)
c1.pack()
btn_next.pack()
Lb1.pack()
text_name.pack()
text_label.pack()
text_path.pack()
canvas = DrawingCanvas(window=window,height=600, width=600)

window.mainloop()