import tkinter as tk
from PIL import Image, ImageTk
import os
import io
import copy


from source.settings import sets 

isDrawing = False
last_x, last_y = 0,0
canvas = None
drawing_tag = 0
isHighlighting = False


class DrawingCanvas(tk.Canvas):
    def __init__(self,window , height, width, imgFilePath=None, sets=None):
        self.window = window
        self.canvas = tk.Canvas(self.window, bg='white', height=height, width=width)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.image = None
        self.drawingTags = []
        self.drawings = []
        self.SETTINGS = sets
        

        #if imgFile != None:
        #    self.image= tk.PhotoImage(file=imgFile)
        #    self.canvas.create_image(height, width, image= self.image)


    
    def start_drawing(self, e):
        global isDrawing,last_x,last_y, drawing_tag
        isDrawing = True
        drawing_tag = drawing_tag + 1
        last_x, last_y = e.x, e.y
    def draw(self, e):
        global last_x,last_y, isDrawing, drawing_tag
        pen_size = self.SETTINGS.get_pen_size()
        pen_color = self.SETTINGS.get_pen_color()

        if isDrawing:
            x, y = e.x, e.y
            #LINE
            d=self.canvas.create_line((last_x, last_y, x, y), fill=pen_color, width=pen_size, tags=str(drawing_tag))

            self.drawings.append((drawing_tag, d, pen_color))

            last_x, last_y = x, y
            #CIRCLE
            r = pen_size/2
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r
            d=self.canvas.create_oval(x0, y0, x1, y1, fill=pen_color, outline=pen_color, tags=str(drawing_tag))
            self.drawings.append((drawing_tag, d, pen_color))
    def stop_drawing(self, e): #TODO save into temp folder and add return values
        global isDrawing, drawing_tag
        isDrawing=False
        self.drawingTags.append(drawing_tag)
        #SAVING
        self.update_drawing()
    def update_drawing(self):
        ps = self.canvas.postscript(colormode='color')
        self.image = Image.open(io.BytesIO(ps.encode('utf-8')))
    def get_drawing(self):
        return self.image
    def set_drawing(self, data):
        self.image = None
        self.canvas.delete('all')
        self.canvas.create_image(0,0,image=data, anchor='nw')
    def get_labeled_drawing(self, label_color):
        current = self.image
        current_canvas = self.canvas
        copy_canvas = copy.copy(self.canvas)
        col_list = []
        #label_set = set(self.drawings)
        
        for _, __, col in self.drawings:
            col_list.append(col)
        col_set = set(col_list)
        for x in col_set:
            if x != 'black' and x != label_color:
                self.clear_label(x)
        copyOut = copy.copy(self.image)
        self.canvas = copy_canvas
        return copyOut
    def load_image(self, imgFilePath = None, data = None):
        self.canvas.create_image(image=data)

        return 0
    def undo(self):
        if self.drawings == []:
            return
        (_tag, item, _) = self.drawings.pop()
        l = len(self.drawings)
        self.canvas.delete(item)
        for i in range(l):
            (tag,item, _) = self.drawings.pop()
            if tag == _tag:
                self.canvas.delete(item)
            else:
                self.drawings.append((tag,item, _))
                break
        self.update_drawing()
    def clear_label(self, color):
        newDrawings = self.drawings.copy()
        if self.drawings == []:
            return
        n = (len(self.drawings))
        for x in range(n):
            i = self.drawings[x]
            (tag,item, col) = i
            if col == color:
                self.canvas.delete(item)
                newDrawings.remove(i)
        self.drawings = newDrawings
        self.update_drawing()
    def clear_labels(self):
        col_list = []
        #label_set = set(self.drawings)
        
        for _, __, col in self.drawings:
            if col != 'black':
                col_list.append(col)
        col_set = set(col_list)
        for x in col_set:
            self.clear_label(x)

    def clear(self):
        return
