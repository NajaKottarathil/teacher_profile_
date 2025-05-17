import React from 'react';
import './TeacherProfile.css';
import './Courses.css';

const TeacherProfile = () => {
  const courses = [
    { id: 1, code: 'Arabic 101', name: 'Introduction to Arabic' },
    { id: 2, code: 'QU 1101', name: 'Introduction to Quran' },
    { id: 3, code: 'Arabic 1050', name: 'Arabic Grammar' }
  ];

  return (
    <div className="container mt-5">
      <div className="card p-4">
        <div className="row">
          <div className="col-md-4 text-center">
            <div className="teacher-photo mx-auto mb-3">
              <img
                src="/arabicteacher.jpg"
                alt="Teacher"
                className="img-fluid rounded-circle"
                style={{ width: '200px', height: '200px', objectFit: 'cover' }}
              />
            </div>
          </div>
          <div className="col-md-8">
            <h2>Abdullah Jassim</h2>
            <h5>Arabic Professor</h5>
            <p>
              Abdullah Jassim is a dedicated Arabic teacher who has a passion for making complex concepts
              easy to understand. He specializes in teaching Arabic, grammar, and Qur’an,
              and aims to inspire students to love learning Arabic.
            </p>
            <a href="/booking" className="btn btn-primary">Book a Session</a>
          </div>
        </div>
      </div>

      {/* Embedded YouTube video in cube style */}
      <div className="video-placeholder my-4">
        <iframe
          width="100%"
          height="100%"
          src="https://www.youtube.com/embed/XC62pWvw4b0"
          title="Arabic Learning Video"
          frameBorder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
          style={{ borderRadius: '12px' }}
        ></iframe>
      </div>

      <div className="courses-section">
        <h3 className="courses-title">Courses</h3>
        <div className="courses-container">
          {courses.map(course => (
            <div key={course.id} className="course-card">
              <div className="card p-3 h-100">
                <h5 className="course-code">{course.code}</h5>
                <p className="course-name mb-0">{course.name}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default TeacherProfile;
