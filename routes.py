# app/routes.py
from flask import Blueprint, render_template, request, jsonify
from app.models import Student
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    students = Student.get_all_students()
    class_distribution = Student.get_class_distribution()
    subject_averages = Student.get_subject_averages()
    
    # Format chart data for JS
    chart_data = {
        "class_distribution": {
            "labels": [str(item["_id"]) for item in class_distribution],
            "data": [item["count"] for item in class_distribution]
        },
        "subject_averages": {
            "labels": list(subject_averages.keys()),
            "data": list(subject_averages.values())
        }
    }
    
    return render_template('dashboard.html', 
                          students=students[:10],  # Show first 10 on dashboard
                          chart_data=chart_data)

@main.route('/search')
def search():
    query = request.args.get('query', '')
    if query:
        results = Student.search_students(query)
    else:
        results = []
    
    return render_template('search.html', students=results, query=query)

@main.route('/student/<student_id>')
def student_details(student_id):
    student = Student.get_student_by_id(student_id)
    
    # Get subject marks for the individual student chart
    subjects = ["Math", "Science", "English", "Social Studies", "Telugu"]
    marks = [student.get(f"{subject} Marks", 0) for subject in subjects]
    
    return render_template('student_details.html', 
                          student=student, 
                          subjects=subjects,
                          marks=marks)
