import sqlite3
from mimesis import Person

with sqlite3.connect('person.db') as connection:
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        )
    """)

    person = Person('en') ## Object of Person class from mimesis library

    list_of_persons = []
    for p in range(500000):
        first_name = person.first_name()
        last_name = person.last_name()
        list_of_persons.append((first_name, last_name))

    ## executemany() instead of execute() to insert multiple names at once
    cursor.executemany("""
        INSERT INTO person (first_name, last_name)
        VALUES (?, ?)
    """, list_of_persons)
