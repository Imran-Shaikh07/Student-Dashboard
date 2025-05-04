# app/models.py
from app import mongo
from bson.objectid import ObjectId

class Student:
    @staticmethod
    def get_all_students():
        return list(mongo.db.RuralStudents.find())
    
    @staticmethod
    def search_students(name):
        return list(mongo.db.RuralStudents.find({"Name": {"$regex": name, "$options": "i"}}))
    
    @staticmethod
    def get_student_by_id(student_id):
        try:
            return mongo.db.RuralStudents.find_one({"_id": ObjectId(student_id)})
        except Exception:
            return None
    
    @staticmethod
    def get_class_distribution():
        pipeline = [
            {"$group": {"_id": "$Class", "count": {"$sum": 1}}},
            {"$sort": {"_id": 1}}
        ]
        return list(mongo.db.RuralStudents.aggregate(pipeline))
    
    @staticmethod
    def get_subject_averages():
        subjects = ["Math Marks", "Science Marks", "English Marks", 
                   "Social Studies Marks", "Telugu Marks"]
        result = {}
        
        for subject in subjects:
            pipeline = [
                {"$group": {"_id": None, "average": {"$avg": f"${subject}"}}}
            ]
            avg_result = list(mongo.db.RuralStudents.aggregate(pipeline))
            if avg_result:
                result[subject.replace(" Marks", "")] = round(avg_result[0]["average"], 2)
            else:
                result[subject.replace(" Marks", "")] = 0
                
        return result
