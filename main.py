from flask import Flask, render_template, request, redirect
from DBmanager import DBManager
from JsonManager import Testmanager

db_manager = DBManager()
db_manager.create_tables()


app = Flask(__name__)
testmanager = Testmanager(folder_path="Testjsons")

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
        if db_manager.add_student(name, number, class_id) == True:
            return redirect("/ogrenciler/add")
        elif db_manager.add_student(name, number, class_id) == False:
            return redirect("/ogrenciler/add/error_samenumber")

    data = []
    for cls in classes:
        class_dict = {
            "id": cls[0],
            "name": cls[1],
            "students": db_manager.get_students_by_class(cls[0])
        }
        data.append(class_dict)

    return render_template("addstudents.html", classes=data)

@app.route("/ogrenciler/add/error_samenumber")
def ogrenciler_add_error_samenumber():
    return render_template("addstudents.html", error="Aynı numaraya sahip öğrenci zaten var.")

@app.route('/ogrenciler/delete/<int:student_id>')
def ogrenciler_delert(student_id):
    db_manager.delete_student(student_id)
    return redirect("/ogrenciler")

@app.route('/ogrenciler/points/<int:student_id>')
def ogrenciler_points(student_id):
    db_manager.add_points(student_id, 10)
    return redirect("/ogrenciler")

@app.route('/ogrenciler/addclass', methods=['GET', 'POST'])
def ogrenciler_addclass():
    if request.method == "POST":
        name = request.form.get("name")
        if db_manager.add_class(name):
            return redirect("/ogrenciler")
        else:
            return redirect("/ogrenciler/addclass", error="Sınıf ekleme işlemi başarısız oldu.")

    return render_template("addclass.html")

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

@app.route('/dersler/add', methods=['GET', 'POST'])
def dersler_add():
    classes = db_manager.get_all_classes()
    if request.method == "POST":
        lesson_name = request.form.get("lesson_name")
        topic_name = request.form.get("topic_name")
        description = request.form.get("description")
        youtube_url = request.form.get("youtube_url")
        class_id = request.form.get("class_id")

        db_manager.add_lesson(lesson_name, topic_name, description, youtube_url, class_id)
        return redirect("/dersler")
    
    data = []
    for cls in classes:
        class_dict = {
            "id": cls[0],
            "name": cls[1],
            "students": db_manager.get_students_by_class(cls[0])
        }
        data.append(class_dict)

    return render_template("addders.html", classes=data)

@app.route('/dersler/delete/<int:lesson_id>')

@app.route("/sinavlar")
def sinavlar():
    tests = testmanager.get_tests()
    print(tests)
    tests_data = []
    for i in tests:
        tests_data.append(testmanager.get_test_data(i))
    print(tests_data)

    return render_template("exam.html", tests_data=tests_data)

@app.route('/sinavlar/add', methods=['GET', 'POST'])
def sinavlar_add():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        lessons_name = request.form.get("lessons_name")
        if testmanager.create_test(name, description, lessons_name):
            return redirect("/sinavlar")
        else:
            return redirect("/sinavlar/add/error")

    return render_template("exam_add.html")

@app.route('/sinavlar/add/error')
def sinavlar_add_error():
    return render_template("exam_add.html", error="Sınav ekleme işlemi başarısız oldu.")

@app.route('/sinavlar/delete/<string:examname>')
def sinavlar_delete(examname):
    testmanager.delete_test(f"{examname}.json")
    return redirect("/sinavlar")

@app.route('/sinavlar/edit/<string:examname>', methods=['GET', 'POST'])
def sinavlar_edit(examname):
    if request.method == "POST":
        exam_name = request.form.get("exam_name")
        description = request.form.get("description")
        lessons_name = request.form.get("lessons_name")

        exam_data = []
        question_count = 1
        while True:
            question_key = f"question_{question_count}"
            if question_key not in request.form:
                break

            question = request.form.get(question_key)
            options = [
                request.form.get(f"A){question_count}"),
                request.form.get(f"B){question_count}"),
                request.form.get(f"C){question_count}"),
                request.form.get(f"D){question_count}")
            ]
            correct_option = request.form.get(f"correct_{question_count}")
            # correct_option 'A', 'B', 'C', 'D' değerini taşıdığından, direct olarak indexe dönüştür
            correct_index = ord(correct_option) - ord('A') if correct_option in ['A', 'B', 'C', 'D'] else 0

            exam_data.append({
                "question": question,
                "options": options,
                "correct": correct_index
            })

            question_count += 1

        new_data = {
            "exam_name": exam_name,
            "exam_description": description,
            "lesson_name": lessons_name,
            "exam_data": exam_data
        }

        # Eğer sınav adı değişmişse, eski dosyayı sil ve yeni dosya adıyla kaydet
        if exam_name != examname:
            testmanager.delete_test(f"{examname}.json")
            if testmanager.create_test(exam_name, description, lessons_name, exam_data):
                return redirect("/sinavlar")
            else:
                return redirect(f"/sinavlar/edit/{examname}/error")
        else:
            # Sınav adı değişmemişse, sadece güncelle
            if testmanager.edit_test(f"{examname}.json", new_data):
                return redirect("/sinavlar")
            else:
                return redirect(f"/sinavlar/edit/{examname}/error")

    try:
        exam_data = testmanager.get_test_data(f"{examname}.json")
        return render_template("exam_edit.html",
                               exam_name=exam_data.get("exam_name", examname),
                               exam_description=exam_data.get("exam_description", ""),
                               lesson_name=exam_data.get("lesson_name", ""),
                               exam_questions=exam_data.get("exam_data", []))
    except:
        return render_template("exam_edit.html", error=f"{examname} sınavı yüklenemedi.")


if __name__ == '__main__':
    app.run(debug=True)