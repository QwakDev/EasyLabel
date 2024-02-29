import tkinter as tk
from PIL import Image, ImageTk
import os
import io

isDrawing = False
last_x, last_y = 0,0
pen_color = 'black'
canvas = None
pen_size = 0


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
        #if imgFile != None:
        #    self.image= tk.PhotoImage(file=imgFile)
        #    self.canvas.create_image(height, width, image= self.image)


    
    def start_drawing(self, e):
        global isDrawing,last_x,last_y
        isDrawing = True
        last_x, last_y = e.x, e.y
    def draw(self, e):
        global last_x,last_y, isDrawing

        if isDrawing:
            x, y = e.x, e.y
            #LINE
            self.canvas.create_line((last_x, last_y, x, y), fill=pen_color, width=self.pen_size)
            last_x, last_y = x, y
            #CIRCLE
            r = self.pen_size/2
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r
            self.canvas.create_oval(x0, y0, x1, y1, fill=pen_color)


    def stop_drawing(self, e): #TODO save into temp folder and add return values
        global isDrawing
        isDrawing=False
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

   

    def clear(self):
        return
