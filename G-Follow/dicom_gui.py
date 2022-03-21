from logging import root
import tkinter as tk
from tkinter import filedialog
import cv2
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

        self.root = tk.Tk()
        self.root.title("DICOM Viewer")
        self.root.geometry(f"{self.width}x{self.height}")
        # self.root.resizable(False, False)

        btn1 = tk.Button(self.root, text="파일 선택", command=self.choose_path)
        btn1.pack()

        self.root.mainloop()

    def choose_path(self):
        self.root.file = filedialog.askopenfile(
            initialdir='path',
            title='select file',
            filetypes=(('all files', '*.*'), ('dcm files', '*.dcm'),
            ('png files', '*.png'),('jpg files', '*.jpg'))
        )
        self.path = self.root.file.name
        self.filename = self.path.split('/')[-1]
        print(self.path)
        if self.path is not None:
            if self.ax is not None:
                # self.ax.clear()
                self.canvas_tk.destroy()
                print("canvas destroy")
            self.fig = plt.Figure()
            self.ax = self.fig.add_subplot()
            self.img = cv2.imread(self.path)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

            self.ax.set_title(f"{self.filename}")
            self.ax.imshow(self.img)
            self.ax.set_xticks([])
            self.ax.set_yticks([])

            self.canvas = FigureCanvasTkAgg(self.fig, self.root)
            self.canvas_tk = self.canvas.get_tk_widget()
            self.canvas_tk.pack()
            self.canvas.draw()

if __name__=='__main__':
    gui()