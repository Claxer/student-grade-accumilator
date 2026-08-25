# 🎓 Student Grade Management and Performance Analyzer

A beginner-friendly **Student Grade Management and Performance Analyzer** that manages and analyzes student academic performance. The program accepts grades and attendance, calculates averages, determines letter grades and academic status, and provides detailed performance reports.

The project started as a **Python console-based application** and was later expanded into a **web-based application using HTML, CSS, and JavaScript**.

## 📌 Features

* 👨‍🎓 Process multiple students
* 📚 Record grades for:

  * Programming
  * Database
  * Mathematics
  * Networking
  * Web Development
* 📊 Calculate student averages
* 🏆 Determine letter grades from A to F
* ✅ Determine academic status
* 📈 Analyze student performance
* 🎓 Check scholarship eligibility
* ⚠️ Identify students who need academic warnings
* 📋 Analyze individual subject performance
* 🏫 Generate an overall class summary
* 🥇 Find the highest and lowest-performing students
* 📊 Calculate class average, pass percentage, and failure percentage

### 🌐 Web Version Features

* 💻 Interactive web-based dashboard
* 👨‍🎓 Add and manage student records
* 📝 Add student grades and attendance
* 📊 Automatic average calculation
* 🏆 Automatic letter grade calculation
* ✅ Automatic academic status detection
* 📈 Automatic performance level detection
* 🎓 Automatic scholarship eligibility checking
* ⚠️ Automatic academic warning detection
* 🔎 Search student records
* 👁️ View detailed student information
* 🗑️ Delete student records
* 📋 Generate individual student performance reports
* 📊 Display class statistics on the dashboard
* 🥇 Display highest-performing student
* 📉 Display lowest-performing student
* 💾 Save student records using browser LocalStorage
* 📱 Responsive web interface
* 🪟 Student details modal
* 🔔 Interactive notifications and user feedback

## 🛠️ Concepts Used

This project demonstrates basic Python programming concepts, including:

* Functions
* `if`, `elif`, and `else` statements
* `for` loops
* Nested loops
* Logical operators (`and`, `or`)
* Arithmetic operators
* Input validation
* Variables and data types
* Lists
* String formatting
* Basic statistics and calculations

### 🌐 Web Development Concepts Used

The web version also demonstrates:

* HTML5
* CSS3
* JavaScript
* Arrays and objects
* DOM manipulation
* Event handling
* Form handling
* LocalStorage
* Responsive web design
* Modal interfaces
* Search and filtering
* Dynamic content updates

## ⚙️ How It Works

### 🐍 Python Version

1. The user enters the number of students to process.
2. The program asks for each student's name.
3. Grades for five subjects are entered.
4. The student's attendance percentage is entered.
5. The program calculates the student's average.
6. It determines the:

   * Letter grade
   * Academic status
   * Performance level
   * Scholarship eligibility
   * Academic warning
7. A detailed student performance report is displayed.
8. After processing all students, a class summary is generated.

### 🌐 Web Version

1. The user opens the web application.
2. Student information is entered through the student form.
3. Grades and attendance are entered.
4. The system validates the entered information.
5. JavaScript automatically calculates the student's average.
6. The system determines the:

   * Letter grade
   * Academic status
   * Performance level
   * Scholarship eligibility
   * Academic warning
7. The student record is added to the dashboard.
8. Class statistics are automatically updated.
9. Students can be searched and their details can be viewed.
10. Student records can be deleted from the dashboard.
11. Student information is saved using browser LocalStorage.

## 📊 Grading System

|  Average | Letter Grade |
| -------: | :----------: |
|   90–100 |       A      |
|    80–89 |       B      |
|    70–79 |       C      |
|    60–69 |       D      |
| Below 60 |       F      |

## ✅ Academic Status

A student is considered **PASSED** when:

* Average is **75 or higher**
* Attendance is **80% or higher**

Otherwise, the student is marked **FAILED**.

## 🎓 Scholarship Eligibility

A student qualifies for a scholarship when:

* Average is **90 or higher**
* Attendance is **90% or higher**

## ⚠️ Academic Warning

An academic warning is given when:

* The student's average is below **75**, or
* Attendance is below **80%**

The program also identifies whether the issue is related to grades, attendance, or both.

## 📈 Class Statistics

After all students have been processed, the program displays:

* Total number of students
* Number of passed students
* Number of failed students
* Pass percentage
* Failure percentage
* Number of excellent students
* Class average
* Highest average
* Top student
* Lowest average
* Lowest-performing student
* Overall class performance

The web version displays these statistics directly on the dashboard and automatically updates them when student records are added or deleted.

## 💻 Technologies Used

### Python Version

* Python 3.x
* Functions
* Conditional statements
* Loops
* Lists
* Basic statistics and calculations

### Web Version

* HTML5
* CSS3
* JavaScript
* LocalStorage
* Responsive Web Design

## 💾 Data Storage

The web version uses **LocalStorage** to save student records in the browser.

This allows student information to remain available even after refreshing the webpage.

> Note: LocalStorage is used for this educational project and is not intended to replace a production database.

## 💻 Requirements

### Python Version

* Python 3.x
* No external libraries are required.

### Web Version

* Modern web browser
* No additional libraries or frameworks are required.

## 🚀 How to Run

### 🐍 Python Version

1. Install **Python 3** on your computer.
2. Clone this repository:

```bash
git clone https://github.com/yourusername/student-grade-management.git
```

3. Open the project folder.
4. Run the Python file:

```bash
python main.py
```

5. Follow the instructions displayed in the terminal.

### 🌐 Web Version

1. Open the project folder.
2. Navigate to the web version folder.
3. Open `index.html` in a web browser.

You can also use **VS Code with Live Server** for easier development.

## 📁 Project Structure

```text
Student-Grade-Management/
│
├── README.md
│
└── web-version/
    ├── index.html
    ├── style.css
    └── script.js
└── python-version/
    └── main.py
    
```

The project now contains two versions:

**Python Version**

* Console-based student grade management system
* Focuses on Python programming logic and problem solving

**Web Version**

* Browser-based student grade management system
* Focuses on HTML, CSS, JavaScript, UI design, and interactivity

## 🎯 Purpose

This project was created as a beginner-level Python programming project to practice **programming logic, functions, conditional statements, loops, input validation, and basic data analysis**.

The project was later expanded into a web application to practice **HTML, CSS, JavaScript, DOM manipulation, form handling, LocalStorage, responsive design, and user interface development**.

The goal is to demonstrate how the same student grade management logic can be implemented in both a **Python console application** and an **interactive web application**.

## 👨‍💻 Author

**Jose Navoa**

First-Year Information Technology Student

## 📄 License

This project is for **educational and learning purposes**.
