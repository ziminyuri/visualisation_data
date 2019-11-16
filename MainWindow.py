from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

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

        choice_of_visualisation = self.c2.get()

        if choice_of_visualisation == "Круговая диаграмма":
            visualisation.count_parameters_for_pie()

        if choice_of_visualisation == "Столбчатая диаграмма":
            visualisation.count_parameters_for_bar()

        choice_of_place_for_output = int(self.c1.get())

        self.draw(visualisation, choice_of_place_for_output)

    def draw(self, visualisation, choice_of_place_for_output):

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot()

        if visualisation.type_visualisation == 1:
            pieces = visualisation.parameters_for_pie[1]
            owners = visualisation.parameters_for_pie[0]
            custom_colors = ['b', 'r', 'c', 'm', 'y', 'g']
            explode = (0.2, 0, 0, 0, 0, 0)

            # Для отображения без UI
            # plt.pie(pieces, labels=owners, colors=custom_colors)
            # plt.show()

            ax.pie(pieces,
                   labels=owners,
                   colors=custom_colors,
                   shadow=1,
                   startangle=90,
                   explode=explode,
                   autopct='%1.1f%%'
                   )

            ax.axis('equal')
            ax.legend(
                bbox_to_anchor=(0.23, 0.87),
                loc="upper right",
                prop={'size': 8},
                labels=owners)

        if visualisation.type_visualisation == 2:
            name_level_of_education = visualisation.unique_parental_level_of_education.tolist()
            xpos_male = np.arange(len(name_level_of_education)) - 0.2
            xpos_female = np.arange(len(name_level_of_education)) + 0.2

            count_male = visualisation.gender_parental_level_of_education[:6]
            count_female = visualisation.gender_parental_level_of_education[6:]

            ax.bar(xpos_male, count_male, width=0.4, label='Male')
            ax.bar(xpos_female, count_female, width=0.4, label='Female')

            ax.legend(loc='upper right')

            xs = np.arange(len(name_level_of_education)).tolist()
            ax.set_xticks(xs)
            ax.set_xticklabels(name_level_of_education, fontdict={'fontsize': 8}, minor=False)

            y_min = 0
            y_max = np.amax(visualisation.gender_parental_level_of_education) * 1.5
            ax.set_ylim([y_min, y_max])

            fig.autofmt_xdate(rotation=25)

        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()

        if choice_of_place_for_output == 1:
            canvas.get_tk_widget().place(x=5, y=35)

        if choice_of_place_for_output == 2:
            canvas.get_tk_widget().place(x=550, y=35)

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
        self.c2 = ttk.Combobox(a,
                               values=[u"Круговая диаграмма", u"Столбчатая диаграмма", u"y(x) = beta * exp^(alpha * i)",
                                       u"y(x) = beta * exp^(alpha * -i)"], height=15)
        self.c2.place(x=10, y=80)

        b1 = Button(a, text="Добавить", command=lambda: self.click_button_add(), width="13", height="2")
        b1.place(x=40, y=150)
        b2 = Button(a, text="Закрыть", command=self.click_button_close, width="13", height="2")
        b2.place(x=170, y=150)

        a.grab_set()  # Перехватывает все события происходящие в приложении
        a.focus_set()  # Захватывает и удерживает фокус
