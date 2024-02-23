import tkinter as tk

isDrawing = False
last_x, last_y = 0,0
pen_color = 'black'
canvas = None


class DrawingCanvas(tk.Canvas):
    def __init__(self,window , height, width, img=None, thickness=2):
        self.window = window
        self.canvas = tk.Canvas(self.window, bg='white', height=height, width=width)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

    
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

    def stop_drawing(self, e):
        global isDrawing
        isDrawing=False


   

    def clear(self):
        return
