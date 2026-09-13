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

### 🆕 New Python Version Features

* 🏅 Determine honor eligibility
* 🏆 Identify students with Honors
* 🥇 Identify students with High Honors
* 👑 Identify students with Highest Honors
* 📚 Calculate an equivalent grade point
* ⚠️ Determine student academic risk level
* 🚨 Identify students who are at risk
* 📊 Track grade distribution from A to F
* 🏆 Rank students based on their average
* 🥇 Display the Top 3 students
* 📋 Store individual student records for class analysis
* 📅 Calculate the class attendance average
* 🏅 Find the student with the highest attendance
* 📚 Calculate the average grade for every subject
* ⭐ Identify the best-performing subject
* 📉 Identify the most difficult subject based on class average
* 📝 Display an honor students list
* 🚨 Display an at-risk students list
* 💡 Generate an overall class recommendation
* 📊 Provide additional class performance statistics

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
* Dictionaries
* String formatting
* Sorting
* `max()` and `min()` functions
* Lambda functions
* Basic statistics and calculations
* Storing and processing multiple records

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
   * Honor eligibility
   * Grade point
   * Academic risk level
7. A detailed student performance report is displayed.
8. The student's information is stored for further class analysis.
9. After processing all students, a class summary is generated.
10. The program calculates the average performance of every subject.
11. The program identifies the best-performing and most difficult subjects.
12. Students are ranked from highest to lowest average.
13. The Top 3 students are displayed.
14. At-risk students and honor students are displayed.
15. Grade distribution and attendance statistics are calculated.
16. The program provides an overall class recommendation.

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

## 📈 Performance Levels

|  Average | Performance       |
| -------: | :---------------- |
|   95–100 | Outstanding       |
|    90–94 | Excellent         |
|    85–89 | Very Good         |
|    80–84 | Good              |
|    75–79 | Satisfactory      |
|    60–74 | Needs Improvement |
| Below 60 | Poor              |

## ✅ Academic Status

A student is considered **PASSED** when:

* Average is **75 or higher**
* Attendance is **80% or higher**

Otherwise, the student is marked **FAILED**.

## 🎓 Scholarship Eligibility

A student qualifies for a scholarship when:

* Average is **90 or higher**
* Attendance is **90% or higher**

## 🏅 Honor Eligibility

The Python version now includes an additional honor classification system.

| Requirement                     | Honor Status        |
| :------------------------------ | :------------------ |
| Average 85+ and Attendance 85%+ | With Honors         |
| Average 90+ and Attendance 90%+ | With High Honors    |
| Average 95+ and Attendance 90%+ | With Highest Honors |
| Does not meet requirements      | No Honor            |

This allows the program to identify students who meet different academic achievement levels.

## ⚠️ Academic Warning

An academic warning is given when:

* The student's average is below **75**, or
* Attendance is below **80%**

The program also identifies whether the issue is related to grades, attendance, or both.

## 🚨 Academic Risk Level

The Python version also analyzes the student's overall academic risk.

| Condition                                 | Risk Level    |
| :---------------------------------------- | :------------ |
| Average 75+ and Attendance 80%+           | Low Risk      |
| Average below 75 OR Attendance below 80%  | Moderate Risk |
| Average below 75 AND Attendance below 80% | High Risk     |

This allows the program to quickly identify students who may need additional academic support.

## 📊 Class Statistics

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
* Class attendance average
* Student with the highest attendance
* Number of students at risk
* Number of honor students
* Grade distribution

The web version displays these statistics directly on the dashboard and automatically updates them when student records are added or deleted.

## 🏆 Student Ranking

The Python version now stores the processed student records and sorts them according to their average.

The ranking displays:

* Student rank
* Student name
* Average
* Letter grade
* Academic status

The program also displays the **Top 3 students** separately for quick identification of the highest-performing students.

## 🚨 At-Risk Students

The program provides a separate list of students who have either:

* An average below 75
* Attendance below 80%
* Both low academic performance and low attendance

This makes it easier to identify students who may require additional academic support.

## 🏅 Honor Students

The program also generates a separate list of students who qualify for:

* With Honors
* With High Honors
* With Highest Honors

This provides a quick overview of the students with strong academic performance.

## 📚 Subject Class Performance

The Python version now calculates the **class average for every subject**.

The subjects analyzed are:

* Programming
* Database
* Mathematics
* Networking
* Web Development

The program then identifies:

* The best-performing subject
* The highest subject average
* The most difficult subject
* The lowest subject average

This allows the user to determine which subjects the class performs well in and which subjects may require additional attention.

## 📊 Grade Distribution

The program counts the number of students who received each letter grade:

* A
* B
* C
* D
* F

This provides a quick overview of the overall grade distribution of the class.

## 📅 Attendance Statistics

The Python version also analyzes class attendance.

It calculates:

* Class attendance average
* Highest attendance percentage
* Student with the highest attendance

This allows attendance to be analyzed alongside academic performance.

## 💡 Class Recommendation

After analyzing the class, the program provides a recommendation based on:

* Overall class average
* Overall attendance average
* Academic performance
* Attendance performance

The recommendation can indicate whether the class is performing excellently, satisfactorily, or needs improvement.

## 💻 Technologies Used

### Python Version

* Python 3.x
* Functions
* Conditional statements
* Loops
* Lists
* Dictionaries
* Sorting
* Lambda functions
* `max()` and `min()`
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

The Python version stores student information in memory while the program is running. Student records are placed into a list of dictionaries so they can be sorted, analyzed, and included in additional class reports.

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
├── web-version/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── python-version/
    └── index.py
```

The project now contains two versions:

### Python Version

* Console-based student grade management system
* Focuses on Python programming logic and problem solving
* Performs student ranking and class analysis
* Provides academic risk and honor analysis
* Calculates subject performance statistics
* Generates detailed class recommendations

### Web Version

* Browser-based student grade management system
* Focuses on HTML, CSS, JavaScript, UI design, and interactivity
* Uses LocalStorage for student records
* Provides an interactive dashboard for managing students

## 🎯 Purpose

This project was created as a beginner-level Python programming project to practice **programming logic, functions, conditional statements, loops, input validation, and basic data analysis**.

The project was later expanded into a web application to practice **HTML, CSS, JavaScript, DOM manipulation, form handling, LocalStorage, responsive design, and user interface development**.

The Python version has also been expanded to demonstrate more programming concepts such as **lists of dictionaries, sorting, lambda functions, `max()` and `min()`, record management, ranking systems, academic risk analysis, honor classification, and subject-level statistics**.

The goal is to demonstrate how the same student grade management logic can be implemented in both a **Python console application** and an **interactive web application**.

## 👨‍💻 Author

**Jose Navoa**

First-Year Information Technology Student

## 📄 License

This project is for **educational and learning purposes**.
