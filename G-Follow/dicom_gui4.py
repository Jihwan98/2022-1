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
        self.hu_img = None
        self.ax = None
        self.fig = None
        self.canvas = None
        self.canvas_tk = None
        self.slice = None
        self.window_center = None
        self.window_width = None
        self.img = None
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
            self.hu_img = self.dicom_to_array(self.path)
            self.img = self.dicom_windowing(self.hu_img, self.window_center, self.window_width)
            self.draw_canvas()

    def dicom_to_array(self, dicom_path):
        self.slice = pydicom.read_file(dicom_path)
        self.window_center, self.window_width = self.slice.WindowCenter, self.slice.WindowWidth
        s = int(self.slice.RescaleSlope)
        b = int(self.slice.RescaleIntercept)
        return s * self.slice.pixel_array + b
    
    def dicom_windowing(self, image, window_center, window_width):
        img_min = window_center - window_width / 2
        img_max = window_center + window_width / 2
        window_img = np.clip(image, img_min, img_max)
        return window_img

    def draw_canvas(self):
        if self.canvas_tk:
            self.canvas_tk.destroy()
            self.label1.destroy()
            self.label2.destroy()
            self.btn2.destroy()
            self.btn3.destroy()
            self.btn4.destroy()
            self.window1.destroy()
            self.window2.destroy()
            self.label3.destroy()
            self.label4.destroy()
            self.label5.destroy()
            self.label6.destroy()
            self.input_text1.destroy()
            self.input_text2.destroy()

        self.ax.set_title(f"{self.filename}")
        self.ax.imshow(self.img, cmap='gray')
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas_tk = self.canvas.get_tk_widget()
        self.canvas_tk.pack()
        self.canvas.draw()

        self.label1 = tk.Label(self.root, text=f"Window Center : {self.window_center}, Window Wdith : {self.window_width}")
        self.label1.pack()
        self.label2 = tk.Label(self.root)
        self.label2.pack()
        self.btn2 = tk.Button(self.label2, text="영역 선택", command=self.make_roi, width=10)
        self.btn2.pack(side='left', padx=20)
        self.btn3 = tk.Button(self.label2, text="초기화", command=self.reset, width=10)
        self.btn3.pack(side='left')
        
        self.window1 = tk.Label(self.root)
        self.window1.pack()

        self.window2 = tk.Label(self.window1)
        self.window2.pack(side='left')

        self.label3 = tk.Label(self.window2)
        self.label3.pack()
        self.label4 = tk.Label(self.label3, text="Window Center")
        self.input_text1 = tk.Entry(self.label3, width=10)
        self.input_text1.insert(0, self.window_center)
        self.label4.pack(side='left')
        self.input_text1.pack(side='left')
        
        self.label5 = tk.Label(self.window2)
        self.label5.pack()
        self.label6 = tk.Label(self.label5, text="Window Width")
        self.input_text2 = tk.Entry(self.label5, width=10)
        self.input_text2.insert(0, self.window_width)
        self.label6.pack(side='left')
        self.input_text2.pack(side='left')

        self.btn4 = tk.Button(self.window1, text='적용', command=self.confirm_input, height=2)
        self.btn4.pack(side='left')


    def select_roi(self, img):
        x, y, w, h = cv2.selectROI('img', img, False)
        if w and h:
            print(f'x:{x: 3d}, y:{y: 3d}, w:{w: 3d}, h:{h: 3d}')
            roi = img[y:y+h, x:x+w]
            cv2.imshow('roi', roi)
            cv2.moveWindow('roi', 0,0)
            # cv2.imwrite(save_path,roi)

        cv2.imshow('img',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return x, y, w, h

    def roi_window(self, hu_img, percent=0):
        float_hu_img = (hu_img - np.min(hu_img)) / (np.max(hu_img) - np.min(hu_img))
        float_hu_img = np.expand_dims(float_hu_img, axis=2)
        x, y, w, h = self.select_roi(float_hu_img)
        roi_img = hu_img[y:y+h, x:x+w]
        hist, bins = np.histogram(roi_img.flatten(), int(np.max(roi_img) - np.min(roi_img) + 1), [np.min(roi_img), np.max(roi_img) + 1])
        cdf = hist.cumsum()
        percent = percent

        if cdf[0] < cdf[-1] * percent / 100:
            clip_min = np.min(roi_img) + np.where(cdf < cdf[-1] * percent / 100)[0][-1]
        else:
            clip_min = np.min(roi_img)
        if cdf[-1] > cdf[-1] * (100-percent)/100:
            clip_max = np.min(roi_img) + np.where(cdf > cdf[-1] * (100-percent)/100)[0][0]
        else:
            clip_max = np.max(roi_img)

        window_center = (clip_max + clip_min) / 2
        window_width = (clip_max - clip_min)
        print(f"window_center : {window_center}, window_width : {window_width}")
        return window_center, window_width
    
    def make_roi(self, percent=0):
        self.window_center, self.window_width = self.roi_window(self.hu_img, percent=percent)
        self.change_window(self.window_center, self.window_width)

    def change_window(self, window_center, window_width):
        self.window_center = window_center
        self.window_width = window_width
        self.img = self.dicom_windowing(self.hu_img, self.window_center, self.window_width)
            
        self.canvas_tk.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.window1.destroy()
        self.window2.destroy()
        self.label3.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.label6.destroy()
        self.input_text1.destroy()
        self.input_text2.destroy()
        self.draw_canvas()

    def confirm_input(self):
        window_center = float(self.input_text1.get())
        window_width = float(self.input_text2.get())
        self.change_window(window_center, window_width)

    def reset(self):
        self.window_center, self.window_width = self.slice.WindowCenter, self.slice.WindowWidth
        self.change_window(self.window_center, self.window_width)


if __name__=='__main__':
    gui()