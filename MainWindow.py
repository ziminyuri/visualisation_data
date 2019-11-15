from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter.ttk as ttk

from model import Model


class MainWindow(Frame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root
        self.graph = []
        self.analysis_model = []  # Список, где храним модели анализа

        label1 = Label(text="Визуализация №1", height=1, width=15, font='Arial 18')
        label1.place(x=165, y=5)

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_xlim([0, 1000])
        ax.set_ylim([-100, 100])
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=5, y=35)

        label2 = Label(text="Визуализация №2", height=1, width=15, font='Arial 18')
        label2.place(x=700, y=5)
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=35)

        label3 = Label(text="Визуализация №3", height=1, width=15, font='Arial 18')
        label3.place(x=165, y=360)
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=5, y=400)

        label4 = Label(text="Визуализация №4", height=1, width=15, font='Arial 18')
        label4.place(x=700, y=360)
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=400)

        b2 = Button(text="Добавить", command=self.click_button_add_model, width="26", height="2")
        b2.place(x=1120, y=70)

        self.combobox_value = []  # ComboBox графиков для анализа


    def click_button_add(self):
        visualisation = Model()


    # Окно добавления визуализации
    def click_button_add_model(self):
        a = Toplevel()
        a.title('Добавить визуализацию')
        a.geometry('300x200')

        label1 = Label(a, text="Номер визаулизации", height=1, width=18, font='Arial 14')
        label1.place(x=10, y=10)
        self.c1 = ttk.Combobox(a, values=[u"1", u"2", u"3", u"4"], height=4)
        self.c1.place(x=10, y=30)

        label2 = Label(a, text="Визаулизация", height=1, width=12, font='Arial 14')
        label2.place(x=10, y=60)
        self.c2 = ttk.Combobox(a, values=[u"y(x)=kx+b", u"y(x)=-kx+b", u"y(x) = beta * exp^(alpha * i)",
                                             u"y(x) = beta * exp^(alpha * -i)", u"Встроенный рандом"], height=15)
        self.c2.place(x=10, y=80)

        b1 = Button(a, text="Добавить", command=lambda: self.click_button_add(), width="13", height="2")
        b1.place(x=40, y=150)
        b2 = Button(a, text="Закрыть", command=self.click_button_close, width="13", height="2")
        b2.place(x=170, y=150)

        a.grab_set()  # Перехватывает все события происходящие в приложении
        a.focus_set()  # Захватывает и удерживает фокус
