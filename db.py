import psycopg2

class DB:
    def __init__(self, dbname, user, password, host='localhost'):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        self.c = self.conn.cursor()

    class Homework_Table:
        def __init__(self, db):
            self.db = db

        def create(self):
            self.db.c.execute('''CREATE TABLE IF NOT EXISTS homework (
                _id serial PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description VARCHAR(255) NOT NULL,
                due_date DATE NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT FALSE
            )''')
            self.db.conn.commit()

        def insert(self, title, description, due_date):
            self.db.c.execute('''INSERT INTO homework (title, description, due_date) VALUES (%s, %s, %s)''', (title, description, due_date))
            self.db.conn.commit()

        def update(self, _id, title, description, due_date):
            self.db.c.execute('''UPDATE homework SET title = %s, description = %s, due_date = %s WHERE _id = %s''', (title, description, due_date, _id))
            self.db.conn.commit()

        def delete(self, _id):
            self.db.c.execute('''DELETE FROM homework WHERE _id = %s''', (_id,))
            self.db.conn.commit()

        def select_all(self):
            self.db.c.execute('''SELECT * FROM homework''')
            return self.db.c.fetchall()

        def select_one(self, _id):
            self.db.c.execute('''SELECT * FROM homework WHERE _id = %s''', (_id,))
            return self.db.c.fetchone()

    class Projects_Table:
        def __init__(self, db):
            self.db = db

        def create(self):
            self.db.c.execute('''CREATE TABLE IF NOT EXISTS projects (
                _id serial PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description VARCHAR(255) NOT NULL,
                due_date DATE NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT FALSE
            )''')
            self.db.conn.commit()

        def insert(self, title, description, due_date):
            self.db.c.execute('''INSERT INTO projects (title, description, due_date) VALUES (%s, %s, %s)''', (title, description, due_date))
            self.db.conn.commit()

        def update(self, _id, title, description, due_date):
            self.db.c.execute('''UPDATE projects SET title = %s, description = %s, due_date = %s WHERE _id = %s''', (title, description, due_date, _id))
            self.db.conn.commit()

        def delete(self, _id):
            self.db.c.execute('''DELETE FROM projects WHERE _id = %s''', (_id,))
            self.db.conn.commit()

        def select_all(self):
            self.db.c.execute('''SELECT * FROM projects''')
            return self.db.c.fetchall()

        def select_one(self, _id):
            self.db.c.execute('''SELECT * FROM projects WHERE _id = %s''', (_id,))
            return self.db.c.fetchone()

    class Exam_Table:
         # date, topic, batch, completed
        def __init__(self, db):
            self.db = db

        def create(self):
            self.db.c.execute('''CREATE TABLE IF NOT EXISTS exam (
                _id serial PRIMARY KEY,
                date DATE NOT NULL,
                topic VARCHAR(255) NOT NULL,
                batch VARCHAR(255) NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT FALSE
            )''')
            self.db.conn.commit()

        def insert(self, date, topic, batch):
            self.db.c.execute('''INSERT INTO exam (date, topic, batch) VALUES (%s, %s, %s)''', (date, topic, batch))
            self.db.conn.commit()

        def update(self, _id, date, topic, batch):
            self.db.c.execute('''UPDATE exam SET date = %s, topic = %s, batch = %s WHERE _id = %s''', (date, topic, batch, _id))
            self.db.conn.commit()

        def delete(self, _id):
            self.db.c.execute('''DELETE FROM exam WHERE _id = %s''', (_id,))
            self.db.conn.commit()

        def completed(self, _id):
            self.db.c.execute('''UPDATE exam SET completed = TRUE WHERE _id = %s''', (_id,))
            self.db.conn.commit()