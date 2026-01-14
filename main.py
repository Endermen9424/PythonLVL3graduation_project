from flask import Flask, render_template, request, redirect
from DBmanager import DBManager

db_manager = DBManager()
db_manager.create_tables()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ogrenciler')
def ogrenciler():
    classes = db_manager.get_all_classes()

    data = []

    for cls in classes:
        class_dict = {
            "id": cls[0],
            "name": cls[1],
            "students": db_manager.get_students_by_class(cls[0])
        }
        data.append(class_dict)

    return render_template("ogrenciler.html", classes=data)

@app.route('/ogrenciler/add', methods=['GET', 'POST'])
def ogrenciler_add():
    classes = db_manager.get_all_classes()
    
    if request.method == "POST":
        name = request.form.get("name")
        number = request.form.get("number")
        class_id = request.form.get("class_id")
        db_manager.add_student(name, number, class_id)
        return redirect("/ogrenciler/add")

    data = []
    for cls in classes:
        class_dict = {
            "id": cls[0],
            "name": cls[1],
            "students": db_manager.get_students_by_class(cls[0])
        }
        data.append(class_dict)

    return render_template("addstudents.html", classes=data)

@app.route('/ogrenciler/delete/<int:student_id>')
def ogrenciler_delert(student_id):
    db_manager.delete_student(student_id)
    return redirect("/ogrenciler")

@app.route('/ogrenciler/points/<int:student_id>')
def ogrenciler_points(student_id):
    db_manager.add_points(student_id, 10)
    return redirect("/ogrenciler")


@app.route('/dersler')
def dersler():
    lessons = db_manager.get_all_lessons()

    data = [
        {
            "lesson": l[1],
            "topic": l[2],
            "desc": l[3],
            "youtube": l[4]
        } for l in lessons
    ]

    return render_template("dersler.html", lessons=data)


@app.route('/ayarlar')
def ayarlar():
    return render_template('ayarlar.html')
if __name__ == '__main__':
    app.run(debug=True)