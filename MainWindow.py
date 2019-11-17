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

        # Вставили title
        label1 = Label(text="Визуализация №1", height=1, width=15, font='Arial 18')
        label1.place(x=165, y=5)   # Указали место на окне приложения


        fig = Figure(figsize=(5, 3), dpi=100)   # Инициализирования объект fig класса Figure размером 5 на 3 и плотность 100
        ax = fig.add_subplot(111)               # Инициализиурем subplot ax
        ax.set_xlim([0, 1000])                  # Задаем значение оси х от 0 до 1000
        ax.set_ylim([-100, 100])                # Задаем значение оси у от -100 до 100

        canvas = FigureCanvasTkAgg(fig, master=self.root)  # Включаем в canvas(Tkinter) объект fig
        canvas.draw()                                      # Рисуем canvas
        canvas.get_tk_widget().place(x=5, y=35)            # Указываем местоположение

        label2 = Label(text="Визуализация №2", height=1, width=15, font='Arial 18')
        label2.place(x=700, y=5)
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=35)

        label3 = Label(text="Визуализация №3", height=1, width=15, font='Arial 18')
        label3.place(x=165, y=360)
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(x=5, y=400)

        label4 = Label(text="Визуализация №4", height=1, width=15, font='Arial 18')
        label4.place(x=700, y=360)
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=400)

        # Инициализировали кнопку на экране, при нажатии на кнопку переход к функции click_button_add_model()
        b2 = Button(text="Добавить", command=self.click_button_add_model, width="26", height="2")
        b2.place(x=1120, y=70)          # Указали место на окне

    # Происходит непосредственно добавление модели
    def click_button_add(self, subWindow):
        visualisation = Model()                 # Объявили объект класса Model

        # Вытащили значение визуализации из combobox
        choice_of_visualisation = self.c2.get()

        if choice_of_visualisation == "Круговая диаграмма":
            visualisation.count_parameters_for_pie()    # Расчитываем параметры для круговой диаграммы

        if choice_of_visualisation == "Столбчатая диаграмма":
            visualisation.count_parameters_for_bar()     # Расчитываем параметры для столбчатой диаграммы

        if choice_of_visualisation == "Мультипликативная модель":
            visualisation.count_parameters_multi()      # Расчитываем параметры для мультипликативной модели

        if choice_of_visualisation == "Вложенная круговая диаграмма":
            visualisation.count_parameters_nested_pie()         # Расчитываем параметры для вложенная круговая

        # Вытащили место где отобразить видуализацию из combobox
        choice_of_place_for_output = int(self.c1.get())

        # Отрисовываем модель
        self.draw(visualisation, choice_of_place_for_output)

        # Закрываем окно добавления визализации
        subWindow.destroy()

    def draw(self, visualisation, choice_of_place_for_output):

        fig = Figure(figsize=(5, 3), dpi=100) # Инициализирования объект fig класса Figure размером 5 на 3 и плотность 100
        ax = fig.add_subplot() # Инициализиурем subplot ax

        # Если круговая диаграмма
        if visualisation.type_visualisation == 1:
            pieces = visualisation.parameters_for_pie[1]   # Значения сколько раз встречается определенная степень образования
            owners = visualisation.parameters_for_pie[0]   # Наименование уникальных значений
            custom_colors = ['b', 'r', 'c', 'm', 'y', 'g']      # Задаем список цветов пользовательский, например r = red
            explode = (0.2, 0, 0, 0, 0, 0)      # Задаем будет ли какая то часть отделятся, в данном случае первая часть отделяется

            # Для отображения без UI
            # plt.pie(pieces, labels=owners, colors=custom_colors)
            # plt.show()

            # Задаем ax что будет именно круговая диаграмма
            ax.pie(pieces,                # Значения сколько раз встречается определенная степень образования
                   labels=owners,           # title для частей
                   colors=custom_colors,    # Цвета
                   shadow=1,                # Тень
                   startangle=90,           # Угол с которого будет начинаться первая доля
                   explode=explode,         # Отделение какой то части
                   autopct='%1.1f%%'        # Указываем, что необходимо отобраджать проценты
                   )

            ax.axis('equal')                # Задаем чтобы график отображался без перспективы
            ax.legend(                      # Инициализируем легенду
                bbox_to_anchor=(0.23, 0.87),        # Координаты точки отсчета для прямоугольника легенды
                loc="upper right",                  # Позиционирование относительно точки
                prop={'size': 8},                   # Размер шрифта
                labels=owners)

        # Столбчатая диаграмма
        if visualisation.type_visualisation == 2:
            name_level_of_education = visualisation.unique_parental_level_of_education.tolist()
            xpos_male = np.arange(len(name_level_of_education)) - 0.2
            xpos_female = np.arange(len(name_level_of_education)) + 0.2

            count_male = visualisation.gender_parental_level_of_education[:6]
            count_female = visualisation.gender_parental_level_of_education[6:]

            ax.bar(xpos_male, count_male, width=0.4, label='Male')
            ax.bar(xpos_female, count_female, width=0.4, label='Female')
            ax.set_ylabel('Number')

            ax.legend(loc='upper right')

            xs = np.arange(len(name_level_of_education)).tolist()
            ax.set_xticks(xs)
            ax.set_xticklabels(name_level_of_education, fontdict={'fontsize': 8}, minor=False)

            y_min = 0
            y_max = np.amax(visualisation.gender_parental_level_of_education) * 1.5
            ax.set_ylim([y_min, y_max])

            fig.autofmt_xdate(rotation=25)

        if visualisation.type_visualisation == 3:
            x_list = visualisation.multi_x
            y_list = visualisation.multi_y

            y_min = np.amin(visualisation.multi_y)
            y_max = np.amax(visualisation.multi_y)

            x = len(x_list)
            ax.set_xlim([0, x])
            ax.set_ylim([y_min, y_max])

            ax.plot(x_list, y_list, color='red')

        if visualisation.type_visualisation == 4:
            ax = fig.add_subplot()
            owners = visualisation.parameters_for_pie[0]
            data = visualisation.parameters_for_pie_2
            offset = 0.4
            custom_colors = ['b', 'r', 'c', 'm', 'y', 'g']
            ax.pie(data.sum(axis=1), radius=1, colors=custom_colors, wedgeprops=dict(width=offset, edgecolor='w'))

            first_legend = fig.legend(
                title="Level of education",
                bbox_to_anchor=(0.32, 0.87),
                loc="upper right",
                prop={'size': 8},
                labels=owners)
            ax.add_artist(first_legend)

            custom_colors_2 = ['#DC143C', '#B8860B', '#32CD32']
            owners_2 = ['Satisfactorily', 'Good', 'Excellent']
            bx = fig.add_subplot()
            bx.pie(data.flatten(), radius=1 - offset, colors=custom_colors_2,
                   wedgeprops=dict(width=offset, edgecolor='w'))

            second_legend = bx.legend(
                title="Math_score",
                bbox_to_anchor=(0.1, 0.3),
                loc="upper right",
                prop={'size': 8},
                labels=owners_2)

            LH = second_legend.legendHandles
            j = 0
            for i in LH:
                i.set_color(custom_colors_2[j])
                j += 1

        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()

        if choice_of_place_for_output == 1:
            canvas.get_tk_widget().place(x=5, y=35)

        if choice_of_place_for_output == 2:
            canvas.get_tk_widget().place(x=550, y=35)

        if choice_of_place_for_output == 3:
            canvas.get_tk_widget().place(x=5, y=400)

        if choice_of_place_for_output == 4:
            canvas.get_tk_widget().place(x=550, y=400)

    def click_button_close(self, subWindow):
        subWindow.destroy()

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
                               values=[u"Круговая диаграмма", u"Столбчатая диаграмма", u"Мультипликативная модель",
                                       u"Вложенная круговая диаграмма"], height=4)
        self.c2.place(x=10, y=80)

        b1 = Button(a, text="Добавить", command=lambda: self.click_button_add(a), width="13", height="2")
        b1.place(x=40, y=150)
        b2 = Button(a, text="Закрыть", command=lambda: self.click_button_close(a), width="13", height="2")
        b2.place(x=170, y=150)

        a.grab_set()    # Перехватывает все события происходящие в приложении
        a.focus_set()   # Захватывает и удерживает фокус
