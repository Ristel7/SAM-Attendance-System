# 📄 Software Requirements Specification (SRS)

# 🎓 SAM Attendance Management System

---

# 1. Introduction

## 1.1 Project Title

SAM Attendance Management System

---

## 1.2 Project Overview

The SAM Attendance Management System is a web-based application developed to digitally manage classroom attendance for Diploma CSE 2025–26 Final Semester students at SAM Global University.

The system provides a smart and efficient platform for teachers to manage student attendance records, monitor present/absent statistics, and maintain attendance history using a modern dashboard interface.

The application eliminates the need for traditional paper-based attendance systems and improves overall classroom attendance management.

---

# 2. Purpose of the Project

The purpose of this project is to:

- Digitize classroom attendance management
- Reduce manual attendance work
- Store attendance records securely
- Improve attendance tracking efficiency
- Provide a modern user-friendly interface
- Enable teachers to manage students dynamically

---

# 3. Scope of the Project

The system is designed specifically for:

```text
Diploma CSE 2025–26 Final Semester

The application allows teachers to:

✅ Login securely
✅ View all students
✅ Mark attendance daily
✅ Add new students
✅ Remove students
✅ Track attendance statistics

4. Objectives
Main Objectives
Create a secure attendance management platform
Store attendance records date-wise
Develop a responsive dashboard
Implement student management functionality
Create analytics for attendance tracking
Learn full-stack development concepts
5. Functional Requirements
5.1 Home Page

The system shall provide:

Modern landing page
Navigation bar
Project information
Teacher login button
Dashboard navigation
5.2 Login System

The system shall:

Allow teacher authentication
Validate username and password
Protect dashboard routes using sessions
Allow secure logout
5.3 Dashboard

The dashboard shall display:

Total number of students
Present students count
Absent students count
Current date
Attendance management controls
5.4 Student Management

The system shall allow teachers to:

Add students
Remove students
View all student records
Manage attendance dynamically
5.5 Attendance Management

The system shall:

Mark students as Present
Mark students as Absent
Store attendance date-wise
Prevent duplicate attendance entries
5.6 Reports

The system shall provide:

Attendance history
Daily attendance records
Student attendance tracking
Attendance analytics
6. Non-Functional Requirements
6.1 Performance
Fast page loading
Efficient database queries
Smooth UI interactions
6.2 Security
Session-based authentication
Protected dashboard access
Secure database credential handling using .env
6.3 Usability
User-friendly interface
Responsive design
Easy navigation
Modern dashboard UI
6.4 Reliability
Stable database operations
Proper attendance storage
Consistent attendance tracking

| Technology | Purpose             |
| ---------- | ------------------- |
| Python     | Backend Development |
| Flask      | Web Framework       |
| MySQL      | Database            |
| HTML5      | Structure           |
| CSS3       | Styling             |
| JavaScript | Interactivity       |
| Bootstrap  | Responsive UI       |
| Chart.js   | Graphs & Analytics  |


| Component | Requirement             |
| --------- | ----------------------- |
| Processor | Intel i3 or above       |
| RAM       | 4 GB Minimum            |
| Storage   | 500 MB Free Space       |
| Internet  | Required for deployment |


| Software    | Version     |
| ----------- | ----------- |
| Python      | 3.x         |
| Flask       | Latest      |
| MySQL       | 8.x         |
| VS Code     | Latest      |
| Web Browser | Chrome/Edge |


14. Testing

The application was tested for:
✅ Authentication
✅ Attendance Storage
✅ Student CRUD Operations
✅ Session Protection
✅ Database Connectivity
✅ Responsive UI