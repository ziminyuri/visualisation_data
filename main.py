from tkinter import *
from MainWindow import MainWindow
from tkinter import *

def main():

    ### Отрисовываем UI
    root = Tk()
    app = MainWindow(root)
    app.pack()
    root.title("Визуализация данных")
    root.geometry('1400x820')
    root.resizable(False, False)
    root.mainloop()


if __name__=="__main__":
    main()