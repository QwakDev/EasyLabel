import tkinter as tk
from source.pen import DrawingCanvas
import source.files as FILE


window = tk.Tk()
##VARIABLES
_saved_num_files = 0
saved_num_files = tk.StringVar()
saved_num_files.set(str(_saved_num_files))
##ACTIONS
#BUTTONS, LISTS AND VALUES
def btn_next_click(): #TODO : ADD FILE SAVING METHOD
    global _saved_num_files, saved_num_files
    _saved_num_files = _saved_num_files + 1
    saved_num_files.set(str(_saved_num_files))
    print(_saved_num_files)
     
    window.mainloop()
def btn_add_label_click():
    listbox_label.insert(4,text_label.get(1.0, 'end-1c'))
    text_label.delete(1.0, 'end-1c')
    text_label.insert('end-1c', 'TYPE NEW LABEL' )
def btn_remove_label_click():
    i = listbox_label.curselection()
    listbox_label.delete(i)
def btn_save_path_click(): #TODO check if path isValid and change textbox to SAVING TO: or PLEASE WINPUT VALID PATH
    o = FILE.SetSavingDir(text_s_path.get(1.0, 'end-1c'))
    print(o)
def btn_load_path_click():#TODO LOAD FILES PATHS FROM DIR and add them to the list
    _items = FILE.GetListOfFiles(text_path.get(1.0, 'end-1c'))
    listbox_path.delete(0, tk.END)
    if _items != False:
        _n = 1
        for i in _items:
            listbox_path.insert(_n, i)
            _n = _n + 1

##VIEWS
window.title("EasyLoop App")
window.geometry('1200x650')

frame_options = tk.Frame(window)
frame_right = tk.Frame(window)
frame_main = tk.Frame(window)

frame_right.pack(side='right')
frame_main.pack(side='top')
frame_options.pack(side='bottom')
#MAIN
canvas = DrawingCanvas(window=frame_main,height=600, width=600)
#OPTIONS (BOTTOM PANEL)
#RIGHT_PANEL
frame_path = tk.Frame(frame_right)                      
text_path = tk.Text(frame_path, height=1, width=50)
text_path.insert('end-1c', 'TYPE DIR PATH FROM WHERE TO LOAD FILES')
text_path.pack(side='right')
btn_load_path = tk.Button(frame_path,text='LOAD_DIR',command=btn_load_path_click)
btn_load_path.pack(side='left')

listbox_path = tk.Listbox(frame_right, width=70)        
frame_path.pack()
listbox_path.pack()

frame_label = tk.Frame(frame_right)    
btn_remove_label = tk.Button(frame_label,text='REMOVE_LABEL',command=btn_remove_label_click)
btn_remove_label.pack(side='right')                 
text_label = tk.Text(frame_label, height=1, width=25)
text_label.insert('end-1c', 'TYPE NEW LABEL')
text_label.pack(side='right')
btn_add_label = tk.Button(frame_label,text='ADD_LABEL',command=btn_add_label_click)
btn_add_label.pack(side='left')

listbox_label = tk.Listbox(frame_right, width=70 ,height=4, )

frame_label.pack()
listbox_label.pack()

frame_s_path = tk.Frame(frame_right)
text_s_path = tk.Text(frame_s_path, height=1, width=50)
text_s_path.insert('end-1c', 'TYPE DIR WHERE TO SAVE FILE')
btn_save_path = tk.Button(frame_s_path,text='SAVE_TO',command=btn_save_path_click)

text_s_path.pack(side='right')
btn_save_path.pack(side='left')
frame_s_path.pack()

frame_pen = tk.Frame(frame_right)
checkbox_auto_fill = tk.Checkbutton(frame_pen, text='AUTO_FILL')
checkbox_highlight = tk.Checkbutton(frame_pen, text='HIGHLIGHT')
checkbox_smooth = tk.Checkbutton(frame_pen, text='SMOOTH')
scale_pen_size = tk.Scale(frame_pen, orient='horizontal')

frame_pen.pack()
checkbox_highlight.pack(side='left')
checkbox_auto_fill.pack(side='left')
checkbox_smooth.pack(side='left')
scale_pen_size.pack(side='left')



frame_s= tk.Frame(frame_right)
btn_next = tk.Button(frame_s, text='SAVE_AND_NEXT',command=btn_next_click)
checkbox_auto_s = tk.Checkbutton(frame_s, text='AUTO_SAVE')
label_s_num_text = tk.Label(frame_s, text='NUM_FILES_SAVED: ' )
label_s_num = tk.Label(frame_s, textvariable= str(saved_num_files) )

frame_s.pack()
label_s_num.pack(side='right')
label_s_num_text.pack(side='right')
btn_next.pack(side='left')
checkbox_auto_s.pack(side='right')


window.mainloop()