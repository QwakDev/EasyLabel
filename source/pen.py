import tkinter as tk
import cv2 as cv
from PIL import Image
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
            self.canvas.create_line((last_x, last_y, x, y), fill=pen_color, width=2)
            last_x, last_y = x, y

    def stop_drawing(self, e): #TODO save into temp folder and add return values
        global isDrawing
        isDrawing=False

        ps = self.canvas.postscript(colormode='color')
        self.image = Image.open(io.BytesIO(ps.encode('utf-8')))
    def get_drawing(self):
        return self.image
    def load_image(self, imgFilePath):

        return 0

   

    def clear(self):
        return
