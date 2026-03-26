# MCQ-Exam-Project

A comprehensive Multiple Choice Question (MCQ) Exam System developed in Python, designed to manage students, exams, and grading efficiently.

## Features

### 1. User Management
*   **Signup:** Register new students with a unique user code and name.
*   **Login:** Secure login for existing students using their assigned codes.
*   **Persistence:** User data is saved in `users.json` for long-term storage.

### 2. Versatile Exam System
*   **Subjects:** Currently supports both **English** and **Math**.
*   **Difficulty Settings:** Three selectable levels of difficulty: **Easy**, **Intermediate**, and **Hard**.
*   **Customization:** Students can define the number of questions they wish to answer in a session.
*   **Randomization:** Questions are selected randomly from JSON data banks to ensure variety.

### 3. Grading and Performance Tracking
*   **Real-time Results:** Immediate calculation of scores upon exam completion.
*   **Grade History:** Detailed records (Subject, Level, Score) are logged into `grades.csv`.
*   **Result Inquiry:** Students can review their past performance by entering their unique code.

## Technologies Used
*   **Core:** Python 3
*   **Data Formats:** JSON (Questions & Users), CSV (Grades)
*   **Libraries:** `json`, `csv`, `random`, `os` (Standard Python Libraries)

## Project Structure
*   `exam.py`: The main application logic and interface.
*   `MCQ.*.json`: Question banks categorized by subject and difficulty.
*   `users.json`: Stores user account information.
*   `grades.csv`: Historical record of all student grades.

## How to Run
1. Ensure you have Python 3 installed.
2. Clone or download the project files.
3. Run the application using:
   ```bash
   python exam.py
   ```
4. Follow the on-screen menu to sign up, log in, or take an exam.