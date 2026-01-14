import sqlite3

class DBManager:
    def __init__(self, db_name="school.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            school_no TEXT,
            class_id INTEGER,
            points INTEGER DEFAULT 0,
            FOREIGN KEY (class_id) REFERENCES classes(id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lesson_name TEXT,
            topic_name TEXT,
            description TEXT,
            youtube_url TEXT,
            class_id INTEGER,
            FOREIGN KEY (class_id) REFERENCES classes(id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lesson_name TEXT,
            topic_name TEXT,
            description TEXT,
            json_file TEXT,
            class_id INTEGER,
            FOREIGN KEY (class_id) REFERENCES classes(id)
        )
        """)

        self.conn.commit()

    # ---------- TEACHERS ----------
    def register_teacher(self, name, email, password):
        self.cursor.execute(
            "INSERT INTO teachers VALUES (NULL, ?, ?, ?)",
            (name, email, password)
        )
        self.conn.commit()

    def login_teacher(self, email, password):
        self.cursor.execute(
            "SELECT * FROM teachers WHERE email=? AND password=?",
            (email, password)
        )
        return self.cursor.fetchone()

    # ---------- CLASSES ----------
    def add_class(self, name):
        self.cursor.execute(
            "INSERT INTO classes VALUES (NULL, ?)",
            (name,)
        )
        self.conn.commit()

    def get_all_classes(self):
        self.cursor.execute("SELECT * FROM classes")
        return self.cursor.fetchall()

    # ---------- STUDENTS ----------
    def add_student(self, name, school_no, class_id):
        #Aynı numaraya ait bir öğrenci olup olmadığını kontrol et
        self.cursor.execute(
            "SELECT * FROM students WHERE school_no=?",
            (school_no,)
        )
        if self.cursor.fetchone():
            raise ValueError("Bu numaraya ait bir öğrenci zaten var.")
        else:
            self.cursor.execute(
                "INSERT INTO students VALUES (NULL, ?, ?, ?, 0)",
                (name, school_no, class_id)
            )
            self.conn.commit()

    def delete_student(self, student_id):
        self.cursor.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )
        self.conn.commit()

    def get_students_by_class(self, class_id):
        self.cursor.execute(
            "SELECT * FROM students WHERE class_id=?",
            (class_id,)
        )
        return self.cursor.fetchall()

    def add_points(self, student_id, points):
        self.cursor.execute(
            "UPDATE students SET points = points + ? WHERE id=?",
            (points, student_id)
        )
        self.conn.commit()

    # ---------- LESSONS ----------
    def add_lesson(self, lesson_name, topic_name, description, youtube_url, class_id):
        self.cursor.execute(
            "INSERT INTO lessons VALUES (NULL, ?, ?, ?, ?, ?)",
            (lesson_name, topic_name, description, youtube_url, class_id)
        )
        self.conn.commit()

    def get_lessons_by_class(self, class_id):
        self.cursor.execute(
            "SELECT * FROM lessons WHERE class_id=?",
            (class_id,)
        )
        return self.cursor.fetchall()

    def get_all_lessons(self):
        """Return all lessons across classes."""
        self.cursor.execute("SELECT * FROM lessons")
        return self.cursor.fetchall()

    # ---------- TESTS ----------
    def add_test(self, lesson_name, topic_name, description, json_file, class_id):
        self.cursor.execute(
            "INSERT INTO tests VALUES (NULL, ?, ?, ?, ?, ?)",
            (lesson_name, topic_name, description, json_file, class_id)
        )
        self.conn.commit()

    def get_tests_by_class(self, class_id):
        self.cursor.execute(
            "SELECT * FROM tests WHERE class_id=?",
            (class_id,)
        )
        return self.cursor.fetchall()

if __name__ == "__main__":
    db_manager = DBManager()
    db_manager.create_tables()
    # Example usage
    db_manager.add_class("10-B")
    db_manager.add_student("Ayşe Fatma", "67890", 2)
    db_manager.add_lesson("Science", "Physics", "Basic Physics Concepts", "https://youtube.com/example2", 2)
    db_manager.add_test("Science", "Physics", "Physics Test", "physics_test.json", 2)
    print(db_manager.get_students_by_class(1))
