import psycopg2
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

    # conn = psycopg2.connect(dbname='database', user='db_user',
         #                   password='mypassword', host='localhost')
    #cursor = conn.cursor()

    #cursor.execute('SELECT * FROM airport LIMIT 10')
    #records = cursor.fetchall()

    #cursor.close()
    #conn.close()


if __name__=="__main__":
    main()