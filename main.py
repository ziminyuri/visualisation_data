from tkinter import *
from MainWindow import MainWindow
from tkinter import *

def main():

    ### Отрисовываем UI
    root = Tk()                     # Инициализируем использования библиотеки Tk
    app = MainWindow(root)          # Инициализируем окно MainWindow
    app.pack()
    root.title("Визуализация данных")
    root.geometry('1400x820')
    root.resizable(False, False)        # Нельзя изменить размер экрана
    root.mainloop()                     # Запустили цикл для ожидания нажатия


if __name__=="__main__":
    main()