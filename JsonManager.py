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

    
    def create_test(self, exam_name, exam_description, lesson_name, exam_data:dict):
        
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