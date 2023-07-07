import sqlite3 as sq

# второй способ ввода данных в БД (с помощью коллекций)
cars = [
    ('Toyota Camry', 770000),
    ('KIA Spectra', 240000),
    ('VAZ 2114', 120000)
]

with sq.connect("cars.db") as con: # подключаемся к БД

    cur = con.cursor() # метод для взаимодействия с БД

    # здесь можем указывать sql-запросы для работы с БД
    cur.execute('''CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INREGER
    )''')


    # первый способ ввода данных в БД
    # cur.execute("INSERT OR IGNORE INTO cars VALUES(1, 'Toyota Camry', 770000)")
    # cur.execute("INSERT OR IGNORE INTO cars VALUES(2, 'KIA Spectra', 240000)")
    # cur.execute("INSERT OR IGNORE INTO cars VALUES(3, 'VAZ 2124', 120000)")

    # второй способ ввода данных в БД (с помощью коллекций)
    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    #третий способ ввода данных в БД (через метод, похож на второй способ)
    #cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    # удаление данных (одной записи) из таблицы
    #cur.execute("DELETE FROM cars WHERE car_id=6")

    # удаление данных (много записей) из таблицы
    #cur.executemany("DELETE FROM cars WHERE car_id=?", [(3,), (7,), (8,), (9,)])

    # SQL-запрос (выборка из таблицы)
    cur.execute("SELECT * FROM cars")

    # с помощью метода fetchall выводим SQL-запрос
    rows = cur.fetchall()
    print(rows)
