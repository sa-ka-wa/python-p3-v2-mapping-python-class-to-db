from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
        
    @classmethod
    def create_table(cls):
        """Creates a new department in the database."""
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL
            )
        """)
        CONN.commit()
        print("Table created successfully.")

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS departments")
        CONN.commit()
        print("Table dropped successfully.")
            
    def save(self):
        '''Saves the instance to the database and sets its id.'''
        CURSOR.execute("""
            INSERT INTO departments (name, location)
            VALUES (?, ?)
        """, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, location):
        '''Creates and saves a new department instance to the DB, then returns it.'''
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        '''Updates the row in the database that matches the instance's id.'''
        CURSOR.execute("""
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        '''Deletes the row in the database that matches the instance's id.'''
        CURSOR.execute("DELETE FROM departments WHERE id = ?", (self.id,))
        CONN.commit()