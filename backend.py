from flask import Flask, jsonify

app = Flask(__name__)

# Mock data
teachers = {
    "1": {
        "name": "Alex Martin",
        "courses": [
            {"id": "INFS3201", "title": "Introduction to Web Technologies"},
            {"id": "DACS3203", "title": "Cyber Security Analytics"},
            {"id": "MATH1050", "title": "Linear Algebra"}
        ]
    }
}
students = {
    "1": {
        "name": "Student One",
        "courses": [
            {"id": "INFS3201", "title": "Introduction to Web Technologies"},
            {"id": "MATH1050", "title": "Linear Algebra"}
        ]
    },
    "2": {
        "name": "Student Two",
        "courses": [
            {"id": "DACS3203", "title": "Cyber Security Analytics"}
        ]
    }
}

@app.route('/api/courses/student/<student_id>', methods=['GET'])
def get_courses_for_student(student_id):
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"student": student["name"], "courses": student["courses"]})

@app.route('/api/courses/teacher/<teacher_id>', methods=['GET'])
def get_courses_for_teacher(teacher_id):
    teacher = teachers.get(teacher_id)
    if not teacher:
        return jsonify({"error": "Teacher not found"}), 404
    return jsonify({"teacher": teacher["name"], "courses": teacher["courses"]})

if __name__ == '__main__':
    app.run(debug=True) 