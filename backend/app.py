from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Mock database
teachers = {
    "1": {
        "id": "1",
        "name": "Mohammed Salah",
        "subject": "Introduction to Quran",
        "courses": [
            {
                "id": "QUR 1010",
                "code": "QUR 1010",
                "title": "Introduction to Quran",
                "students": ["1", "2", "3"],
                "schedule": "MWF 10:00-11:30",
                "semester": "Fall 2024"
            },
            {
                "id":  "ISL 1120",
                 "code": "ISL 1120",
                "title": "Introduction to Islamic Studies",
                "students": ["1", "4", "5"],
                "schedule": "TTh 13:00-14:30",
                "semester": "Fall 2024"
            },
            {
                "id": "ARB 1050",
                "code": "ARB 1050",
                "title": "Introduction to Arabic",
                "students": ["2", "3", "5"],
                "schedule": "MWF 14:00-15:30",
                "semester": "Fall 2024"
            }
        ]
    }
}

students = {
    "1": {
        "id": "1",
        "name": "Ayesha Syed",
        "courses": ["QUR 1010", "ARB 1050"]
    },
    "2": {
        "id": "2",
        "name": "Aboobacker M",
        "courses": ["ARB 1050", "ISL 1120"]
    },
    "3": {
        "id": "3",
        "name": "Salem Mo",
        "courses": ["ISL 1120", "QUR 1010"]
    },
    "4": {
        "id": "4",
        "name": "Ali Radwan",
        "courses": ["QUR 1010"]
    },
    "5": {
        "id": "5",
        "name": "Khalid H",
        "courses": ["QUR 1010", "ARB 1050"]
    }
}

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route('/api/courses/student/<student_id>', methods=['GET'])
def get_courses_for_student(student_id):
    """
    Get all courses for a specific student
    
    Args:
        student_id (str): The ID of the student
        
    Returns:
        JSON response containing student information and their courses
    """
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    
    # Get detailed course information for each course ID
    student_courses = []
    for course_id in student["courses"]:
        for teacher in teachers.values():
            for course in teacher["courses"]:
                if course["id"] == course_id:
                    student_courses.append({
                        "id": course["id"],
                        "code": course["code"],
                        "title": course["title"],
                        "teacher": teacher["name"],
                        "schedule": course["schedule"],
                        "semester": course["semester"]
                    })
    
    return jsonify({
        "student": {
            "id": student["id"],
            "name": student["name"]
        },
        "courses": student_courses
    })

@app.route('/api/courses/teacher/<teacher_id>', methods=['GET'])
def get_courses_for_teacher(teacher_id):
    """
    Get all courses for a specific teacher
    
    Args:
        teacher_id (str): The ID of the teacher
        
    Returns:
        JSON response containing teacher information and their courses
    """
    teacher = teachers.get(teacher_id)
    if not teacher:
        return jsonify({"error": "Teacher not found"}), 404
    
    # Get student information for each course
    courses_with_students = []
    for course in teacher["courses"]:
        course_students = []
        for student_id in course["students"]:
            student = students.get(student_id)
            if student:
                course_students.append({
                    "id": student["id"],
                    "name": student["name"]
                })
        
        courses_with_students.append({
            "id": course["id"],
            "code": course["code"],
            "title": course["title"],
            "schedule": course["schedule"],
            "semester": course["semester"],
            "students": course_students
        })
    
    return jsonify({
        "teacher": {
            "id": teacher["id"],
            "name": teacher["name"],
            "subject": teacher["subject"]
        },
        "courses": courses_with_students
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000) 