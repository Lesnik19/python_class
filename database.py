import sqlite3
from tkinter import messagebox


class Database:
    # подключение к БД, требуется её название
    def __init__(self, name):
        self.connector = sqlite3.connect(name)
        self.cursor = self.connector.cursor()

    def execute(self, request):
        try:
            result = self.cursor.execute(request)
        except sqlite3.DatabaseError as error:
            messagebox.showerror('Ошибка', 'Ошибка при обращении к базе данных!')
            print(error)
        else:
            self.connector.commit()
            return result

    def close(self):
        self.cursor.close()
        self.connector.close()
