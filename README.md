
# Teacher Profile Page

A responsive teacher profile website built using **React.js**. This project demonstrates a clean and interactive UI for showcasing a teacher's profile, including a video introduction, bio, and list of courses. Additionally, it includes a mock "Book a Session" button for potential future functionality. It also has a basic backend API for listing courses per student and per teacher

## Frontend
- `index.html`: Teacher profile page
  
## Features:
- Teacher's name, subject, and bio
- Video intro placeholder
- Course list with 2-3 mock courses
- Optional "Book a Session" button
  
## Backend (Python, Flask)

### Setup
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Run the backend:
   ```bash
   python backend.py
   ```
    ```bash
   flask run
   ```

### API Endpoints

#### List Courses per Student
- **Endpoint:** `/api/courses/student/<student_id>`
- **Method:** GET
- **Example:**
  ```bash
  curl http://127.0.0.1:5000/api/courses/student/1
  ```

#### List Courses per Teacher
- **Endpoint:** `/api/courses/teacher/<teacher_id>`
- **Method:** GET
- **Example:**
  ```bash
  curl http://127.0.0.1:5000/api/courses/teacher/1
  ```

# Admin Page Designed in Wireframe
## Features:
- Ongoing courses (shows  courses available)
- Attendance(a graph representing attendance in each class)
- Vdeo chat links(Link to classroom, time, and name of instructor)
- Course status(Number of lessons completed)

# Teacher page Designed in Wireframe
## Features:
- Name of instructor and bio
- Video placeholder
- Ongoing course
- Student feedback

## Screenshots:
![Profile Page](/assets/screenshot1.jpg)  
![Course List](/assets/screenshot2.jpg)

## How to Run:

1. Clone the repository:  
   git clone https://github.com/NajaKottarathil/teacher-profile_.git

2. Navigate to the directory containing teacher-profile
   cd teacher-profile

3. Install NPM
   npm install
   
4. Start the code
   npm start 

# teacher_profile_
Responsive Teacher Profile Page
>>>>>>> c93252cff88340a55f07afefdde645cb6522bc47
