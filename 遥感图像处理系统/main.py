import tkinter as tk
import os
from PIL import Image, ImageTk
import cv2
from skimage import util
from tkinter import filedialog
import numpy as np


class Img_tif:
    def read(self, flie_path):
        self.img_cv = cv2.imread(flie_path, cv2.IMREAD_GRAYSCALE)
        self.img_data = Image.fromarray(self.img_cv)
        self.img = Image.fromarray(util.img_as_ubyte(self.img_data))
        self.name = os.path.basename(flie_path)


imgs = []


def on_quickLoad():
    for i in range(1, 11):
        flie_path = ".\Images\B"+str(i)+".TIF"
        image = cv2.imread(flie_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            img = Img_tif()
            img.read(flie_path)
            imgs.append(img)
    Init_list()


# 主窗口


class Main_win:
    closed_fun = None

    def show(self):
        self.win.mainloop()

    def destroy(self):
        try:
            self.closed_fun()
        except:
            pass
        self.win.destroy()

    def on_color(self):
        # 彩色合成界面
        title_name = "彩色合成"
        self.top = tk.Toplevel(self.win)
        self.top.protocol('WM_DELETE_WINDOW', self.top.destroy)
        self.top.geometry("480x320")
        self.top.title(title_name)

        self.color_label0 = tk.Label(self.top)
        self.color_label0.place(relx=0.10, rely=0.10,
                                relheight=0.1, relwidth=0.15)
        self.color_label0.configure(
            text='R图层', anchor='center', justify='center')

        self.color_label1 = tk.Label(self.top)
        self.color_label1.place(relx=0.30, rely=0.10,
                                relheight=0.1, relwidth=0.15)
        self.color_label1.configure(
            text='G图层', anchor='center', justify='center')

        self.color_label2 = tk.Label(self.top)
        self.color_label2.place(relx=0.50, rely=0.10,
                                relheight=0.1, relwidth=0.15)
        self.color_label2.configure(
            text='B图层', anchor='center', justify='center')

        self.color_label3 = tk.Label(self.top)
        self.color_label3.place(relx=0.1, rely=0.5, relheight=0.1)
        self.color_label3.configure(
            text='此处的选择数为选择图层在图层列表中自上而下的次序', anchor='center', justify='center')

        self.color_spb0 = tk.Spinbox(self.top, from_=1, to=self.list.size()+1)
        self.color_spb0.place(relx=0.10, rely=0.20,
                              relheight=0.1, relwidth=0.15)

        self.color_spb1 = tk.Spinbox(self.top, from_=1, to=self.list.size()+1)
        self.color_spb1.place(relx=0.30, rely=0.20,
                              relheight=0.1, relwidth=0.15)

        self.color_spb2 = tk.Spinbox(self.top, from_=1, to=self.list.size()+1)
        self.color_spb2.place(relx=0.50, rely=0.20,
                              relheight=0.1, relwidth=0.15)

        # 合成键
        self.color_btn = tk.Button(self.top, command=on_color)
        self.color_btn.place(relx=0.80, rely=0.9,
                             relheight=0.05, relwidth=0.07)
        self.color_btn.configure(text='合成')

    def on_ndvi(self):
        # NDVI界面
        title_name = "NDVI"
        self.top = tk.Toplevel(self.win)
        self.top.protocol('WM_DELETE_WINDOW', self.top.destroy)
        self.top.geometry("480x320")
        self.top.title(title_name)

        self.ndvi_label0 = tk.Label(self.top)
        self.ndvi_label0.place(relx=0.10, rely=0.10,
                               relheight=0.1, relwidth=0.15)
        self.ndvi_label0.configure(
            text='R图层', anchor='center', justify='center')

        self.ndvi_label1 = tk.Label(self.top)
        self.ndvi_label1.place(relx=0.30, rely=0.10,
                               relheight=0.1, relwidth=0.15)
        self.ndvi_label1.configure(
            text='nir图层', anchor='center', justify='center')

        self.ndvi_label3 = tk.Label(self.top)
        self.ndvi_label3.place(relx=0.1, rely=0.5, relheight=0.1)
        self.ndvi_label3.configure(
            text='此处的选择数为选择图层在图层列表中自上而下的次序', anchor='center', justify='center')

        self.ndvi_spb0 = tk.Spinbox(self.top, from_=1, to=self.list.size()+1)
        self.ndvi_spb0.place(relx=0.10, rely=0.20,
                             relheight=0.1, relwidth=0.15)

        self.ndvi_spb1 = tk.Spinbox(self.top, from_=1, to=self.list.size()+1)
        self.ndvi_spb1.place(relx=0.30, rely=0.20,
                             relheight=0.1, relwidth=0.15)

        # 计算键
        self.ndvi_btn = tk.Button(self.top, command=on_ndvi)
        self.ndvi_btn.place(relx=0.80, rely=0.9,
                            relheight=0.05, relwidth=0.07)
        self.ndvi_btn.configure(text='计算')

    def __init__(self):
        # 主界面外框
        title_name = "遥感图像处理程序 made by rainshabow"
        self.win = tk.Tk()
        self.win.protocol('WM_DELETE_WINDOW', self.destroy)
        self.win.geometry("1600x900")
        self.win.title(title_name)

        # 图层列表
        self.list = tk.Listbox(self.win)
        self.list.place(relx=0.80, rely=0.10,
                        relheight=0.78, relwidth=0.15)

        self.label1 = tk.Label(self.win)
        self.label1.place(relx=0.80, rely=0.05,
                          relheight=0.05, relwidth=0.15)
        self.label1.configure(text='图层列表', anchor='center', justify='center')

        # 创建画布
        self.canvas = tk.Canvas(self.win, width=400, height=300, bg='white')
        self.canvas.place(relx=0.02, rely=0.06, relheight=0.89, relwidth=0.75)

        # 读取键
        self.btn_read = tk.Button(self.win)
        self.btn_read.place(relx=0.80, rely=0.9,
                            relheight=0.05, relwidth=0.04)
        self.btn_read.configure(text='读取')

        # 删除键
        self.btn_delete = tk.Button(self.win)
        self.btn_delete.place(relx=0.85, rely=0.9,
                              relheight=0.05, relwidth=0.04)
        self.btn_delete.configure(text='删除')

        # 快速读取键
        self.btn_QL = tk.Button(self.win)
        self.btn_QL.place(relx=0.9, rely=0.9,
                          relheight=0.05, relwidth=0.04)
        self.btn_QL.configure(text='快速读取')

        # 尺度条
        self.scale = tk.Scale(self.win, from_=1.0, to=20.0,
                              resolution=0.1, orient=tk.HORIZONTAL)
        self.scale.place(relx=0.02, rely=0.01,
                         relheight=0.05, relwidth=0.1)

        # 彩色合成键
        self.btn_color = tk.Button(self.win, command=self.on_color)
        self.btn_color.place(relx=0.14, rely=0.01,
                             relheight=0.05, relwidth=0.1)
        self.btn_color.configure(text='彩色合成')

        # 中值滤波键
        self.btn_median = tk.Button(self.win)
        self.btn_median.place(relx=0.26, rely=0.01,
                              relheight=0.05, relwidth=0.1)
        self.btn_median.configure(text='中值滤波')

        # Roberts边缘识别键
        self.btn_Roberts = tk.Button(self.win)
        self.btn_Roberts.place(relx=0.38, rely=0.01,
                               relheight=0.05, relwidth=0.1)
        self.btn_Roberts.configure(text='Roberts边缘识别')

        # otsu算法键
        self.btn_otsu = tk.Button(self.win)
        self.btn_otsu.place(relx=0.50, rely=0.01,
                            relheight=0.05, relwidth=0.1)
        self.btn_otsu.configure(text='otsu阈值分割')

        # ndvi键
        self.btn_ndvi = tk.Button(self.win, command=self.on_ndvi)
        self.btn_ndvi.place(relx=0.62, rely=0.01,
                            relheight=0.05, relwidth=0.1)
        self.btn_ndvi.configure(text='计算ndvi')

        # 其他
        self.img_container = None
        self.img_tk = None
        self.current_img = Img_tif()


main_win = Main_win()


def on_select(event):
    widget = event.widget
    selection = widget.curselection()
    if selection:
        index = selection[0]
        value = widget.get(index)
        print(f'Selected: {value}')
        Insert_image(index)

    global move_x, move_y
    move_x = 0.0
    move_y = 0.0
    main_win.scale.set(1)


def on_delete():
    selection = main_win.list.curselection()
    index = selection[0]
    value = main_win.list.get(index)
    for i in range(len(imgs)):
        if (imgs[i].name == f'{value}'):
            imgs.pop(i)
            break
    main_win.list.delete(selection)
    # 清空之前的图像
    main_win.canvas.delete("all")
    print(len(imgs))


def on_read():
    flie_path = filedialog.askopenfilename()
    img = Img_tif()
    img.read(flie_path)
    imgs.append(img)
    main_win.list.insert('end', img.name)


def on_scale(event):
    scale = main_win.scale.get()
    Width, Height = main_win.current_img.img_data.size

    Width = int(Width / 10 * scale)
    Height = int(Height / 10 * scale)

    main_win.img_tk = ImageTk.PhotoImage(
        main_win.current_img.img.resize((Width, Height), Image.LANCZOS))
    # 清空之前的图像
    main_win.canvas.delete("all")

    # 在画布上显示图像
    main_win.img_container = main_win.canvas.create_image(
        0, 0, anchor="nw", image=main_win.img_tk)

    global move_x, move_y
    scale_value = main_win.scale.get()
    main_win.canvas.move(main_win.img_container, move_x *
                         scale_value, move_y*scale_value)


def on_mouse_press(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y


def on_mouse_drag(event):
    global last_x, last_y, move_x, move_y
    scale_value = main_win.scale.get()
    dx = event.x - last_x
    dy = event.y - last_y
    move_x += dx / scale_value
    move_y += dy / scale_value
    main_win.canvas.move(main_win.img_container, dx, dy)
    last_x = event.x
    last_y = event.y


def on_mouse_wheel(event):
    scale_value = main_win.scale.get()
    scale_value += event.delta * 0.001
    print(event.delta)
    main_win.scale.set(scale_value)


def on_color():
    numR = int(main_win.color_spb0.get())
    numG = int(main_win.color_spb1.get())
    numB = int(main_win.color_spb2.get())
    RGB_img = Img_tif()
    RGB_img.img_cv = cv2.merge(
        [imgs[numB-1].img_cv, imgs[numG-1].img_cv, imgs[numR-1].img_cv])
    RGB_img.img_data = Image.fromarray(RGB_img.img_cv)
    RGB_img.img = Image.fromarray(util.img_as_ubyte(RGB_img.img_data))
    RGB_img.name = str(numR) + str(numG) + str(numB) + ".TIF"
    imgs.append(RGB_img)
    main_win.list.insert('end', RGB_img.name)
    cv2.imwrite(RGB_img.name, RGB_img.img_cv)


def on_median():
    selection = main_win.list.curselection()
    index = selection[0]
    img_median = Img_tif()
    img_median.img_cv = cv2.medianBlur(imgs[index].img_cv, 5)
    img_median.img_data = Image.fromarray(img_median.img_cv)
    img_median.img = Image.fromarray(util.img_as_ubyte(img_median.img_data))
    img_median.name = 'B' + str(index + 1) + '_median.TIF'
    imgs.append(img_median)
    main_win.list.insert('end', img_median.name)
    cv2.imwrite(img_median.name, img_median.img_cv)


def on_Roberts():
    selection = main_win.list.curselection()
    index = selection[0]
    img_Roberts = Img_tif()
    # 定义 Roberts 算子的卷积核
    kernelx = np.array([[1, 0],
                        [0, -1]], dtype=np.float32)
    kernely = np.array([[0, 1],
                        [-1, 0]], dtype=np.float32)

    # 使用 filter2D 函数应用 Roberts 算子
    robertsx = cv2.filter2D(imgs[index].img_cv, cv2.CV_32F, kernelx)
    robertsy = cv2.filter2D(imgs[index].img_cv, cv2.CV_32F, kernely)

    # 结果取绝对值
    roberts_absx = np.abs(robertsx)
    roberts_absy = np.abs(robertsy)

    # 将增强后的图像进行合并
    img_Roberts.img_cv = cv2.addWeighted(
        roberts_absx, 0.5, roberts_absy, 0.5, 0)
    # 将图像像素值归一化到 0 到 255 的范围
    img_Roberts.img_cv = np.where(
        img_Roberts.img_cv == 0, 0, 255).astype(np.uint8)
    img_Roberts.img_data = Image.fromarray(img_Roberts.img_cv)
    img_Roberts.img = Image.fromarray(util.img_as_ubyte(img_Roberts.img_data))
    img_Roberts.name = 'B' + str(index + 1) + '_Roberts.TIF'
    imgs.append(img_Roberts)
    main_win.list.insert('end', img_Roberts.name)
    cv2.imwrite(img_Roberts.name, img_Roberts.img_cv)


def on_otsu():
    selection = main_win.list.curselection()
    index = selection[0]
    # 使用Otsu法进行阈值分割
    image = imgs[index].img_cv
    height, width = image.shape
    # 对边缘的黑框进行一定处理,减轻对图像的影响
    image[image == 0] = image[int(height/2)][int(width/2)]
    ret, otsu_thresh = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img_otsu = Img_tif()
    img_otsu.img_cv = np.where(
        otsu_thresh == 0, 0, 255).astype(np.uint8)
    img_otsu.img_data = Image.fromarray(img_otsu.img_cv)
    img_otsu.img = Image.fromarray(util.img_as_ubyte(img_otsu.img_data))
    img_otsu.name = 'B' + str(index + 1) + '_otsu.TIF'
    imgs.append(img_otsu)
    main_win.list.insert('end', img_otsu.name)
    cv2.imwrite(img_otsu.name, img_otsu.img_cv)


def on_ndvi():
    numR = int(main_win.ndvi_spb0.get())
    numNir = int(main_win.ndvi_spb1.get())

    img_ndvi = Img_tif()
    img_ndvi.img_cv = (imgs[numR - 1].img_cv - imgs[numNir - 1].img_cv) * 256 / \
        (imgs[numR - 1].img_cv + imgs[numNir - 1].img_cv)
    img_ndvi.img_data = Image.fromarray(img_ndvi.img_cv)
    img_ndvi.img = img_ndvi.img_data
    img_ndvi.name = str(numR) + str(numNir) + '_ndvi.TIF'
    imgs.append(img_ndvi)
    main_win.list.insert('end', img_ndvi.name)
    cv2.imwrite(img_ndvi.name, img_ndvi.img_cv)


def Init_list():
    for i in range(len(imgs)):
        main_win.list.insert('end', imgs[i].name)
        print(imgs[i].name)


def Insert_image(index=0):
    main_win.current_img = imgs[index]

    Width, Height = main_win.current_img.img_data.size

    Width = int(Width/10)
    Height = int(Height/10)

    main_win.img_tk = ImageTk.PhotoImage(
        main_win.current_img.img.resize((Width, Height), Image.LANCZOS))
    # 清空之前的图像
    main_win.canvas.delete("all")

    # 在画布上显示图像
    main_win.img_container = main_win.canvas.create_image(
        0, 0, anchor="nw", image=main_win.img_tk)

    print("Image displayed successfully")


def Init():
    main_win.list.bind('<<ListboxSelect>>', on_select)
    main_win.btn_delete.configure(command=on_delete)
    main_win.btn_read.configure(command=on_read)
    main_win.btn_median.configure(command=on_median)
    main_win.btn_Roberts.configure(command=on_Roberts)
    main_win.btn_otsu.configure(command=on_otsu)
    main_win.scale.configure(command=on_scale)
    main_win.btn_QL.configure(command=on_quickLoad)

    # 绑定鼠标事件
    main_win.canvas.bind('<ButtonPress-1>', on_mouse_press)
    main_win.canvas.bind('<B1-Motion>', on_mouse_drag)
    main_win.win.bind("<MouseWheel>", on_mouse_wheel)


if __name__ == '__main__':
    Init()
    main_win.show()
