<<<<<<< HEAD
# Teacher Profile Web App

This project is a responsive teacher profile page with a booking form and a basic backend API for listing courses per student and per teacher.

## Frontend
- `index.html`: Teacher profile page
- `booking.html`: Booking form for sessions with Alex Martin
- `teacher_page.html`: Detailed teacher page with bio, courses, intro video, and student feedback
- `admin_page.html`: Admin dashboard showing ongoing courses, attendance, video chat links, and course stats

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

# Responsive Teacher Profile Page

A responsive teacher profile website built using **React.js**. This project demonstrates a clean and interactive UI for showcasing a teacher's profile, including a video introduction, bio, and list of courses. Additionally, it includes a mock "Book a Session" button for potential future functionality.  

## Features:
- Teacher's name, subject, and bio
- Video intro placeholder
- Course list with 2-3 mock courses
- Optional "Book a Session" button

# Responsive Admin Page
## Features:
- Ongoing courses, attendance, video chat links, and course stats.
- Responsive design using Bootstrap.


## Screenshots:
![Profile Page](assets/screenshot1.png)  
![Course List](assets/screenshot2.png)

## How to Run:

1. Clone the repository:  
   git clone https://github.com/NajaKottarathil/teacher-profile.git

## Learn More
You can learn more in the Create React App documentation.

To learn React, check out the React documentation.

## License
This project is open-source and available under the MIT License.
=======
# teacher_profile_
Responsive Teacher Profile Page
>>>>>>> c93252cff88340a55f07afefdde645cb6522bc47
