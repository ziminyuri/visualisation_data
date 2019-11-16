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
        records = get_records_from_postgress()

        self.gender = []
        self.race = []
        self.parental_level_of_education = []
        self.lunch = []
        self.test_preparation_course = []
        self.math_score = []
        self.reading_score = []
        self.writing_score = []

        for i in records:
            self.gender.append(i[0])
            self.race.append(i[1])
            self.parental_level_of_education.append(i[2])
            self.lunch.append(i[3])
            self.test_preparation_course.append(i[4])
            self.math_score.append(i[5])
            self.reading_score.append(i[6])
            self.writing_score.append(i[7])

        self.type_visualisation = 0

    def count_parameters_for_pie(self):
        self.type_visualisation = 1
        self.parameters_for_pie = np.unique(self.parental_level_of_education, return_counts=True)


    def count_parameters_for_bar(self):
        self.type_visualisation = 2
        unique_parental_level_of_education = np.unique(self.parental_level_of_education)

        len_unique = len(unique_parental_level_of_education)
        self.gender_parental_level_of_education = np.zeros(len_unique * 2)

        n = len(self.parental_level_of_education)
        m = len(unique_parental_level_of_education)

        for i in range(n):
            for j in range(m):
                if self.parental_level_of_education[i] == unique_parental_level_of_education[j]:
                    if self.gender[i] == "male":
                        self.gender_parental_level_of_education[j] += 1
                    else:
                        self.gender_parental_level_of_education[m + j] += 1

        self.unique_parental_level_of_education = unique_parental_level_of_education

    def count_parameters_multi(self):
        self.type_visualisation = 3

        k = 0.1
        b = 4
        n= 1000
        x = np.arange(0, n)
        trend_y_1 = k * x + b

        trend_y_2 = np.random.uniform(-100, 100, n)

        self.multi_y = trend_y_1 * trend_y_2
        self.multi_x = x

    def count_parameters_nested_pie(self):
        self.type_visualisation = 4
        self.parameters_for_pie = np.unique(self.parental_level_of_education, return_counts=True)

        parameters_for_pie_2 = [[0] * 3 for i in range(len(self.parameters_for_pie[0]))]

        n = len(self.math_score)
        m = len(self.parameters_for_pie[0])

        for i in range(n):
            for j in range(m):
                if self.parental_level_of_education[i] == self.parameters_for_pie[0][j]:
                    if self.math_score[i] <50:
                        parameters_for_pie_2[j][0] += 1

                    if (self.math_score[i] >=50) and (self.math_score[i] <75):
                        parameters_for_pie_2[j][1] += 1

                    if self.math_score[i] >=75:
                        parameters_for_pie_2[j][2] += 1

        self.parameters_for_pie_2 = np.array(parameters_for_pie_2)

