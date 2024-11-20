import sqlite3

# Создание и подключение к базе данных
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Очистка таблицы перед заполнением (если требуется)
cursor.execute("DELETE FROM Users")

# Заполнение таблицы 10 записями
users = [
    (f"User{i}", f"example{i}@gmail.com", i * 10, 1000) for i in range(1, 11)
]
cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users)

# Обновление balance у каждой 2-ой записи начиная с 1-ой
cursor.execute("SELECT id FROM Users")
all_ids = [row[0] for row in cursor.fetchall()]
for i, user_id in enumerate(all_ids):
    if i % 2 == 0:  # Индексы начинаются с 0
        cursor.execute("UPDATE Users SET balance = 500 WHERE id = ?", (user_id,))

# Удаление каждой 3-ей записи начиная с 1-ой
cursor.execute("SELECT id FROM Users")
all_ids = [row[0] for row in cursor.fetchall()]
for i, user_id in enumerate(all_ids):
    if i % 3 == 0:  # Индексы начинаются с 0
        cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))

# Выборка всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
result = cursor.fetchall()

# Вывод в консоль
for row in result:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

# Сохранение изменений и закрытие подключения
connection.commit()
connection.close()

###
"""
Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500
"""