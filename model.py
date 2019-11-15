import psycopg2

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



