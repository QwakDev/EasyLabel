import cv2 as cv
import pickle
import tkinter as tk
from source.pen import DrawingCanvas
import source.files as FILE
from source.settings import sets, COLORS, GET_SAVE_sets, READ_sets
import time
import random
import source.IMG_PROCESSING.seperator as SEPARATOR
import source.IMG_PROCESSING.multiplier as MULTIPLIER
import source.view as VIEWS
window = tk.Tk()
SETTINGS = sets()
##VARIABLES
isCkecked_highlight = tk.BooleanVar()
isCkecked_multi = tk.BooleanVar()
saved_num_files = tk.StringVar()
saved_num_files.set(str(0))
##ACTIONS
#BUTTONS, LISTS AND VALUESs

def get_s_path(): return text_s_path.get(1.0, 'end-1c')

def onSelect_listbox_items(e):
    selection = e.widget.curselection()
    if e.widget.get(selection[0]) != '':
        _item_name = e.widget.get(selection[0])
        img = FILE.GetPicture(text_path.get(1.0, 'end-1c')+ str(_item_name)) 
        canvas.set_drawing(img)
        window.mainloop()
    return 0
def onSelect_listbox_label(e):
    selection = e.widget.curselection()
    SETTINGS.highlighter_color = listbox_label.itemcget(selection[0], 'background') # GET COLOR
   # .itemconfig
def btn_next_click():
    global  isCkecked_multi
    if isCkecked_multi.get(): #SAVE MULTIPLE PICTURES 
        path_temp = get_s_path() + 'TEMP_DIR/'
        col_set = []
        for col in COLORS:
            (x, _,_,_) = col
            col_set.append(x)
        Temp_Labels = []
        for n in range(listbox_label.index('end')): 
            b_col = listbox_label.itemcget(n, 'background')
            i = col_set.index(b_col)
            (_,b,g,r) = COLORS[i]
            toSave = "{},{},{},{}\n".format(listbox_label.get(n), b,g,r)
            Temp_Labels.append(toSave)

        FILE.SaveTempLabels(get_s_path(), Temp_Labels) # SAVE LABELS WITH BGR color

        FILE.SaveFile(path_temp, canvas.get_drawing(),label=None, toTemp=True) #SAVE LABELED TEMP_PICTURE
        window.after(20,canvas.clear_labels()) #GET CLEAN PICTURE

        FILE.SaveFile(path_temp + '_', canvas.get_drawing(), label=None, toTemp=True) #SAVE CLEAN TEMP_PICTURE

        items = SEPARATOR.SEPARATE(path_temp)
        for (_lab, _p_img, _p_mask) in items:
            _img = cv.imread(_p_img)
            _mask = cv.imread(_p_mask)
            IMGS = MULTIPLIER.GET_ALL(_img,_mask,sets=SETTINGS)
            FILE.SaveImages(get_s_path(),IMGS,_lab)

    else: # SAVE JUST LABEL AND PICTURE
        window.after(20,canvas.clear_labels()) #GET CLEAN PICTURE
        FILE.SaveFile(get_s_path(), canvas.get_drawing(),listbox_label.get(listbox_label.curselection()), toTemp=False)

    saved_num_files.set(str(FILE.GetNumberOfPictures(get_s_path())))
    window.mainloop()
def btn_add_label_click(): 
    listbox_label.insert(listbox_label.index('end'),text_label.get(1.0, 'end-1c'))
    _index = listbox_label.index('end') - 1
    _color = SETTINGS.get_next_color()
    listbox_label.itemconfig(_index, background = _color)
    text_label.delete(1.0, 'end-1c')
    text_label.insert('end-1c', 'TYPE NEW LABEL' )
def btn_remove_label_click():
    i = listbox_label.curselection()
    canvas.clear_label(listbox_label.itemcget(i, 'background'))
    listbox_label.delete(i)
def btn_save_path_click():
    o = FILE.SetSavingDir(get_s_path())
    global _saved_num_files, saved_num_files
    _saved_num_files = o
    saved_num_files.set(str(_saved_num_files))

    _labels = FILE.GetLabels(get_s_path())
    listbox_label.delete(0, tk.END)
    _n = 1
    for l in _labels[1]:
        if l == '':
            continue
        listbox_label.insert(_n, l)
        _color = SETTINGS.get_next_color()
        listbox_label.itemconfig(_n - 1, background = _color)
        _n = _n + 1
def btn_load_path_click():
    _items = FILE.GetListOfFiles(text_path.get(1.0, 'end-1c'))
    listbox_path.delete(0, tk.END)

    if _items != False:
        _n = 1
        for i in _items:
            if i[-4:].lower() == '.jpg':
                listbox_path.insert(_n, i)
                _n = _n + 1
def btn_undo_click():
    canvas.undo()
def scale_set_pen_size(val):
    SETTINGS.pen_size = int(val)
def btn_highlight_click():
    SETTINGS.isHighlighting = isCkecked_highlight.get()
    return
def btn_multi_click():
    return

    
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
canvas = DrawingCanvas(window=frame_main,height=600, width=600, sets= SETTINGS)
#OPTIONS (BOTTOM PANEL)
#RIGHT_PANEL
frame_path = tk.Frame(frame_right) 
#LIST OF FILES DIR                     
text_path = tk.Text(frame_path, height=1, width=50)
text_path.insert('end-1c', 'TYPE DIR PATH FROM WHERE TO LOAD FILES')
text_path.pack(side='right')
btn_load_path = tk.Button(frame_path,text='LOAD_DIR',command=btn_load_path_click)
btn_load_path.pack(side='left')

listbox_path = tk.Listbox(frame_right, width=70, exportselection=False)  
listbox_path.bind('<<ListboxSelect>>', onSelect_listbox_items)      
frame_path.pack()
listbox_path.pack()
#LIST OF LABELS
frame_label = tk.Frame(frame_right)    
btn_remove_label = tk.Button(frame_label,text='REMOVE_LABEL',command=btn_remove_label_click)
btn_remove_label.pack(side='right')                 
text_label = tk.Text(frame_label, height=1, width=25)
text_label.insert('end-1c', 'TYPE NEW LABEL')
text_label.pack(side='right')
btn_add_label = tk.Button(frame_label,text='ADD_LABEL',command=btn_add_label_click)
btn_add_label.pack(side='left')

listbox_label = tk.Listbox(frame_right, width=70 ,height=4, exportselection=False)
listbox_label.bind('<<ListboxSelect>>', onSelect_listbox_label)      

frame_label.pack()
listbox_label.pack()
#SAVING PATH
frame_s_path = tk.Frame(frame_right)
text_s_path = tk.Text(frame_s_path, height=1, width=50)
text_s_path.insert('end-1c', 'TYPE DIR WHERE TO SAVE FILE')
btn_save_path = tk.Button(frame_s_path,text='SAVE_TO',command=btn_save_path_click)

text_s_path.pack(side='right')
btn_save_path.pack(side='left')
frame_s_path.pack()
#OPTIONS
frame_pen = tk.Frame(frame_right)
checkbox_multi = tk.Checkbutton(frame_pen, text='MULTI_LABEL',variable=isCkecked_multi, command= btn_multi_click)
checkbox_highlight = tk.Checkbutton(frame_pen, text='HIGHLIGHT',variable=isCkecked_highlight, command= btn_highlight_click)
scale_pen_size = tk.Scale(frame_pen, orient='horizontal', from_=3, to=40,command=scale_set_pen_size)
btn_undo = tk.Button(frame_pen, text='UNDO', command=btn_undo_click)

frame_pen.pack()
checkbox_highlight.pack(side='left')
checkbox_multi.pack(side='left')
btn_undo.pack(side='left')
scale_pen_size.pack(side='left')


#SAVE BUTTON
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



#MENU BAR
def popup_MUL_eff():
    VIEWS.SHOW_IMG_MUL_effects(window,SETTINGS)
    return
def popup_MUL_def():
    VIEWS.SHOW_IMG_MUL_deform(window,SETTINGS)
    return
def popup_MUL_col():
    VIEWS.SHOW_IMG_MUL_color(window,SETTINGS)
    return
def popup_MUL_slices():
    VIEWS.SHOW_IMG_MUL_slices(window,SETTINGS)
    return
def popup_MUL_rot():
    VIEWS.SHOW_IMG_MUL_rotate(window, SETTINGS)
    return
def save_SETTINGS():
    global SETTINGS
    #SAVE
    path = tk.filedialog.asksaveasfilename(confirmoverwrite=False, defaultextension='.pkl')
    with open(path, 'wb') as out:
        data = GET_SAVE_sets(SETTINGS)
        pickle.dump(data, out, pickle.HIGHEST_PROTOCOL)
    return
def load_SETTINGS():
    global SETTINGS
    path = tk.filedialog.askopenfilename(filetypes=[('save files','*.pkl')])
    data = None
    with open(path, 'rb') as d:
        data = pickle.load(d)
    SETTINGS = READ_sets(data)
    return
menubar = tk.Menu(window)

MUL_Menu = tk.Menu(menubar, tearoff=0)
MUL_Menu.add_command(label="IMG_MUL_color",command=popup_MUL_col)
MUL_Menu.add_command(label="IMG_MUL_effects", command=popup_MUL_eff)
MUL_Menu.add_command(label="IMG_MUL_rotate", command=popup_MUL_rot)
MUL_Menu.add_command(label="IMG_MUL_deform", command=popup_MUL_def)
MUL_Menu.add_command(label="IMG_MUL_slices", command=popup_MUL_slices)
menubar.add_cascade(label="MULTIPLIER", menu=MUL_Menu)

SAVE_SETS_Menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="SAVE_SETTINGS", command=save_SETTINGS)
LOAD_SETS_Menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="LOAD_SETTINGS", command=load_SETTINGS)

window.config(menu=menubar)
#DEBUGGGGGG
def btn_debug_click():
    return

#DEBUG
btn_debug = tk.Button(frame_options,text='DEBUG',command=btn_debug_click)
btn_debug.pack(side='left')
#END OF DEBUUUG
window.mainloop()


