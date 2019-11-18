import psycopg2
import numpy as np


# Получаем значения из БД
def get_records_from_postgress():
    # Устанавилваем соединением с Postgres
    conn = psycopg2.connect(dbname='profi', user='zimin_data', password='1', host='localhost')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Public."Visualisation_data"')
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    # Закончили работать с бд

    return records


class Model():
    def __init__(self):
        records = get_records_from_postgress()   # Получили список значений из БД

        # Далее разделяем данняе по заголовкам
        # Объявляем одноименые пустые списки
        self.gender = []
        self.race = []
        self.parental_level_of_education = []
        self.lunch = []
        self.test_preparation_course = []
        self.math_score = []
        self.reading_score = []
        self.writing_score = []

        # Добавляем в конец списка необходимо значение
        for i in records:
            self.gender.append(i[0])
            self.race.append(i[1])
            self.parental_level_of_education.append(i[2])
            self.lunch.append(i[3])
            self.test_preparation_course.append(i[4])
            self.math_score.append(i[5])
            self.reading_score.append(i[6])
            self.writing_score.append(i[7])

        # ИНициализируем номер типа визаулизации по умполчанию равен 0
        self.type_visualisation = 0

    # Подготавливаем данные для круговой диаграммы
    def count_parameters_for_pie(self):
        # Указали номер визуализации
        self.type_visualisation = 1
        # Создаем массив numpy с количество уникальных значений, и количеством их вхождений в исходный массив
        self.parameters_for_pie = np.unique(self.parental_level_of_education, return_counts=True)

    # Расчитываем параметры для столбчатой диаграммы
    def count_parameters_for_bar(self):
        self.type_visualisation = 2
        # Создаем массив numpy с количество уникальных значений
        unique_parental_level_of_education = np.unique(self.parental_level_of_education)

        # Считаем длину этого массива
        len_unique = len(unique_parental_level_of_education)

        # Создаем массив значений из нулей размером кол-во уникальных label education для каждого пола
        self.gender_parental_level_of_education_male = np.zeros(len_unique)
        self.gender_parental_level_of_education_female = np.zeros(len_unique)

        n = len(self.parental_level_of_education)
        m = len(unique_parental_level_of_education)

        # Проходим по всем значения, если i значение совпадает с j значением уникального образования, то проверяем пол i
        # го элемента и увеличваем значение на 1 для нужного массива
        for i in range(n):
            for j in range(m):
                if self.parental_level_of_education[i] == unique_parental_level_of_education[j]:
                    if self.gender[i] == "male":
                        self.gender_parental_level_of_education_male[j] +=1
                    else:
                        self.gender_parental_level_of_education_female[j] += 1

        # Присваиваем значение полю класса
        self.unique_parental_level_of_education = unique_parental_level_of_education

    # Расчитваем значение для мультипликативного тренда
    def count_parameters_multi(self):
        self.type_visualisation = 3


        k = 0.1
        b = 4
        n= 1000
        x = np.arange(0, n) # Формирвуем массив numpy из n элементов от 0 до n
        trend_y_1 = k * x + b     # Создаем  массив numpy где каждое значение вычисляется как k * x + b

        trend_y_2 = np.random.uniform(-100, 100, n)  # # Создаем  массив numpy из n элементов где каждая величина есть
        # случайная величина от -100 до 100

        self.multi_y = trend_y_1 * trend_y_2  # Перемножаем две матрицы для формирования мультипликативной модели значений y
        self.multi_x = x            # Значения х

    def count_parameters_nested_pie(self):
        self.type_visualisation = 4
        self.parameters_for_pie = np.unique(self.parental_level_of_education, return_counts=True)

        # Создаем numpy двумерный массив из 0 где столбцы это количество оценок - удовлетворительно, хорошо, отлично
        # А строки label education
        parameters_for_pie_2 = [[0] * 3 for i in range(len(self.parameters_for_pie[0]))]


        n = len(self.math_score)
        m = len(self.parameters_for_pie[0])

        # Проходим по всем значения, если совпадает с уникальным то проверяем балл оценки по математики и увеличиваем
        # на 1 подходяшее значение
        for i in range(n):
            for j in range(m):
                if self.parental_level_of_education[i] == self.parameters_for_pie[0][j]:
                    if self.math_score[i] <50:
                        parameters_for_pie_2[j][0] += 1

                    if (self.math_score[i] >=50) and (self.math_score[i] <75):
                        parameters_for_pie_2[j][1] += 1

                    if self.math_score[i] >=75:
                        parameters_for_pie_2[j][2] += 1

        # Присваиваем полю класса значение и конверитруем значение из списка в массив numpy
        self.parameters_for_pie_2 = np.array(parameters_for_pie_2)

