from logging import root
import tkinter as tk
from tkinter import filedialog
import cv2
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pydicom
from pydicom.pixel_data_handlers.util import apply_modality_lut, apply_voi_lut

import numpy as np

class gui:
    def __init__(self):
        self.width = 1024
        self.height = 768
        self.path = None
        self.filename = None
        self.img = None
        self.ax = None
        self.fig = None
        self.canvas = None
        self.canvas_tk = None
        self.slice = None
        self.output_img = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None

        self.root = tk.Tk()
        self.root.title("DICOM Viewer")
        self.root.geometry(f"{self.width}x{self.height}")
        # self.root.resizable(False, False)

        self.btn1 = tk.Button(self.root, text="파일 선택", command=self.choose_path)
        self.btn1.pack()

        self.root.mainloop()

    def choose_path(self):
        self.root.file = filedialog.askopenfile(
            initialdir='path',
            title='select file',
            filetypes=(('dcm files', '*.dcm'), ('all files', '*.*'),
            ('png files', '*.png'),('jpg files', '*.jpg'))
        )
        self.path = self.root.file.name
        self.filename = self.path.split('/')[-1]
        print(self.path)
        if self.path is not None:
            if self.ax is not None:
                self.canvas_tk.destroy()
                self.label1.destroy()
                print("canvas, label1 destroy")
            self.fig = plt.Figure()
            self.ax = self.fig.add_subplot()
            self.img = self.dicom_to_array(self.path)
            self.output_img = self.dicom_windowing(self.slice.WindowCenter, self.slice.WindowWidth)
            self.draw_canvas()

    def dicom_to_array(self, dicom_path):
        self.slice = pydicom.read_file(dicom_path)
        s = int(self.slice.RescaleSlope)
        b = int(self.slice.RescaleIntercept)
        return s * self.slice.pixel_array + b
    
    def dicom_windowing(self, window_center, window_width):
        self.slice.WindowCenter, self.slice.WindowWidth = window_center, window_width
        return apply_voi_lut(apply_modality_lut(self.img, self.slice), self.slice)

    def draw_canvas(self):
        self.ax.set_title(f"{self.filename}")
        self.ax.imshow(self.output_img, cmap='gray')
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas_tk = self.canvas.get_tk_widget()
        self.canvas_tk.pack()
        self.canvas.draw()

        self.label1 = tk.Label(self.root, text=f"Window Center : {self.slice.WindowCenter}, Window Wdith : {self.slice.WindowWidth}")
        self.label1.pack()

        self.canvas_tk.bind("<Button-1>", self.click)
        self.canvas_tk.bind("<B1-Motion>", self.drag)

    def click(self, event):
        self.x0, self.y0 = event.x, event.y
    
    def drag(self, event):
        self.x1 , self.y1 = event.x, event.y
        if self.x0 != self.x1 or self.y0 != self.y1:
            self.canvas_tk.destroy()
            self.label1.destroy()
            window_center, window_width = self.slice.WindowCenter, self.slice.WindowWidth
            window_center += self.x1 - self.x0
            window_width += self.y0 - self.y1
            print(f"window center, window width : {window_center, window_width}")
            self.output_img = self.dicom_windowing(window_center, window_width)
            self.draw_canvas()   

if __name__=='__main__':
    gui()