import sqlite3 as sq

con = None

'''В данном примере используем метод уже без менеджера контекста, сохранение и закрытие БД вручную через методы. При штатной работе все данные будут сохранены,
если возникнет исключение, то выскочит ошибка, а БД откатится в исходное состоянию с помощью метода rollback'''
try:
    con = sq.connect("cars.db") # подключаемся к БД
    cur = con.cursor() # метод для взаимодействия с БД

    #данный метод записывает sql-запросы так как они есть, буквально со всеми данными
    # cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
    #         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         model TEXT,
    #         price INTEGER
    #     );
    #     BEGIN;
    #     INSERT INTO cars VALUES(NULL,'Audi',52642);
    #     INSERT INTO cars VALUES(NULL,'Mercedes',57127);
    #     INSERT INTO cars VALUES(NULL,'Skoda',9000);
    #     INSERT INTO cars VALUES(NULL,'Volvo',29000);
    #     INSERT INTO cars VALUES(NULL,'Bentley',350000);
    #     UPDATE cars SET price = price+1000
    # """)
    #con.commit() # сохранение в БД всех внесенных изменений

    # в списке указываем не верный тип, чтобы вызвать ошибку
    cur.executemany("DELETE FROM cars WHERE car_id=?", [13, 17])

except sq.Error as e:
    print("Ошибка выполнения запроса", e)
finally:
    if con: con.close()
