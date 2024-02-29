import tkinter as tk
from PIL import Image, ImageTk
import os
import io

isDrawing = False
last_x, last_y = 0,0
pen_color = 'black'
highlight = False
canvas = None
pen_size = 0
drawing_tag = 0


class DrawingCanvas(tk.Canvas):
    def __init__(self,window , height, width, imgFilePath=None, pen_size=2):
        self.window = window
        self.canvas = tk.Canvas(self.window, bg='white', height=height, width=width)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.pen_size = pen_size
        self.image = None
        self.drawingTags = []
        self.drawings = []
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

        if isDrawing:
            x, y = e.x, e.y
            #LINE
            d=self.canvas.create_line((last_x, last_y, x, y), fill=pen_color, width=self.pen_size, tags=str(drawing_tag))

            self.drawings.append((drawing_tag,d))

            last_x, last_y = x, y
            #CIRCLE
            r = self.pen_size/2
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r
            d=self.canvas.create_oval(x0, y0, x1, y1, fill=pen_color, tags=str(drawing_tag))
            self.drawings.append((drawing_tag,d))

    def stop_drawing(self, e): #TODO save into temp folder and add return values
        global isDrawing, drawing_tag
        isDrawing=False
        self.drawingTags.append(drawing_tag)
        #SAVING
        ps = self.canvas.postscript(colormode='color')
        self.image = Image.open(io.BytesIO(ps.encode('utf-8')))
    def get_drawing(self):
        return self.image
    def set_drawing(self, data):
        self.image = None
        self.canvas.delete('all')
        self.canvas.create_image(0,0,image=data, anchor='nw')

    def load_image(self, imgFilePath = None, data = None):
        self.canvas.create_image(image=data)

        return 0

   
    def undo(self):
        if self.drawings == []:
            return
        (_tag, item) = self.drawings.pop()
        l = len(self.drawings)
        self.canvas.delete(item)

        for i in range(l):
            (tag,item) = self.drawings.pop()
            if tag == _tag:
                self.canvas.delete(item)
            else:
                self.drawings.append((tag,item))
                break
    def clear(self):
        return
