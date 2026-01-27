import json
import os

class Testmanager:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.tests = []
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
    def get_tests(self):
        self.tests = []

        for filename in os.listdir(self.folder_path):
            if filename.endswith(".json"):
                self.tests.append(filename)

        return self.tests

    
    def create_test(self, exam_name, exam_description, lesson_name, exam_data:dict=[]):
        
        with open(os.path.join(self.folder_path, f"{exam_name}.json"), "w", encoding="utf-8") as file:
            data = {
                "exam_name": exam_name,
                "exam_description": exam_description,
                "lesson_name": lesson_name,
                "exam_data": exam_data
            }
            #Exampe and structure
            #data = {
            #        "exam_name": exam_name,
            #        "exam_description": exam_description,
            #        "lesson_name": lesson_name,
            #        "exam_data": [
            #           {
            #                "question": "question",
            #                "options": ["A", "B", "C", "D"],
            #                "correct": index of correct option
            #            },
            #            {
            #                "question": "questions",
            #                "options": ["A", "B", "C", "D"],
            #                "correct": index of correct option
            #            }
            #        ]
            #    }

            json.dump(data, file, ensure_ascii=False, indent=4)
            return True
        
    def edit_test(self, filename, new_data:dict):
        file_path = os.path.join(self.folder_path, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            data.update(new_data)
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return True
        except FileNotFoundError:
            print(f"{filename} bulunamadı.")
            return False

    def delete_test(self, filename):
        file_path = os.path.join(self.folder_path, filename)
        try:
            os.remove(file_path)
            print(f"{filename} başarıyla silindi.")
        except FileNotFoundError:
            print(f"{filename} bulunamadı.")

    def get_test_data(self, filename):
        file_path = os.path.join(self.folder_path, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"{filename} bulunamadı.")
            return None
        except json.JSONDecodeError:
            print(f"JSON okunamadı: {file_path}")
            return None
        
    def get_results(self, students_answer, exam_name):
        data = self.get_test_data(f"{exam_name}.json")
        if data and "exam_data" in data:
            exam_questions = data["exam_data"]
            correct_answers = [q["correct"] for q in exam_questions]
            score = sum(1 for i, answer in enumerate(students_answer) if answer == correct_answers[i])
            return {
                "score": score,
                "total_questions": len(exam_questions),
                "percentage": (score / len(exam_questions) * 100) if exam_questions else 0
            }
        return None